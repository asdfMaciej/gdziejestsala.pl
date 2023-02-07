<script setup lang="ts">
import PointSelect from "../components/PointSelect.vue";
import BackButton from "@/components/BackButton.vue";
import router from '../router/index';
import { useRoute } from 'vue-router';
import { useToast } from 'vue-toast-notification';
import { useDataStore } from '../stores/data';
import { changeTitle } from '@/helpers/metatags';
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
    useToast().info('Wybrano punkt końcowy.', {
        position: 'bottom'
    });

    router.push({
        name: 'view-route', params: { 'start_id': startId, 'destination_id': pointId }
    });
};

changeTitle('Wybierz miejsce docelowe');
</script>

<template>
    <section class="about">
        <h1>Trasa z {{ pointName }}
            - wybierz punkt docelowy</h1>

        <PointSelect :floors="dataStore.floors" :points="dataStore.points" @selected="onSelectPoint" />
    </section>
    <BackButton />
</template>

<style scoped>
section {
    flex: 1;
}
</style>
