<script setup lang="ts">
import PointSelect from "../components/PointSelect.vue";
import router from '../router/index';
import { useRoute } from 'vue-router';
import { useDataStore } from '../stores/data';

const dataStore = useDataStore();

const route = useRoute();
const startId = route.params.start_id;

const onSelectPoint = (pointId) => {
    router.push({
        name: 'view-route', params: { 'start_id': startId, 'destination_id': pointId }
    });
};


</script>

<template>
    <div class="about">
        <h1>route from {{ startId }} - select destination view</h1>

        <PointSelect :floors="dataStore.floors" :points="dataStore.points" @selected="onSelectPoint" />
    </div>
</template>
  
<style>

</style>
  