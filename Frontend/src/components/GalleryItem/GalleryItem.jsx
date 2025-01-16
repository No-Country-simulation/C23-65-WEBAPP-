import { TransformWrapper, TransformComponent } from "react-zoom-pan-pinch";
import Modal from "@mui/material/Modal";
import { useState } from "react";

export const GalleryItem = () => {
  const [open, setOpen] = useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);
  return (
    <>
      <div className="w-full flex flex-col ">
        <div className="w-full flex justify-center">
          <img
            src="https://media.admagazine.com/photos/618a7dbc58ac69e38abb6c2c/16:9/w_1280,c_limit/43884.jpg"
            alt="noche"
            className=" w-4/5 object-contain"
            onClick={handleOpen}
          />
        </div>

        <h2 className="text-text-secondary text-xl font-semibold ml-14 my-4">
          La noche estrellada -1820
        </h2>
        <div className="flex flex-row justify-evenly mb-6 text-text-secondary ">
          <div className="w-2/5">
            <p>Autor: Vicent</p>
            <p>Medidas: 120cm x 120cm</p>
            <p>Medio: Oleaje sobre tela</p>
            <p>Estilo: Impresionismo</p>
            <p>Género: Paisajismo</p>
          </div>
          <div className="w-2/5">
            <p>
              It is a long established fact that a reader will be distracted by
              the readable content of a page when looking at its layout. The
              point of using Lorem Ipsum is that it has a more-or-less normal
              distribution of letters, as opposed to using Content here, cont
            </p>
          </div>
        </div>
      </div>
      <Modal
        open={open}
        onClose={handleClose}
        className="flex flex-col items-center justify-center gap-4"
      >
        <div className="bg-background-page p-6 rounded-lg shadow-md w-[60vw] h-auto flex flex-col border-none">
          <TransformWrapper>
            <TransformComponent>
              <img
                src="https://media.admagazine.com/photos/618a7dbc58ac69e38abb6c2c/16:9/w_1280,c_limit/43884.jpg"
                alt="noche"
                className="w-[60vw] object-contain"
                onClick={handleOpen}
              />
            </TransformComponent>
          </TransformWrapper>
        </div>
      </Modal>
    </>
  );
};
