Name:           ros-jade-rqt-multiplot
Version:        0.0.7
Release:        1%{?dist}
Summary:        ROS rqt_multiplot package

Group:          Development/Libraries
License:        GNU Lesser General Public License (LGPL)
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-jade-rosbag
Requires:       ros-jade-roscpp
Requires:       ros-jade-rqt-gui
Requires:       ros-jade-rqt-gui-cpp
Requires:       ros-jade-variant-topic-tools
BuildRequires:  qwt-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-rosbag
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-rqt-gui
BuildRequires:  ros-jade-rqt-gui-cpp
BuildRequires:  ros-jade-variant-topic-tools

%description
rqt_multiplot provides a GUI plugin for visualizing numeric values in multiple
2D plots using the Qwt plotting backend.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Mon May 08 2017 Ralf Kaestner <ralf.kaestner@gmail.com> - 0.0.7-1
- Autogenerated by Bloom

* Mon May 08 2017 Ralf Kaestner <ralf.kaestner@gmail.com> - 0.0.7-0
- Autogenerated by Bloom

* Wed Dec 28 2016 Ralf Kaestner <ralf.kaestner@gmail.com> - 0.0.6-0
- Autogenerated by Bloom

* Mon Aug 08 2016 Ralf Kaestner <ralf.kaestner@gmail.com> - 0.0.5-1
- Autogenerated by Bloom

* Fri Aug 05 2016 Ralf Kaestner <ralf.kaestner@gmail.com> - 0.0.5-0
- Autogenerated by Bloom

