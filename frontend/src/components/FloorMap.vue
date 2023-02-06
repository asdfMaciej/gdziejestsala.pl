<script setup lang="ts">
import type { Floor, Point } from '@/api/models';
import type { FloorPointDetails } from '@/helpers/route-display-helper';
import { computed, watch, ref, onMounted, nextTick } from 'vue';
import { getRoutePointsOnFloor } from '@/helpers/route-display-helper';


const props = defineProps<{
    floor: Floor,
    points: Point[] | null
}>();

const showPath = computed(() => !(props.points == null));
const floorPoints = computed(() => getRoutePointsOnFloor(props.points as Point[], props.floor.id));

// Stores a reference to the HTML5 canvas element
const canvasRef: any = ref(null);

const drawPointsOnCanvas = (pointsOnFloor: FloorPointDetails[]) => {
    const canvas = canvasRef.value;
    const ctx = canvas.getContext("2d");
    ctx.textBaseline = 'middle';
    ctx.textAlign = 'center';

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    if (!pointsOnFloor)
        return;

    let no = 1;
    for (const { floorPoint, point } of pointsOnFloor) {
        const x = floorPoint.x;
        const y = floorPoint.y;
        if (x && y) {
            drawCircle(ctx, x, y, no);
        }
        no += 1;
    }
}

const drawCircle = (ctx: any, x: any, y: any, no: number) => {
    const colors = [
        // border, inside, text
        ["#ff0000", "#ff0000", "#ffffff"],
        ["#0000ff", "#0000ff", "#ffffff"]
    ];

    const color = colors[no % 2];

    ctx.beginPath();
    ctx.fillStyle = color[0];
    ctx.arc(x, y, 25, 0, 2 * Math.PI, 0);
    ctx.fill();

    ctx.beginPath();
    ctx.fillStyle = color[1];
    ctx.arc(x, y, 22, 0, 2 * Math.PI, 0);
    ctx.fill();

    ctx.fillStyle = color[2];
    ctx.font = 'bold 26px sans-serif';
    ctx.fillText(no, x, y);
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

        <div class="floor-image">
            <img v-if="floor.map_image" :src="floor.map_image.url">
            <canvas v-if="floor.map_image" :width="floor.map_image.width" :height="floor.map_image.height"
                ref="canvasRef"></canvas>
        </div>

        <template v-if="showPath">
            <h2>Punkty na piętrze:</h2>
            <ol>
                <li v-for="point in floorPoints">
                    <RouterLink :to="{ name: 'view-point', params: { 'point_id': point.point.id } }">{{
                        point.point.name
                    }}</RouterLink>
                </li>
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
