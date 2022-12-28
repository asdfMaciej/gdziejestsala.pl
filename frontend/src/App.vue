<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'

const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;
</script>

<template>
  <header>
    <div class="wrapper">
      BACKEND URL: {{ BACKEND_URL }}

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

  <RouterView />
</template>

<style scoped>

</style>
