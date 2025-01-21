import { useControls } from "react-zoom-pan-pinch";
import { MdOutlineZoomOut, MdZoomIn } from "react-icons/md";
import { TbZoomReset } from "react-icons/tb";

export const ControlsZoom = () => {
  const { zoomIn, zoomOut, resetTransform } = useControls();

  return (
    <div className="absolute right-[3%] top-[3%] ">
      <button className="bg-transparent" onClick={() => zoomIn()}>
        <MdZoomIn size={40} />
      </button>
      <button className="bg-transparent" onClick={() => zoomOut()}>
        <MdOutlineZoomOut size={40} />
      </button>
      <button className="bg-transparent" onClick={() => resetTransform()}>
        <TbZoomReset size={38} />
      </button>
    </div>
  );
};
