<script setup lang="ts">
import { useRoute } from 'vue-router';
import { useDataStore } from '../stores/data';
import { computed } from 'vue';

const dataStore = useDataStore();

const route = useRoute();
const routeFloorId = computed(() => route.params.floor_id);

const floor = computed(() => dataStore.floors.find(floor => floor.id == route.params.floor_id));
const loading = computed(() => dataStore.floors.length == 0);

</script>

<template>
    <div class="about">
        <h1>floor #{{ routeFloorId }} details</h1>

        <template v-if="floor">
            {{ floor }}
        </template>
        <template v-else-if="loading">
            Ładowanie...
        </template>
        <template v-else>
            Nie znaleziono piętra!
        </template>

    </div>
</template>
  
<style>

</style>
  