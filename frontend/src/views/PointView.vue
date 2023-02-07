<script setup lang="ts">
import { useRoute } from 'vue-router';
import { useDataStore } from '../stores/data';
import { computed } from 'vue';
import { changeTitle } from '@/helpers/metatags';
import BackButton from '@/components/BackButton.vue';
import Gallery from '@/components/Gallery.vue';
import FloorMap from '@/components/FloorMap.vue';

const dataStore = useDataStore();

const route = useRoute();
const routePointId = computed(() => route.params.point_id);

const point = computed(() => dataStore.points.find(point => point.id === parseInt(route.params.point_id as string, 10)));

const floors = computed(() => dataStore.floors.filter(floor => point.value?.floors.some(pointFloor => pointFloor.floor_id === floor.id)));
const loading = computed(() => dataStore.points.length == 0);

changeTitle('Szczegóły miejsca');
</script>

<template>
    <section class="about">
        <template v-if="point">
            <h1>{{ point.name }}</h1>
            <p>{{ point.description }}</p>

            <Gallery :images="point.images"></Gallery>

            <h3 v-if="floors.length">Znajduje się na piętrach:</h3>
            <template v-if="floors.length">
                <template v-for="floor in floors">
                    <RouterLink :to="{
                        name: 'view-floor', params: {
                            'floor_id': floor.id
                        }
                    }">
                        <h3>{{ floor.name }}</h3>
                    </RouterLink>

                    <FloorMap :floor="floor" :points="[point]" :display-points-list="false">
                    </FloorMap>
                </template>
            </template>
        </template>
        <template v-else-if="loading">
            <h1>Ładowanie miejsca {{ routePointId }}...</h1>
        </template>
        <template v-else>
            <h1>Nie znaleziono miejsca {{ routePointId }}!</h1>
        </template>
    </section>
    <BackButton />
</template>

<style scoped>
section {
    flex: 1;
}
</style>
