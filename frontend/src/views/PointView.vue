<script setup lang="ts">
import { useRoute } from 'vue-router';

const route = useRoute();
const point_id = route.params.point_id;
</script>

<template>
    <div class="about">
        <h1>point #{{ point_id }} details</h1>
    </div>
</template>
  
<style>

</style>
  