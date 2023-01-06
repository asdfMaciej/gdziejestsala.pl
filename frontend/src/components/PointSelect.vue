<script lang="ts">
export default {
  props: ['floors', 'points'],

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
      return !(this.selectedFloorId == null || this.selectedPointId == null);
    },

    selectedFloorPoints() {
      const floorPointIsSelected = (floorPoint) => floorPoint.floor_id === this.selectedFloorId;
      const pointHasSelectedFloor = (point) => point.floors.some(floorPointIsSelected);
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
  <div>
    <h3>Wybierz piętro</h3>
    <select v-model="selectedFloorId">
      <option :value="null">--</option>
      <option v-for="floor of floors" :value="floor.id">{{ floor.name }}</option>
    </select>
    <h3>Wybierz punkt</h3>
    <select v-model="selectedPointId">
      <option :value="null">--</option>
      <option v-for="point of selectedFloorPoints" :value="point.id">{{ point.name }}</option>
    </select>
    <br>
    <button :disabled="!canSubmit" @click="submit">Zatwierdź</button>
  </div>
</template>

<style scoped>

</style>
