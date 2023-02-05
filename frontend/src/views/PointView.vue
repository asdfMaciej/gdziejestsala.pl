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
    <section class="about">
        <template v-if="point">
            <h1>{{ point.name }}</h1>
            <p>{{ point.description }}</p>
            <!-- todo: image -->

            <h3 v-if="point.floors.length">Piętro:</h3>
            <ul>
                <li v-for="floor in point.floors">{{ floor }}</li>
            </ul>
        </template>
        <template v-else-if="loading">
            <h1>Ładowanie miejsca {{ routePointId }}...</h1>
        </template>
        <template v-else>
            <h1>Nie znaleziono miejsca {{ routePointId }}!</h1>
        </template>
    </section>
</template>

<style>

</style>
