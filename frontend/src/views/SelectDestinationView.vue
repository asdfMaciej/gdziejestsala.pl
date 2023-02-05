<script setup lang="ts">
import PointSelect from "../components/PointSelect.vue";
import router from '../router/index';
import { useRoute } from 'vue-router';
import { useDataStore } from '../stores/data';
import { computed } from "vue";

const dataStore = useDataStore();

const route = useRoute();
const startId = route.params.start_id;

const pointName = computed(() =>
    dataStore.points
        .filter(p => p.id == startId as unknown as number)
        .map(x => x.name)
        .find(() => true) || startId
);

const onSelectPoint = (pointId: number) => {
    router.push({
        name: 'view-route', params: { 'start_id': startId, 'destination_id': pointId }
    });
};


</script>

<template>
    <section class="about">
        <h1>Trasa z {{ pointName }}
            - wybierz punkt docelowy</h1>

        <PointSelect :floors="dataStore.floors" :points="dataStore.points" @selected="onSelectPoint" />
    </section>
</template>

<style>

</style>
