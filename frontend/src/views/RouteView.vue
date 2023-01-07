<script setup lang="ts">
import { useRoute } from 'vue-router';
import { useRouteStore } from '../stores/routes';
import { computed, ref } from 'vue';
import type { Path } from '@/api/models';
import RouteDetails from '@/components/RouteDetails.vue';

const routeStore = useRouteStore();

const route = useRoute();
const startId = computed(() => route.params.start_id as string);
const destinationId = computed(() => route.params.destination_id as string);

const pathPromise = routeStore.getRoute(route.params.start_id as string, route.params.destination_id as string);
pathPromise.then(result => { path.value = result; })

let path = ref<Path | null>(null);


</script>

<template>
    <div class="about">
        <h1>route from {{ startId }} to {{ destinationId }} view</h1>
        <RouteDetails :route="(path as Path)"></RouteDetails>
    </div>
</template>

<style>

</style>
