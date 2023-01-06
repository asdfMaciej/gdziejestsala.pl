<script setup lang="ts">
import PointSelect from "../components/PointSelect.vue"
import { useDataStore } from '../stores/data';

const dataStore = useDataStore();

</script>
<template>
    <div class="about">
        <h1>select start view</h1>

        <PointSelect :floors="dataStore.floors" :points="dataStore.points" />
    </div>
</template>
  
<style>

</style>
  