import { defineStore } from 'pinia'
// Import axios to make HTTP requests
import axios from "axios"

const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;

export const useDataStore = defineStore("user", {
    state: () => ({
        points: [],
        floors: []
    }),
    actions: {
        async fetchData() {
            try {
                const data = await axios.get(`${BACKEND_URL}/api/v1/points`);
                this.points = data.data.points;
                this.floors = data.data.floors;
            }
            catch (error) {
                alert(error)
                console.log(error)
            }
        }
    },
})