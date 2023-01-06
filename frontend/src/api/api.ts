import axios from "axios"

const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;

class API {
    async getPoints() {
        const data = await axios.get(`${BACKEND_URL}/api/v1/points`);
        return { points: data.data.points, floors: data.data.floors };
    }

    async getRoute(startId, destinationId) {
        const data = await axios.get(`${BACKEND_URL}/api/v1/route/${startId}/${destinationId}`);
        return { path: data.data.path, floors: data.data.floors };
    }
}

export default new API();
