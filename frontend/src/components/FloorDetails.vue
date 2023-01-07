<script setup lang="ts">
import type { Floor, Path } from '@/api/models';
import { computed } from 'vue';
import { getRoutePointsOnFloor } from '@/helpers/route-display-helper';
import { useDataStore } from '@/stores/data';

const props = defineProps<{
    floor: Floor,
    path: Path | null
}>();

const showPath = computed(() => !(props.path == null));


const floorPoints = computed(() => getRoutePointsOnFloor(props.path as Path)[props.floor.id]);
</script>

<template>
    <article>
        <h1>>{{ floor.name }}</h1>
        <p>{{ floor.description }}</p>
        <img v-if="floor.map_image" :src="floor.map_image.url">

        <template v-if="showPath">
            <h2>Punkty na piętrze:</h2>
            <ol>
                <li v-for="point in floorPoints">{{ point }}</li>
            </ol>
        </template>
    </article>
</template>

<style scoped>
img {
    max-width: 500px;
}
</style>
