<script setup lang="ts">
import { useRoute } from 'vue-router';

const route = useRoute();
const start_id = route.params.start_id;
</script>

<template>
    <div class="about">
        <h1>route from {{ start_id }} - select destination view</h1>
    </div>
</template>
  
<style>

</style>
  