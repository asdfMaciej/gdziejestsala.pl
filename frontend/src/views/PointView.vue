<script setup lang="ts">
import { useRoute } from 'vue-router';
import { useDataStore } from '../stores/data';
import { computed } from 'vue';

const dataStore = useDataStore();

const route = useRoute();
const routePointId = computed(() => route.params.point_id);

const point = computed(() => dataStore.points.find(point => point.id === parseInt(route.params.point_id as string, 10)));
const loading = computed(() => dataStore.points.length == 0);
</script>

<template>
    <div class="about">
        <h1>point #{{ routePointId }} details</h1>

        <template v-if="point">
            {{ point }}
        </template>
        <template v-else-if="loading">
            Ładowanie...
        </template>
        <template v-else>
            Nie znaleziono miejsca!
        </template>
    </div>
</template>
  
<style>

</style>
  