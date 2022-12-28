<script setup lang="ts">
import { useRoute } from 'vue-router';

const route = useRoute();
const floor_id = route.params.floor_id;
</script>

<template>
    <div class="about">
        <h1>floor #{{ floor_id }} details</h1>
    </div>
</template>
  
<style>

</style>
  