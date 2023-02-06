<script lang="ts">
import type { FloorPoint, Point, Floor } from "../api/models";
import type { PropType } from 'vue';

// TODO: Refactor to use the Composition API and type-based declaration (defineProps)
export default {
  props: {
    floors: {
      type: Array as PropType<Floor[]>,
      required: true
    },
    points: {
      type: Array as PropType<Point[]>,
      required: true
    }
  },

  methods: {
    submit() {
      if (!this.canSubmit) { return console.error("Invalid selection!"); }
      this.$emit('selected', this.selectedPointId);
    }
  },

  data() {
    return {
      selectedFloorId: null,
      selectedPointId: null
    };
  },

  computed: {
    canSubmit() {
      return !(this.selectedPointId == null);
    },

    selectedFloorPoints() {
      if (this.selectedFloorId == null)
        return this.points;

      const floorPointIsSelected = (floorPoint: FloorPoint) => floorPoint.floor_id === this.selectedFloorId;
      const pointHasSelectedFloor = (point: Point) => point.floors.some(floorPointIsSelected);
      return this.points.filter(pointHasSelectedFloor);
    }
  },

  watch: {
    selectedFloorId() {
      this.selectedPointId = null;
    }
  }
};
</script>

<template>
  <article>
    <h3>Filtruj po piętrze</h3>
    <select v-model="selectedFloorId">
      <option :value="null">--</option>
      <option v-for="floor of floors" :value="floor.id">{{ floor.name }}</option>
    </select>

    <h2>Wybierz punkt</h2>
    <select v-model="selectedPointId">
      <option :value="null">--</option>
      <option v-for="point of selectedFloorPoints" :value="point.id">{{ point.name }}</option>
    </select>

    <button :disabled="!canSubmit" @click="submit">Zatwierdź</button>
  </article>
</template>

<style scoped>

</style>
