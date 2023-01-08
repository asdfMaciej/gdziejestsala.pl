<script setup lang="ts">
import type { Path } from '@/api/models';
import { computed } from 'vue';
import { routeToDisplay } from '@/helpers/route-display-helper';
import { useDataStore } from '@/stores/data';

const props = defineProps<{
    route: Path | null,
    startId: number | string,
    destinationId: number | string
}>();

let path = computed(() => routeToDisplay(props.route, useDataStore()));
</script>

<template>
    <article v-if="path.length">
        <template v-for="node in path">
            <div v-if="node.type === 'Point'">
                {{ node.point.name }} ({{ node.point.description }})
                <br>

                <RouterLink :to="{ name: 'view-point', params: { 'point_id': node.point.id } }">Point details
                </RouterLink>
            </div>
            <div v-else-if="node.type === 'Floor'">
                Piętro {{ node.floor.name }}

                startid {{ startId }} {{ destinationId }}

                <RouterLink :to="{ name: 'view-route-floor', params: { 
                    'floor_id': node.floor.id, 'start_id': startId, 'destination_id': destinationId } }">Floor details
                </RouterLink>
            </div>
        </template>
    </article>
</template>

<style scoped>

</style>
