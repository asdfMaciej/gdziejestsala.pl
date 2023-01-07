<script setup lang="ts">
import type { Path } from '@/api/models';
import { computed } from 'vue';
import { routeToDisplay } from '@/helpers/route-display-helper';
import { useDataStore } from '@/stores/data';
import { useRouteStore } from '@/stores/routes';

const props = defineProps<{
    startId: string,
    destinationId: string
}>();

const routeStore = useRouteStore();

let path = computed(() => {
    const route = routeStore.getRoute(props.startId, props.destinationId);
    if (!route)
        return [];
    return routeToDisplay(route, useDataStore());
});

</script>

<template>
    <article v-if="path">
        <template v-for="node in path">
            <div v-if="node.type === 'Point'">
                {{ node.point.name }} ({{ node.point.description }})
                <br>

                <RouterLink :to="{ name: 'view-point', params: { 'point_id': node.point.id } }">Point details
                </RouterLink>
            </div>
            <div v-else-if="node.type === 'Floor'">
                Piętro {{ node.floor.name }}

                <RouterLink :to="{ name: 'view-route-floor', params: { 'floor_id': node.floor.id } }">Floor details
                </RouterLink>
            </div>
        </template>
    </article>
</template>

<style scoped>

</style>
