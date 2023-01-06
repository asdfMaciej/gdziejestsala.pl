<script setup lang="ts">
import { useRoute } from 'vue-router';
import { useRouteStore } from '../stores/routes';

const routeStore = useRouteStore();

const route = useRoute();
const startId = route.params.start_id;
const destinationId = route.params.destination_id;

routeStore.fetchRoute(startId, destinationId);
</script>

<template>
    <div class="about">
        <h1>route from {{ startId }} to {{ destinationId }} view</h1>

        {{ routeStore.getRoute(startId, destinationId) }}
    </div>
</template>
  
<style>

</style>
  