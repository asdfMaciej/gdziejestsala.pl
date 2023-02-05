<script setup lang="ts">
import type { Floor, Path } from '@/api/models';
import type { FloorPointDetails } from '@/helpers/route-display-helper';
import { computed, watch, ref, onMounted, nextTick } from 'vue';
import { getRoutePointsOnFloor } from '@/helpers/route-display-helper';


const props = defineProps<{
    floor: Floor,
    path: Path | null
}>();

const showPath = computed(() => !(props.path == null));
const floorPoints = computed(() => getRoutePointsOnFloor(props.path as Path, props.floor.id));

// Stores a reference to the HTML5 canvas element
const canvasRef: any = ref(null);

const drawPointsOnCanvas = (pointsOnFloor: FloorPointDetails[]) => {
    const canvas = canvasRef.value;
    const ctx = canvas.getContext("2d");
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    if (!pointsOnFloor)
        return;

    for (const { floorPoint, point } of pointsOnFloor) {
        const x = floorPoint.x;
        const y = floorPoint.y;
        if (x && y) {
            drawCircle(ctx, x, y);
        }
    }
}

const drawCircle = (ctx: any, x: any, y: any) => {
    ctx.beginPath();
    ctx.fillStyle = "#ffffff";
    ctx.arc(x, y, 25, 0, 2 * Math.PI, 0);
    ctx.fill();

    ctx.beginPath();
    ctx.fillStyle = "#000000";
    ctx.arc(x, y, 15, 0, 2 * Math.PI, 0);
    ctx.fill();
}

onMounted(() => {
    // Redrawing canvas points on each change
    // Creating a watcher in onMounted() to ensure that the canvas ref is populated
    watch(
        floorPoints,
        (points) => {
            drawPointsOnCanvas(points);
        }, { immediate: true });
    // Immediate watcher will fire on variable change and upon creation
});

</script>

<template>
    <article>
        <h1>{{ floor.name }}</h1>
        <p>{{ floor.description }}</p>
        <div class="floor-image">
            <img v-if="floor.map_image" :src="floor.map_image.url">
            <canvas v-if="floor.map_image" :width="floor.map_image.width" :height="floor.map_image.height"
                ref="canvasRef"></canvas>
        </div>

        <template v-if="showPath">
            <h2>Punkty na piętrze:</h2>
            <ol>
                <li v-for="point in floorPoints">{{ point.point.name }}</li>
            </ol>
        </template>
    </article>
</template>

<style scoped>
img {
    max-width: 500px;
}

.floor-image {
    position: relative;
    display: inline-block;
    max-width: 100%;
}

.floor-image img {
    display: block;
    max-width: 100%;
}

.floor-image canvas {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 10;
}
</style>
