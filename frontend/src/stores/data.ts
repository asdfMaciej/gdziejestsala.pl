import { defineStore } from 'pinia'
import api from '../api/api';
import type { Point, Floor } from '../api/models';

export const useDataStore = defineStore("user", {
    state: () => ({
        points: [] as Point[],
        floors: [] as Floor[]
    }),
    actions: {
        async fetchData() {
            try {
                const response = await api.getPoints();
                this.points = response.points;
                this.floors = response.floors;
            }
            catch (error) {
                alert(error)
                console.log(error)
            }
        }
    },
})