<script setup lang="ts">
import { useRoute } from 'vue-router';
import { useRouteStore } from '../stores/routes';
import { computed } from 'vue';
import RouteDetails from '@/components/RouteDetails.vue';

const routeStore = useRouteStore();

const route = useRoute();
const startId = computed(() => route.params.start_id as string);
const destinationId = computed(() => route.params.destination_id as string);

routeStore.fetchRoute(route.params.start_id as string, route.params.destination_id as string);

</script>

<template>
    <div class="about">
        <h1>route from {{ startId }} to {{ destinationId }} view</h1>
        <RouteDetails v-if="routeStore.getRoute(startId, destinationId)"
            :route="routeStore.getRoute(startId, destinationId)"></RouteDetails>
    </div>
</template>

<style>

</style>
