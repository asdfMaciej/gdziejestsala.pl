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
    <dl v-if="path.length" class="route-details">
        <template v-for="node in path">
            <dt v-if="node.type === 'Point'">
                <RouterLink :to="{ name: 'view-point', params: { 'point_id': node.point.id } }">{{ node.point.name }}
                </RouterLink>
            </dt>
            <dd v-else-if="node.type === 'Floor'">


                <RouterLink :to="{
                    name: 'view-route-floor', params: {
                        'floor_id': node.floor.id, 'start_id': startId, 'destination_id': destinationId
                    }
                }">
                    <h3>🏢 {{ node.floor.name }}</h3>
                </RouterLink>
            </dd>
        </template>
    </dl>
</template>

<style scoped lang="scss">
.route-details {
    a {
        color: var(--hex-black);
    }
}

dt {
    margin: 10px 0;
}

dd {
    margin: 15px 0 10px;
}

dd:first-child {
    margin-top: 0;
}

dt:last-child {
    margin-bottom: 0;
}
</style>
