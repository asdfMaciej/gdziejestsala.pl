<script setup lang="ts">
import { useRoute } from 'vue-router';
import { useDataStore } from '../stores/data';
import { useRouteStore } from '../stores/routes';
import { computed, ref } from 'vue';
import FloorDetails from '@/components/FloorDetails.vue';
import type { Path } from '@/api/models';

const dataStore = useDataStore();

const route = useRoute();

const floor = computed(() => dataStore.floors.find(floor => floor.id === parseInt(route.params.floor_id as string, 10)));
const loading = computed(() => dataStore.floors.length == 0);

const displayPathPoints = !(route.params.start_id == null);

let path = ref<Path | null>(null);

if (displayPathPoints) {
    const routeStore = useRouteStore();
    routeStore.getRoute(route.params.start_id as string, route.params.destination_id as string).then(_path => {
        path.value = _path;
    });
}

const header = computed(() => displayPathPoints ? 'Punkty na piętrze' : 'Szczegóły piętra');

</script>

<template>
    <div class="about">
        <h1>{{ header }}</h1>

        <template v-if="floor">
            <FloorDetails :floor="floor" :path="path"></FloorDetails>
        </template>
        <template v-else-if="loading">
            Ładowanie...
        </template>
        <template v-else>
            Nie znaleziono piętra!
        </template>

    </div>
</template>

<style>

</style>
