import { BrowserRouter, Route, Routes } from "react-router";
import { Home } from "./pages/home/home";
import { Hall } from "./pages/hall/Hall";
import { InternationalGalleryHub } from "./pages/InternationalGalleryHub/InternationalGalleryHub";
import { Gallery } from "./pages/Gallery/Gallery";

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route index element={<Home />} />
          <Route index path="/login" element={<Home />} />
          <Route path="/hall" element={<Hall />} />
          {/* <Route path="/hall" element={<Hall />} /> */}
          <Route path="/int-galleries" element={<InternationalGalleryHub />} />
          <Route path="/national-gallery" element={<Gallery />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
