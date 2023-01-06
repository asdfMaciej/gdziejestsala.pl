import { defineStore } from 'pinia'
import api from '../api/api';

export const useDataStore = defineStore("user", {
    state: () => ({
        points: [],
        floors: []
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