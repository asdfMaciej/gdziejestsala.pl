import { defineStore } from 'pinia'
import api from '../api/api';
import type { Path } from '../api/models';

interface RouteStore {
    [id: string]: Path
};

export const useRouteStore = defineStore("routes", {
    state: () => ({
        routes: {} as RouteStore
    }),
    actions: {
        async fetchRoute(startId: number | string, destinationId: number | string) {
            try {
                const response = await api.getRoute(startId, destinationId);
                const id = startId + '|' + destinationId;
                this.routes[id] = response.path;
            }
            catch (error) {
                alert(error)
                console.log(error)
            }
        }
    },
    getters: {
        getRoute: (state) => {
            return (startId: number | string, destinationId: number | string) => state.routes[startId + '|' + destinationId];
        }
    }
})