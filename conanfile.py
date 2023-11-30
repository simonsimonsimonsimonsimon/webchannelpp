from conan import ConanFile
from conan.tools.files import copy
import os

class WebchannelppRecipe(ConanFile):
    name    = "webchannelpp"
    user    =  "menlosystems" # to have some sort of namespace or scope
    version = "0.1"
    # channel = ? of (stable|testing)
    # Metadata
    description = "WebChannel++ is an implementation of Qt's WebChannel protocol in C++14."
    license     = "GPLv2+ and LGPLv3"
    author      = "Arno Rehn (a.rehn@menlosystems.com)"
    # topics = ?
    # homepage = ?
    url         = "https://github.com/MenloSystems/webchannelpp.git"

    exports_sources = "include/*", "*"
    no_copy_source = True

    def package(self):
        # This will also copy the "include" folder
        copy(self, "LICENSE.*", src=self.source_folder, dst=os.path.join(self.package_folder, "licenses"))
        # prune the "/menlosystems"-part if no scoped packages are desired
        copy(self, pattern="*.h", src=os.path.join(self.source_folder, "include"), dst=os.path.join(self.package_folder, "include/menlosystems"))
        copy(self, pattern="*.hpp", src=os.path.join(self.source_folder, "include"), dst=os.path.join(self.package_folder, "include/menlosystems"))

    def package_info(self):
        self.cpp_info.bindirs = []
        self.cpp_info.libdirs = []
