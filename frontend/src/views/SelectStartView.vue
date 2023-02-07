<script setup lang="ts">
import { useToast } from "vue-toast-notification";
import PointSelect from "../components/PointSelect.vue";
import router from '../router/index';
import { useDataStore } from '../stores/data';

const dataStore = useDataStore();

const onSelectPoint = (pointId: number) => {
    useToast().info('Wybrano punkt początkowy.', {
        position: 'bottom'
    });

    router.push({
        name: 'select-destination', params: { 'start_id': pointId }
    });
};

</script>
<template>
    <section class="about">
        <h1>Wybierz punkt początkowy</h1>

        <PointSelect :floors="dataStore.floors" :points="dataStore.points" @selected="onSelectPoint" />

        <RouterLink class="alternative" :to="{ name: 'scan-qr', params: {} }">...lub zeskanuj najbliższy kod QR
        </RouterLink>
    </section>
</template>

<style scoped>
.alternative {
    display: block;
    margin-top: 20px;
}
</style>
