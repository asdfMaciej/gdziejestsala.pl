interface Point {
    name: string,
    description: string,
    is_classroom: boolean,
    id: number,
    floors: FloorPoint[]
};

interface FloorPoint {
    x: number,
    y: number,
    floor_id: number
};

interface Floor {
    name: string,
    id: number,
    description: string,
    map_image: Image,
};

interface Image {
    url: string,
    width: number,
    height: number,
    id: number
};

type Path = Point[];


export type { Point, FloorPoint, Floor, Image, Path };
