<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'

const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;
</script>

<template>
  <header>
    <div class="wrapper">
      BACKEND URL: {{ BACKEND_URL }}

      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>

</style>
