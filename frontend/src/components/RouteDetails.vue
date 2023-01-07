<script setup lang="ts">
import type { Path, FloorPoint, Point, Floor } from '@/api/models';
import { computed } from 'vue';
import { useDataStore } from '@/stores/data';

const dataStore = useDataStore();
const props = defineProps<{
    route: Path
}>();

interface PathPoint {
    type: 'Point',
    point: Point
};

interface PathFloor {
    type: 'Floor',
    floor: Floor
}

let path = computed(() => {
    let path: Array<PathPoint | PathFloor> = [];
    let currentFloorId: number | null = null;

    for (let point of props.route) {
        // Display a header once you switch the floor
        //   - for ex. going from stairs to a hallway / classroom,
        //     but not when entering stairs / elevator
        if (point.floors.length === 1 && point.floors[0].floor_id != currentFloorId) {
            currentFloorId = point.floors[0].floor_id;
            const floor = dataStore.floors.find(floor => floor.id === currentFloorId) as Floor;
            path.push({
                type: 'Floor',
                floor: floor
            });
        }

        path.push({
            type: 'Point',
            point: point
        })
    }

    return path;
});

</script>

<template>
    <article>
        <template v-for="node in path">
            <div v-if="node.type === 'Point'">
                {{ node.point.name }} ({{ node.point.description }})
                <br>

                <RouterLink :to="{ name: 'view-point', params: { 'point_id': node.point.id } }">Point details
                </RouterLink>
            </div>
            <div v-else-if="node.type === 'Floor'">
                Piętro {{ node.floor.name }}

                <RouterLink :to="{ name: 'view-floor', params: { 'floor_id': node.floor.id } }">Floor details
                </RouterLink>
            </div>
        </template>
    </article>
</template>

<style scoped>

</style>
