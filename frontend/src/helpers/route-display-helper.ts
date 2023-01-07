import type { Path, Point, Floor } from '@/api/models';

interface PathPoint {
    type: 'Point',
    point: Point
};

interface PathFloor {
    type: 'Floor',
    floor: Floor
}

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

const getRoutePointsOnFloor = (inputPath: Path) => {
    let result: { [floorId: number]: Point[] } = {};

    for (let point of inputPath) {
        for (let floor of point.floors) {
            if (!(floor.floor_id in result)) {
                result[floor.floor_id] = [];
            }

            result[floor.floor_id].push(point);
        }
    }

    return result;
};

export { routeToDisplay, getRoutePointsOnFloor };
export type { PathPoint, PathFloor };