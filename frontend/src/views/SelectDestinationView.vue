<script setup lang="ts">
import { useRoute } from 'vue-router';
import PointSelect from "../components/PointSelect.vue"

const route = useRoute();
const start_id = route.params.start_id;
</script>

<template>
    <div class="about">
        <h1>route from {{ start_id }} - select destination view</h1>

        <PointSelect />
    </div>
</template>
  
<style>

</style>
  