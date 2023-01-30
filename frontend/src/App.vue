<script setup lang="ts">
import { onMounted, computed, inject } from 'vue';
import { RouterLink, RouterView } from 'vue-router'
import { useDataStore } from './stores/data';

const dataStore = useDataStore();
onMounted(() => {
  dataStore.fetchData();
});

const $debug = inject('$debug');
</script>

<template>
  <header>
    <div class="wrapper">
      <nav v-if="$debug">
        <span>Debug menu (CD test):</span>
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
  <RouterView v-slot="{ Component }">
    <keep-alive>
      <component :is="Component" :key="$route.fullPath"></component>
    </keep-alive>
  </RouterView>
</template>

<style scoped>

</style>
