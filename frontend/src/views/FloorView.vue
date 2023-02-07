<script setup lang="ts">
import { useRoute } from 'vue-router';
import { useDataStore } from '@/stores/data';
import { useRouteStore } from '@/stores/routes';
import { computed, ref } from 'vue';
import { changeTitle } from '@/helpers/metatags';
import FloorMap from '@/components/FloorMap.vue';
import BackButton from '@/components/BackButton.vue';
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

const header = computed(() => displayPathPoints ? 'Szczegóły piętra' : 'Szczegóły piętra');

changeTitle('Szczegóły piętra');
</script>

<template>
    <section class="about">
        <h1>{{ header }}</h1>

        <template v-if="floor">
            <h1>{{ floor.name }}</h1>
            <p>{{ floor.description }}</p>
            <FloorMap :floor="floor" :points="path"></FloorMap>
        </template>
        <template v-else-if="loading">
            Ładowanie...
        </template>
        <template v-else>
            Nie znaleziono piętra!
        </template>
    </section>
    <BackButton />
</template>

<style scoped>
section {
    flex: 1;
}
</style>
