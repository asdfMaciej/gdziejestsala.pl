import { defineStore } from 'pinia'
// Import axios to make HTTP requests
import axios from "axios"

const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;

export const usePointsStore = defineStore("user", {
    state: () => ({
        points: {},
    }),
    actions: {
        async fetchPoints() {
            try {
                const data = await axios.get(`${BACKEND_URL}/api/v1/points`);
                this.points = {};
                for (let point of data.data.points) {
                    this.points[point.id] = point;
                }
                console.log(JSON.stringify(this.points));
            }
            catch (error) {
                alert(error)
                console.log(error)
            }
        }
    },
})