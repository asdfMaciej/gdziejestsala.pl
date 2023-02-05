<script setup lang="ts">
import { useRoute } from 'vue-router';
import { useRouteStore } from '../stores/routes';
import { computed, ref } from 'vue';
import type { Path } from '@/api/models';
import RouteDetails from '@/components/RouteDetails.vue';
import { useDataStore } from '@/stores/data';

const routeStore = useRouteStore();
const dataStore = useDataStore();

const route = useRoute();
const startId = route.params.start_id as string;
const destinationId = route.params.destination_id as string;

const startName = computed(() =>
    dataStore.points
        .filter(p => p.id == startId as unknown as number)
        .map(x => x.name)
        .find(() => true) || startId
);

const destinationName = computed(() =>
    dataStore.points
        .filter(p => p.id == destinationId as unknown as number)
        .map(x => x.name)
        .find(() => true) || destinationId
);

const pathPromise = routeStore.getRoute(route.params.start_id as string, route.params.destination_id as string);
pathPromise.then(result => { path.value = result; })

let path = ref<Path | null>(null);

const log = console.log;
</script>

<template>
    <section class="about">
        <h1>Trasa od {{ startName }} do {{ destinationName }}</h1>
        <p class="caption">Naciśnij na nazwę aby zobaczyć szczegóły budynku lub miejsca.</p>
        <RouteDetails @click="log(route.params)" :start-id="startId" :destination-id="destinationId"
            :route="(path as Path)"></RouteDetails>
    </section>
</template>

<style scoped lang="scss">
section.about {
    h1 {
        margin-bottom: 0.5em;
    }

    .caption {
        margin-bottom: 1.5em;
    }
}

.caption {
    color: var(--hex-lightgrey);
}
</style>
