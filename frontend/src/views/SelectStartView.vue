<script setup lang="ts">
import PointSelect from "../components/PointSelect.vue";
import router from '../router/index';
import { useDataStore } from '../stores/data';

const dataStore = useDataStore();

const onSelectPoint = (pointId: number) => {
    router.push({
        name: 'select-destination', params: { 'start_id': pointId }
    });
};

</script>
<template>
    <div class="about">
        <h1>select start view</h1>

        <PointSelect :floors="dataStore.floors" :points="dataStore.points" @selected="onSelectPoint" />

        <RouterLink :to="{ name: 'scan-qr', params: {} }">Lub zeskanuj najbliższy kod QR</RouterLink>
    </div>
</template>

<style>

</style>
