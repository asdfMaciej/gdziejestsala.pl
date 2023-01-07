import axios from "axios"
import type { Point, FloorPoint, Floor, Image, Path } from "./models";

const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;
interface PointsResponse {
    points: Point[],
    floors: Floor[]
}

interface PathResponse {
    path: Path
}

class API {
    async getPoints(): Promise<PointsResponse> {
        const data = await axios.get(`${BACKEND_URL}/api/v1/points`);
        return { points: data.data.points, floors: data.data.floors };
    }

    async getRoute(startId: number | string, destinationId: number | string): Promise<PathResponse> {
        const data = await axios.get(`${BACKEND_URL}/api/v1/route/${startId}/${destinationId}`);
        return { path: data.data.path };  // ignoring floors
    }
}

export default new API();
