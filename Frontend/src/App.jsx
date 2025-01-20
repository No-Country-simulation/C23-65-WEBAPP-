import { BrowserRouter, Route, Routes } from "react-router";
import { Home } from "./pages/home/home";
import { Hall } from "./pages/hall/Hall";
import { InternationalGalleryHub } from "./pages/InternationalGalleryHub/InternationalGalleryHub";
import { Gallery } from "./pages/Gallery/Gallery";
import { Profile } from "./pages/profile/profile";

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
          <Route path="/profile" element={<Profile />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
