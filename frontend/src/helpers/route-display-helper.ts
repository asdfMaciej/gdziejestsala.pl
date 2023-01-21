import type { Path, Point, Floor, FloorPoint } from '@/api/models';

interface PathPoint {
    type: 'Point',
    point: Point
};

interface PathFloor {
    type: 'Floor',
    floor: Floor
}

interface FloorPointDetails {
    floorPoint: FloorPoint,
    point: Point
};

const routeToDisplay = (inputPath: Path | null, dataStore: any) => {
    if (inputPath == null)
        return [];

    let path: Array<PathPoint | PathFloor> = [];
    let currentFloorId: number | null = null;

    for (let point of inputPath) {
        // Display a header once you switch the floor
        //   - for ex. going from stairs to a hallway / classroom,
        //     but not when entering stairs / elevator
        if (point.floors.length === 1 && point.floors[0].floor_id != currentFloorId) {
            currentFloorId = point.floors[0].floor_id;
            // @ts-ignore
            const floor = dataStore.floors.find(floor => floor.id === currentFloorId) as Floor;
            path.push({
                type: 'Floor',
                floor: floor
            });
        }

        path.push({
            type: 'Point',
            point: point
        })
    }

    return path;
};

/**
 * Lists <point, floorPoint> for each path point on a given floor.
 * 
 * FloorPoint stores point coordinates for a floor, Point stores its details.
 * Uses a helper output type FloorPointDetails. 
 * @param inputPath Path 
 * @param floorId Floor ID
 */
const getRoutePointsOnFloor = (inputPath: Path, floorId: number): FloorPointDetails[] => {
    let result: FloorPointDetails[] = [];

    if (!inputPath)
        return result;

    for (let point of inputPath) {
        for (let floorPoint of point.floors) {
            if (floorPoint.floor_id != floorId)
                continue;

            result.push({
                floorPoint: floorPoint,
                point: point
            });
        }
    }

    return result;
};

export { routeToDisplay, getRoutePointsOnFloor };
export type { PathPoint, PathFloor, FloorPointDetails };