import { defineStore } from 'pinia'
import api from '../api/api';
import type { Path } from '../api/models';

interface RouteStore {
    [id: string]: Path | null
};

export const useRouteStore = defineStore("routes", {
    state: () => ({
        routes: {} as RouteStore
    }),
    actions: {
        async getRoute(startId: number | string, destinationId: number | string): Promise<Path | null> {
            const id = startId + '|' + destinationId;
            if (id in this.routes)
                return this.routes[id];

            await this._fetchRoute(startId, destinationId);
            return this.routes[id];
        },

        async _fetchRoute(startId: number | string, destinationId: number | string) {
            const id = startId + '|' + destinationId;
            try {
                const response = await api.getRoute(startId, destinationId);
                this.routes[id] = response.path;
            }
            catch (error) {
                this.routes[id] = null;
                alert(error)
                console.log(error)
            }
        }
    }
})