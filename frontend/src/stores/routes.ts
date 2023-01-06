import { defineStore } from 'pinia'
import api from '../api/api';

export const useRouteStore = defineStore("routes", {
    state: () => ({
        routes: {}
    }),
    actions: {
        async fetchRoute(startId, destinationId) {
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
            return (startId, destinationId) => state.routes[startId + '|' + destinationId];
        }
    }
})