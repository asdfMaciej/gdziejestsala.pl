<script setup lang="ts">
import QRCodeScanner from '@/components/QRCodeScanner.vue';
import router from '@/router/index';
import { useToast } from 'vue-toast-notification';

const onMatch = (pointId: string | number) => {
    useToast().success('Odczytano punkt początkowy!', {
        position: 'bottom'
    });
    router.push({
        name: 'select-destination', params: { 'start_id': pointId }
    });
};
</script>

<template>
    <section>
        <h2>Zeskanuj nabliższy kod QR</h2>

        <QRCodeScanner @match="onMatch"></QRCodeScanner>

        <RouterLink class="alternative" :to="{ name: 'select-start', params: {} }">...lub wybierz punkt początkowy z
            listy
        </RouterLink>
    </section>
</template>

<style scoped>
.alternative {
    display: block;
    margin-top: 20px;
}
</style>