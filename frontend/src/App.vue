<script setup lang="ts">
import { onMounted, computed } from 'vue';
import { RouterLink, RouterView } from 'vue-router'
import { useDataStore } from './stores/data';

const dataStore = useDataStore();
onMounted(() => {
  dataStore.fetchData();
});

</script>

<template>
  <header>
    <div class="wrapper">
      <nav>
        <span>Debug menu:</span>
        <RouterLink :to="{ name: 'home' }">Home</RouterLink>
        <RouterLink :to="{ name: 'select-start', params: {} }">Select start</RouterLink>
        <RouterLink :to="{ name: 'select-destination', params: { 'start_id': '1' } }">Select destination</RouterLink>
        <RouterLink :to="{ name: 'view-route', params: { 'start_id': '1', 'destination_id': '2' } }">View route
        </RouterLink>
        <RouterLink :to="{ name: 'view-point', params: { 'point_id': '1' } }">Point details</RouterLink>
        <RouterLink :to="{ name: 'view-floor', params: { 'floor_id': '1' } }">Floor details</RouterLink>
        <RouterLink :to="{ name: 'about' }">About application</RouterLink>
      </nav>
    </div>
  </header>

  <div v-for="(point, point_id) in dataStore.points">
    {{ point }}
  </div>

  <div v-for="(floor, floor_id) in dataStore.floors">
    {{ floor }}
  </div>

  <RouterView />
</template>

<style scoped>

</style>
