# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2013, Numenta, Inc.  Unless you have an agreement
# with Numenta, Inc., for a separate license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------
import csv
from nupic.frameworks.opf.modelfactory import ModelFactory
from nupic_output import NuPICFileOutput, NuPICPlotOutput
from nupic.swarming import permutations_runner
import pickle

# Change this to switch from a matplotlib plot to file output.
PLOT = False
SWARM_DEF = "search_def.json"
SWARM_CONFIG = {
  "includedFields": [
    {
      "fieldName": "sequence",
      "fieldType": "int"
    },
    {
      "fieldName": "time",
      "fieldType": "datetime"
    },
    {
      "fieldName": "move_x",
      "fieldType": "float"
    },
    {
      "fieldName": "move_y",
      "fieldType": "float"
    },
    {
      "fieldName": "look_x",
      "fieldType": "float"
    },
    {
      "fieldName": "look_y",
      "fieldType": "float"
    }
    ,{"fieldName": "f0", "fieldType": "float"}
    ,{"fieldName": "f1", "fieldType": "float"}
    ,{"fieldName": "f2", "fieldType": "float"}
    ,{"fieldName": "f3", "fieldType": "float"}
    ,{"fieldName": "f4", "fieldType": "float"}
    ,{"fieldName": "f5", "fieldType": "float"}
    ,{"fieldName": "f6", "fieldType": "float"}
    ,{"fieldName": "f7", "fieldType": "float"}
    ,{"fieldName": "f8", "fieldType": "float"}
    ,{"fieldName": "f9", "fieldType": "float"}
    ,{"fieldName": "f10", "fieldType": "float"}
    ,{"fieldName": "f11", "fieldType": "float"}
    ,{"fieldName": "f12", "fieldType": "float"}
    ,{"fieldName": "f13", "fieldType": "float"}
    ,{"fieldName": "f14", "fieldType": "float"}
    ,{"fieldName": "f15", "fieldType": "float"}
    ,{"fieldName": "f16", "fieldType": "float"}
    ,{"fieldName": "f17", "fieldType": "float"}
    ,{"fieldName": "f18", "fieldType": "float"}
    ,{"fieldName": "f19", "fieldType": "float"}
    ,{"fieldName": "f20", "fieldType": "float"}
    ,{"fieldName": "f21", "fieldType": "float"}
    ,{"fieldName": "f22", "fieldType": "float"}
    ,{"fieldName": "f23", "fieldType": "float"}
    ,{"fieldName": "f24", "fieldType": "float"}
    ,{"fieldName": "f25", "fieldType": "float"}
    ,{"fieldName": "f26", "fieldType": "float"}
    ,{"fieldName": "f27", "fieldType": "float"}
    ,{"fieldName": "f28", "fieldType": "float"}
    ,{"fieldName": "f29", "fieldType": "float"}
    ,{"fieldName": "f30", "fieldType": "float"}
    ,{"fieldName": "f31", "fieldType": "float"}
    ,{"fieldName": "f32", "fieldType": "float"}
    ,{"fieldName": "f33", "fieldType": "float"}
    ,{"fieldName": "f34", "fieldType": "float"}
    ,{"fieldName": "f35", "fieldType": "float"}
    ,{"fieldName": "f36", "fieldType": "float"}
    ,{"fieldName": "f37", "fieldType": "float"}
    ,{"fieldName": "f38", "fieldType": "float"}
    ,{"fieldName": "f39", "fieldType": "float"}
    ,{"fieldName": "f40", "fieldType": "float"}
    ,{"fieldName": "f41", "fieldType": "float"}
    ,{"fieldName": "f42", "fieldType": "float"}
    ,{"fieldName": "f43", "fieldType": "float"}
    ,{"fieldName": "f44", "fieldType": "float"}
    ,{"fieldName": "f45", "fieldType": "float"}
    ,{"fieldName": "f46", "fieldType": "float"}
    ,{"fieldName": "f47", "fieldType": "float"}
    ,{"fieldName": "f48", "fieldType": "float"}
    ,{"fieldName": "f49", "fieldType": "float"}
    ,{"fieldName": "f50", "fieldType": "float"}
    ,{"fieldName": "f51", "fieldType": "float"}
    ,{"fieldName": "f52", "fieldType": "float"}
    ,{"fieldName": "f53", "fieldType": "float"}
    ,{"fieldName": "f54", "fieldType": "float"}
    ,{"fieldName": "f55", "fieldType": "float"}
    ,{"fieldName": "f56", "fieldType": "float"}
    ,{"fieldName": "f57", "fieldType": "float"}
    ,{"fieldName": "f58", "fieldType": "float"}
    ,{"fieldName": "f59", "fieldType": "float"}
    ,{"fieldName": "f60", "fieldType": "float"}
    ,{"fieldName": "f61", "fieldType": "float"}
    ,{"fieldName": "f62", "fieldType": "float"}
    ,{"fieldName": "f63", "fieldType": "float"}
    ,{"fieldName": "f64", "fieldType": "float"}
    ,{"fieldName": "f65", "fieldType": "float"}
    ,{"fieldName": "f66", "fieldType": "float"}
    ,{"fieldName": "f67", "fieldType": "float"}
    ,{"fieldName": "f68", "fieldType": "float"}
    ,{"fieldName": "f69", "fieldType": "float"}
    ,{"fieldName": "f70", "fieldType": "float"}
    ,{"fieldName": "f71", "fieldType": "float"}
    ,{"fieldName": "f72", "fieldType": "float"}
    ,{"fieldName": "f73", "fieldType": "float"}
    ,{"fieldName": "f74", "fieldType": "float"}
    ,{"fieldName": "f75", "fieldType": "float"}
    ,{"fieldName": "f76", "fieldType": "float"}
    ,{"fieldName": "f77", "fieldType": "float"}
    ,{"fieldName": "f78", "fieldType": "float"}
    ,{"fieldName": "f79", "fieldType": "float"}
    ,{"fieldName": "f80", "fieldType": "float"}
    ,{"fieldName": "f81", "fieldType": "float"}
    ,{"fieldName": "f82", "fieldType": "float"}
    ,{"fieldName": "f83", "fieldType": "float"}
    ,{"fieldName": "f84", "fieldType": "float"}
    ,{"fieldName": "f85", "fieldType": "float"}
    ,{"fieldName": "f86", "fieldType": "float"}
    ,{"fieldName": "f87", "fieldType": "float"}
    ,{"fieldName": "f88", "fieldType": "float"}
    ,{"fieldName": "f89", "fieldType": "float"}
    ,{"fieldName": "f90", "fieldType": "float"}
    ,{"fieldName": "f91", "fieldType": "float"}
    ,{"fieldName": "f92", "fieldType": "float"}
    ,{"fieldName": "f93", "fieldType": "float"}
    ,{"fieldName": "f94", "fieldType": "float"}
    ,{"fieldName": "f95", "fieldType": "float"}
    ,{"fieldName": "f96", "fieldType": "float"}
    ,{"fieldName": "f97", "fieldType": "float"}
    ,{"fieldName": "f98", "fieldType": "float"}
    ,{"fieldName": "f99", "fieldType": "float"}
    ,{"fieldName": "f100", "fieldType": "float"}
    ,{"fieldName": "f101", "fieldType": "float"}
    ,{"fieldName": "f102", "fieldType": "float"}
    ,{"fieldName": "f103", "fieldType": "float"}
    ,{"fieldName": "f104", "fieldType": "float"}
    ,{"fieldName": "f105", "fieldType": "float"}
    ,{"fieldName": "f106", "fieldType": "float"}
    ,{"fieldName": "f107", "fieldType": "float"}
    ,{"fieldName": "f108", "fieldType": "float"}
    ,{"fieldName": "f109", "fieldType": "float"}
    ,{"fieldName": "f110", "fieldType": "float"}
    ,{"fieldName": "f111", "fieldType": "float"}
    ,{"fieldName": "f112", "fieldType": "float"}
    ,{"fieldName": "f113", "fieldType": "float"}
    ,{"fieldName": "f114", "fieldType": "float"}
    ,{"fieldName": "f115", "fieldType": "float"}
    ,{"fieldName": "f116", "fieldType": "float"}
    ,{"fieldName": "f117", "fieldType": "float"}
    ,{"fieldName": "f118", "fieldType": "float"}
    ,{"fieldName": "f119", "fieldType": "float"}
    ,{"fieldName": "f120", "fieldType": "float"}
    ,{"fieldName": "f121", "fieldType": "float"}
    ,{"fieldName": "f122", "fieldType": "float"}
    ,{"fieldName": "f123", "fieldType": "float"}
    ,{"fieldName": "f124", "fieldType": "float"}
    ,{"fieldName": "f125", "fieldType": "float"}
    ,{"fieldName": "f126", "fieldType": "float"}
    ,{"fieldName": "f127", "fieldType": "float"}
    ,{"fieldName": "f128", "fieldType": "float"}
    ,{"fieldName": "f129", "fieldType": "float"}
    ,{"fieldName": "f130", "fieldType": "float"}
    ,{"fieldName": "f131", "fieldType": "float"}
    ,{"fieldName": "f132", "fieldType": "float"}
    ,{"fieldName": "f133", "fieldType": "float"}
    ,{"fieldName": "f134", "fieldType": "float"}
    ,{"fieldName": "f135", "fieldType": "float"}
    ,{"fieldName": "f136", "fieldType": "float"}
    ,{"fieldName": "f137", "fieldType": "float"}
    ,{"fieldName": "f138", "fieldType": "float"}
    ,{"fieldName": "f139", "fieldType": "float"}
    ,{"fieldName": "f140", "fieldType": "float"}
    ,{"fieldName": "f141", "fieldType": "float"}
    ,{"fieldName": "f142", "fieldType": "float"}
    ,{"fieldName": "f143", "fieldType": "float"}
    ,{"fieldName": "f144", "fieldType": "float"}
    ,{"fieldName": "f145", "fieldType": "float"}
    ,{"fieldName": "f146", "fieldType": "float"}
    ,{"fieldName": "f147", "fieldType": "float"}
    ,{"fieldName": "f148", "fieldType": "float"}
    ,{"fieldName": "f149", "fieldType": "float"}
    ,{"fieldName": "f150", "fieldType": "float"}
    ,{"fieldName": "f151", "fieldType": "float"}
    ,{"fieldName": "f152", "fieldType": "float"}
    ,{"fieldName": "f153", "fieldType": "float"}
    ,{"fieldName": "f154", "fieldType": "float"}
    ,{"fieldName": "f155", "fieldType": "float"}
    ,{"fieldName": "f156", "fieldType": "float"}
    ,{"fieldName": "f157", "fieldType": "float"}
    ,{"fieldName": "f158", "fieldType": "float"}
    ,{"fieldName": "f159", "fieldType": "float"}
    ,{"fieldName": "f160", "fieldType": "float"}
    ,{"fieldName": "f161", "fieldType": "float"}
    ,{"fieldName": "f162", "fieldType": "float"}
    ,{"fieldName": "f163", "fieldType": "float"}
    ,{"fieldName": "f164", "fieldType": "float"}
    ,{"fieldName": "f165", "fieldType": "float"}
    ,{"fieldName": "f166", "fieldType": "float"}
    ,{"fieldName": "f167", "fieldType": "float"}
    ,{"fieldName": "f168", "fieldType": "float"}
    ,{"fieldName": "f169", "fieldType": "float"}
    ,{"fieldName": "f170", "fieldType": "float"}
    ,{"fieldName": "f171", "fieldType": "float"}
    ,{"fieldName": "f172", "fieldType": "float"}
    ,{"fieldName": "f173", "fieldType": "float"}
    ,{"fieldName": "f174", "fieldType": "float"}
    ,{"fieldName": "f175", "fieldType": "float"}
    ,{"fieldName": "f176", "fieldType": "float"}
    ,{"fieldName": "f177", "fieldType": "float"}
    ,{"fieldName": "f178", "fieldType": "float"}
    ,{"fieldName": "f179", "fieldType": "float"}
    ,{"fieldName": "f180", "fieldType": "float"}
    ,{"fieldName": "f181", "fieldType": "float"}
    ,{"fieldName": "f182", "fieldType": "float"}
    ,{"fieldName": "f183", "fieldType": "float"}
    ,{"fieldName": "f184", "fieldType": "float"}
    ,{"fieldName": "f185", "fieldType": "float"}
    ,{"fieldName": "f186", "fieldType": "float"}
    ,{"fieldName": "f187", "fieldType": "float"}
    ,{"fieldName": "f188", "fieldType": "float"}
    ,{"fieldName": "f189", "fieldType": "float"}
    ,{"fieldName": "f190", "fieldType": "float"}
    ,{"fieldName": "f191", "fieldType": "float"}
    ,{"fieldName": "f192", "fieldType": "float"}
    ,{"fieldName": "f193", "fieldType": "float"}
    ,{"fieldName": "f194", "fieldType": "float"}
    ,{"fieldName": "f195", "fieldType": "float"}
    ,{"fieldName": "f196", "fieldType": "float"}
    ,{"fieldName": "f197", "fieldType": "float"}
    ,{"fieldName": "f198", "fieldType": "float"}
    ,{"fieldName": "f199", "fieldType": "float"}
    ,{"fieldName": "f200", "fieldType": "float"}
    ,{"fieldName": "f201", "fieldType": "float"}
    ,{"fieldName": "f202", "fieldType": "float"}
    ,{"fieldName": "f203", "fieldType": "float"}
    ,{"fieldName": "f204", "fieldType": "float"}
    ,{"fieldName": "f205", "fieldType": "float"}
    ,{"fieldName": "f206", "fieldType": "float"}
    ,{"fieldName": "f207", "fieldType": "float"}
    ,{"fieldName": "f208", "fieldType": "float"}
    ,{"fieldName": "f209", "fieldType": "float"}
    ,{"fieldName": "f210", "fieldType": "float"}
    ,{"fieldName": "f211", "fieldType": "float"}
    ,{"fieldName": "f212", "fieldType": "float"}
    ,{"fieldName": "f213", "fieldType": "float"}
    ,{"fieldName": "f214", "fieldType": "float"}
    ,{"fieldName": "f215", "fieldType": "float"}
    ,{"fieldName": "f216", "fieldType": "float"}
    ,{"fieldName": "f217", "fieldType": "float"}
    ,{"fieldName": "f218", "fieldType": "float"}
    ,{"fieldName": "f219", "fieldType": "float"}
    ,{"fieldName": "f220", "fieldType": "float"}
    ,{"fieldName": "f221", "fieldType": "float"}
    ,{"fieldName": "f222", "fieldType": "float"}
    ,{"fieldName": "f223", "fieldType": "float"}
    ,{"fieldName": "f224", "fieldType": "float"}
    ,{"fieldName": "f225", "fieldType": "float"}
    ,{"fieldName": "f226", "fieldType": "float"}
    ,{"fieldName": "f227", "fieldType": "float"}
    ,{"fieldName": "f228", "fieldType": "float"}
    ,{"fieldName": "f229", "fieldType": "float"}
    ,{"fieldName": "f230", "fieldType": "float"}
    ,{"fieldName": "f231", "fieldType": "float"}
    ,{"fieldName": "f232", "fieldType": "float"}
    ,{"fieldName": "f233", "fieldType": "float"}
    ,{"fieldName": "f234", "fieldType": "float"}
    ,{"fieldName": "f235", "fieldType": "float"}
    ,{"fieldName": "f236", "fieldType": "float"}
    ,{"fieldName": "f237", "fieldType": "float"}
    ,{"fieldName": "f238", "fieldType": "float"}
    ,{"fieldName": "f239", "fieldType": "float"}
    ,{"fieldName": "f240", "fieldType": "float"}
    ,{"fieldName": "f241", "fieldType": "float"}
    ,{"fieldName": "f242", "fieldType": "float"}
    ,{"fieldName": "f243", "fieldType": "float"}
    ,{"fieldName": "f244", "fieldType": "float"}
    ,{"fieldName": "f245", "fieldType": "float"}
    ,{"fieldName": "f246", "fieldType": "float"}
    ,{"fieldName": "f247", "fieldType": "float"}
    ,{"fieldName": "f248", "fieldType": "float"}
    ,{"fieldName": "f249", "fieldType": "float"}
    ,{"fieldName": "f250", "fieldType": "float"}
    ,{"fieldName": "f251", "fieldType": "float"}
    ,{"fieldName": "f252", "fieldType": "float"}
    ,{"fieldName": "f253", "fieldType": "float"}
    ,{"fieldName": "f254", "fieldType": "float"}
    ,{"fieldName": "f255", "fieldType": "float"}
    ,{"fieldName": "f256", "fieldType": "float"}
    ,{"fieldName": "f257", "fieldType": "float"}
    ,{"fieldName": "f258", "fieldType": "float"}
    ,{"fieldName": "f259", "fieldType": "float"}
    ,{"fieldName": "f260", "fieldType": "float"}
    ,{"fieldName": "f261", "fieldType": "float"}
    ,{"fieldName": "f262", "fieldType": "float"}
    ,{"fieldName": "f263", "fieldType": "float"}
    ,{"fieldName": "f264", "fieldType": "float"}
    ,{"fieldName": "f265", "fieldType": "float"}
    ,{"fieldName": "f266", "fieldType": "float"}
    ,{"fieldName": "f267", "fieldType": "float"}
    ,{"fieldName": "f268", "fieldType": "float"}
    ,{"fieldName": "f269", "fieldType": "float"}
    ,{"fieldName": "f270", "fieldType": "float"}
    ,{"fieldName": "f271", "fieldType": "float"}
    ,{"fieldName": "f272", "fieldType": "float"}
    ,{"fieldName": "f273", "fieldType": "float"}
    ,{"fieldName": "f274", "fieldType": "float"}
    ,{"fieldName": "f275", "fieldType": "float"}
    ,{"fieldName": "f276", "fieldType": "float"}
    ,{"fieldName": "f277", "fieldType": "float"}
    ,{"fieldName": "f278", "fieldType": "float"}
    ,{"fieldName": "f279", "fieldType": "float"}
    ,{"fieldName": "f280", "fieldType": "float"}
    ,{"fieldName": "f281", "fieldType": "float"}
    ,{"fieldName": "f282", "fieldType": "float"}
    ,{"fieldName": "f283", "fieldType": "float"}
    ,{"fieldName": "f284", "fieldType": "float"}
    ,{"fieldName": "f285", "fieldType": "float"}
    ,{"fieldName": "f286", "fieldType": "float"}
    ,{"fieldName": "f287", "fieldType": "float"}
    ,{"fieldName": "f288", "fieldType": "float"}
    ,{"fieldName": "f289", "fieldType": "float"}
    ,{"fieldName": "f290", "fieldType": "float"}
    ,{"fieldName": "f291", "fieldType": "float"}
    ,{"fieldName": "f292", "fieldType": "float"}
    ,{"fieldName": "f293", "fieldType": "float"}
    ,{"fieldName": "f294", "fieldType": "float"}
    ,{"fieldName": "f295", "fieldType": "float"}
    ,{"fieldName": "f296", "fieldType": "float"}
    ,{"fieldName": "f297", "fieldType": "float"}
    ,{"fieldName": "f298", "fieldType": "float"}
    ,{"fieldName": "f299", "fieldType": "float"}
    ,{"fieldName": "f300", "fieldType": "float"}
    ,{"fieldName": "f301", "fieldType": "float"}
    ,{"fieldName": "f302", "fieldType": "float"}
    ,{"fieldName": "f303", "fieldType": "float"}
    ,{"fieldName": "f304", "fieldType": "float"}
    ,{"fieldName": "f305", "fieldType": "float"}
    ,{"fieldName": "f306", "fieldType": "float"}
    ,{"fieldName": "f307", "fieldType": "float"}
    ,{"fieldName": "f308", "fieldType": "float"}
    ,{"fieldName": "f309", "fieldType": "float"}
    ,{"fieldName": "f310", "fieldType": "float"}
    ,{"fieldName": "f311", "fieldType": "float"}
    ,{"fieldName": "f312", "fieldType": "float"}
    ,{"fieldName": "f313", "fieldType": "float"}
    ,{"fieldName": "f314", "fieldType": "float"}
    ,{"fieldName": "f315", "fieldType": "float"}
    ,{"fieldName": "f316", "fieldType": "float"}
    ,{"fieldName": "f317", "fieldType": "float"}
    ,{"fieldName": "f318", "fieldType": "float"}
    ,{"fieldName": "f319", "fieldType": "float"}
    ,{"fieldName": "f320", "fieldType": "float"}
    ,{"fieldName": "f321", "fieldType": "float"}
    ,{"fieldName": "f322", "fieldType": "float"}
    ,{"fieldName": "f323", "fieldType": "float"}
    ,{"fieldName": "f324", "fieldType": "float"}
    ,{"fieldName": "f325", "fieldType": "float"}
    ,{"fieldName": "f326", "fieldType": "float"}
    ,{"fieldName": "f327", "fieldType": "float"}
    ,{"fieldName": "f328", "fieldType": "float"}
    ,{"fieldName": "f329", "fieldType": "float"}
    ,{"fieldName": "f330", "fieldType": "float"}
    ,{"fieldName": "f331", "fieldType": "float"}
    ,{"fieldName": "f332", "fieldType": "float"}
    ,{"fieldName": "f333", "fieldType": "float"}
    ,{"fieldName": "f334", "fieldType": "float"}
    ,{"fieldName": "f335", "fieldType": "float"}
    ,{"fieldName": "f336", "fieldType": "float"}
    ,{"fieldName": "f337", "fieldType": "float"}
    ,{"fieldName": "f338", "fieldType": "float"}
    ,{"fieldName": "f339", "fieldType": "float"}
    ,{"fieldName": "f340", "fieldType": "float"}
    ,{"fieldName": "f341", "fieldType": "float"}
    ,{"fieldName": "f342", "fieldType": "float"}
    ,{"fieldName": "f343", "fieldType": "float"}
    ,{"fieldName": "f344", "fieldType": "float"}
    ,{"fieldName": "f345", "fieldType": "float"}
    ,{"fieldName": "f346", "fieldType": "float"}
    ,{"fieldName": "f347", "fieldType": "float"}
    ,{"fieldName": "f348", "fieldType": "float"}
    ,{"fieldName": "f349", "fieldType": "float"}
    ,{"fieldName": "f350", "fieldType": "float"}
    ,{"fieldName": "f351", "fieldType": "float"}
    ,{"fieldName": "f352", "fieldType": "float"}
    ,{"fieldName": "f353", "fieldType": "float"}
    ,{"fieldName": "f354", "fieldType": "float"}
    ,{"fieldName": "f355", "fieldType": "float"}
    ,{"fieldName": "f356", "fieldType": "float"}
    ,{"fieldName": "f357", "fieldType": "float"}
    ,{"fieldName": "f358", "fieldType": "float"}
    ,{"fieldName": "f359", "fieldType": "float"}
    ,{"fieldName": "f360", "fieldType": "float"}
    ,{"fieldName": "f361", "fieldType": "float"}
    ,{"fieldName": "f362", "fieldType": "float"}
    ,{"fieldName": "f363", "fieldType": "float"}
    ,{"fieldName": "f364", "fieldType": "float"}
    ,{"fieldName": "f365", "fieldType": "float"}
    ,{"fieldName": "f366", "fieldType": "float"}
    ,{"fieldName": "f367", "fieldType": "float"}
    ,{"fieldName": "f368", "fieldType": "float"}
    ,{"fieldName": "f369", "fieldType": "float"}
    ,{"fieldName": "f370", "fieldType": "float"}
    ,{"fieldName": "f371", "fieldType": "float"}
    ,{"fieldName": "f372", "fieldType": "float"}
    ,{"fieldName": "f373", "fieldType": "float"}
    ,{"fieldName": "f374", "fieldType": "float"}
    ,{"fieldName": "f375", "fieldType": "float"}
    ,{"fieldName": "f376", "fieldType": "float"}
    ,{"fieldName": "f377", "fieldType": "float"}
    ,{"fieldName": "f378", "fieldType": "float"}
    ,{"fieldName": "f379", "fieldType": "float"}
    ,{"fieldName": "f380", "fieldType": "float"}
    ,{"fieldName": "f381", "fieldType": "float"}
    ,{"fieldName": "f382", "fieldType": "float"}
    ,{"fieldName": "f383", "fieldType": "float"}
    ,{"fieldName": "f384", "fieldType": "float"}
    ,{"fieldName": "f385", "fieldType": "float"}
    ,{"fieldName": "f386", "fieldType": "float"}
    ,{"fieldName": "f387", "fieldType": "float"}
    ,{"fieldName": "f388", "fieldType": "float"}
    ,{"fieldName": "f389", "fieldType": "float"}
    ,{"fieldName": "f390", "fieldType": "float"}
    ,{"fieldName": "f391", "fieldType": "float"}
    ,{"fieldName": "f392", "fieldType": "float"}
    ,{"fieldName": "f393", "fieldType": "float"}
    ,{"fieldName": "f394", "fieldType": "float"}
    ,{"fieldName": "f395", "fieldType": "float"}
    ,{"fieldName": "f396", "fieldType": "float"}
    ,{"fieldName": "f397", "fieldType": "float"}
    ,{"fieldName": "f398", "fieldType": "float"}
    ,{"fieldName": "f399", "fieldType": "float"}
    ,{"fieldName": "f400", "fieldType": "float"}
    ,{"fieldName": "f401", "fieldType": "float"}
    ,{"fieldName": "f402", "fieldType": "float"}
    ,{"fieldName": "f403", "fieldType": "float"}
    ,{"fieldName": "f404", "fieldType": "float"}
    ,{"fieldName": "f405", "fieldType": "float"}
    ,{"fieldName": "f406", "fieldType": "float"}
    ,{"fieldName": "f407", "fieldType": "float"}
    ,{"fieldName": "f408", "fieldType": "float"}
    ,{"fieldName": "f409", "fieldType": "float"}
    ,{"fieldName": "f410", "fieldType": "float"}
    ,{"fieldName": "f411", "fieldType": "float"}
    ,{"fieldName": "f412", "fieldType": "float"}
    ,{"fieldName": "f413", "fieldType": "float"}
    ,{"fieldName": "f414", "fieldType": "float"}
    ,{"fieldName": "f415", "fieldType": "float"}
    ,{"fieldName": "f416", "fieldType": "float"}
    ,{"fieldName": "f417", "fieldType": "float"}
    ,{"fieldName": "f418", "fieldType": "float"}
    ,{"fieldName": "f419", "fieldType": "float"}
    ,{"fieldName": "f420", "fieldType": "float"}
    ,{"fieldName": "f421", "fieldType": "float"}
    ,{"fieldName": "f422", "fieldType": "float"}
    ,{"fieldName": "f423", "fieldType": "float"}
    ,{"fieldName": "f424", "fieldType": "float"}
    ,{"fieldName": "f425", "fieldType": "float"}
    ,{"fieldName": "f426", "fieldType": "float"}
    ,{"fieldName": "f427", "fieldType": "float"}
    ,{"fieldName": "f428", "fieldType": "float"}
    ,{"fieldName": "f429", "fieldType": "float"}
    ,{"fieldName": "f430", "fieldType": "float"}
    ,{"fieldName": "f431", "fieldType": "float"}
    ,{"fieldName": "f432", "fieldType": "float"}
    ,{"fieldName": "f433", "fieldType": "float"}
    ,{"fieldName": "f434", "fieldType": "float"}
    ,{"fieldName": "f435", "fieldType": "float"}
    ,{"fieldName": "f436", "fieldType": "float"}
    ,{"fieldName": "f437", "fieldType": "float"}
    ,{"fieldName": "f438", "fieldType": "float"}
    ,{"fieldName": "f439", "fieldType": "float"}
    ,{"fieldName": "f440", "fieldType": "float"}
    ,{"fieldName": "f441", "fieldType": "float"}
    ,{"fieldName": "f442", "fieldType": "float"}
    ,{"fieldName": "f443", "fieldType": "float"}
    ,{"fieldName": "f444", "fieldType": "float"}
    ,{"fieldName": "f445", "fieldType": "float"}
    ,{"fieldName": "f446", "fieldType": "float"}
    ,{"fieldName": "f447", "fieldType": "float"}
    ,{"fieldName": "f448", "fieldType": "float"}
    ,{"fieldName": "f449", "fieldType": "float"}
    ,{"fieldName": "f450", "fieldType": "float"}
    ,{"fieldName": "f451", "fieldType": "float"}
    ,{"fieldName": "f452", "fieldType": "float"}
    ,{"fieldName": "f453", "fieldType": "float"}
    ,{"fieldName": "f454", "fieldType": "float"}
    ,{"fieldName": "f455", "fieldType": "float"}
    ,{"fieldName": "f456", "fieldType": "float"}
    ,{"fieldName": "f457", "fieldType": "float"}
    ,{"fieldName": "f458", "fieldType": "float"}
    ,{"fieldName": "f459", "fieldType": "float"}
    ,{"fieldName": "f460", "fieldType": "float"}
    ,{"fieldName": "f461", "fieldType": "float"}
    ,{"fieldName": "f462", "fieldType": "float"}
    ,{"fieldName": "f463", "fieldType": "float"}
    ,{"fieldName": "f464", "fieldType": "float"}
    ,{"fieldName": "f465", "fieldType": "float"}
    ,{"fieldName": "f466", "fieldType": "float"}
    ,{"fieldName": "f467", "fieldType": "float"}
    ,{"fieldName": "f468", "fieldType": "float"}
    ,{"fieldName": "f469", "fieldType": "float"}
    ,{"fieldName": "f470", "fieldType": "float"}
    ,{"fieldName": "f471", "fieldType": "float"}
    ,{"fieldName": "f472", "fieldType": "float"}
    ,{"fieldName": "f473", "fieldType": "float"}
    ,{"fieldName": "f474", "fieldType": "float"}
    ,{"fieldName": "f475", "fieldType": "float"}
    ,{"fieldName": "f476", "fieldType": "float"}
    ,{"fieldName": "f477", "fieldType": "float"}
    ,{"fieldName": "f478", "fieldType": "float"}
    ,{"fieldName": "f479", "fieldType": "float"}
    ,{"fieldName": "f480", "fieldType": "float"}
    ,{"fieldName": "f481", "fieldType": "float"}
    ,{"fieldName": "f482", "fieldType": "float"}
    ,{"fieldName": "f483", "fieldType": "float"}
    ,{"fieldName": "f484", "fieldType": "float"}
    ,{"fieldName": "f485", "fieldType": "float"}
    ,{"fieldName": "f486", "fieldType": "float"}
    ,{"fieldName": "f487", "fieldType": "float"}
    ,{"fieldName": "f488", "fieldType": "float"}
    ,{"fieldName": "f489", "fieldType": "float"}
    ,{"fieldName": "f490", "fieldType": "float"}
    ,{"fieldName": "f491", "fieldType": "float"}
    ,{"fieldName": "f492", "fieldType": "float"}
    ,{"fieldName": "f493", "fieldType": "float"}
    ,{"fieldName": "f494", "fieldType": "float"}
    ,{"fieldName": "f495", "fieldType": "float"}
    ,{"fieldName": "f496", "fieldType": "float"}
    ,{"fieldName": "f497", "fieldType": "float"}
    ,{"fieldName": "f498", "fieldType": "float"}
    ,{"fieldName": "f499", "fieldType": "float"}
    ,{"fieldName": "f500", "fieldType": "float"}
    ,{"fieldName": "f501", "fieldType": "float"}
    ,{"fieldName": "f502", "fieldType": "float"}
    ,{"fieldName": "f503", "fieldType": "float"}
    ,{"fieldName": "f504", "fieldType": "float"}
    ,{"fieldName": "f505", "fieldType": "float"}
    ,{"fieldName": "f506", "fieldType": "float"}
    ,{"fieldName": "f507", "fieldType": "float"}
    ,{"fieldName": "f508", "fieldType": "float"}
    ,{"fieldName": "f509", "fieldType": "float"}
    ,{"fieldName": "f510", "fieldType": "float"}
    ,{"fieldName": "f511", "fieldType": "float"}
    ,{"fieldName": "f512", "fieldType": "float"}
    ,{"fieldName": "f513", "fieldType": "float"}
    ,{"fieldName": "f514", "fieldType": "float"}
    ,{"fieldName": "f515", "fieldType": "float"}
    ,{"fieldName": "f516", "fieldType": "float"}
    ,{"fieldName": "f517", "fieldType": "float"}
    ,{"fieldName": "f518", "fieldType": "float"}
    ,{"fieldName": "f519", "fieldType": "float"}
    ,{"fieldName": "f520", "fieldType": "float"}
    ,{"fieldName": "f521", "fieldType": "float"}
    ,{"fieldName": "f522", "fieldType": "float"}
    ,{"fieldName": "f523", "fieldType": "float"}
    ,{"fieldName": "f524", "fieldType": "float"}
    ,{"fieldName": "f525", "fieldType": "float"}
    ,{"fieldName": "f526", "fieldType": "float"}
    ,{"fieldName": "f527", "fieldType": "float"}
    ,{"fieldName": "f528", "fieldType": "float"}
    ,{"fieldName": "f529", "fieldType": "float"}
    ,{"fieldName": "f530", "fieldType": "float"}
    ,{"fieldName": "f531", "fieldType": "float"}
    ,{"fieldName": "f532", "fieldType": "float"}
    ,{"fieldName": "f533", "fieldType": "float"}
    ,{"fieldName": "f534", "fieldType": "float"}
    ,{"fieldName": "f535", "fieldType": "float"}
    ,{"fieldName": "f536", "fieldType": "float"}
    ,{"fieldName": "f537", "fieldType": "float"}
    ,{"fieldName": "f538", "fieldType": "float"}
    ,{"fieldName": "f539", "fieldType": "float"}
    ,{"fieldName": "f540", "fieldType": "float"}
    ,{"fieldName": "f541", "fieldType": "float"}
    ,{"fieldName": "f542", "fieldType": "float"}
    ,{"fieldName": "f543", "fieldType": "float"}
    ,{"fieldName": "f544", "fieldType": "float"}
    ,{"fieldName": "f545", "fieldType": "float"}
    ,{"fieldName": "f546", "fieldType": "float"}
    ,{"fieldName": "f547", "fieldType": "float"}
    ,{"fieldName": "f548", "fieldType": "float"}
    ,{"fieldName": "f549", "fieldType": "float"}
    ,{"fieldName": "f550", "fieldType": "float"}
    ,{"fieldName": "f551", "fieldType": "float"}
    ,{"fieldName": "f552", "fieldType": "float"}
    ,{"fieldName": "f553", "fieldType": "float"}
    ,{"fieldName": "f554", "fieldType": "float"}
    ,{"fieldName": "f555", "fieldType": "float"}
    ,{"fieldName": "f556", "fieldType": "float"}
    ,{"fieldName": "f557", "fieldType": "float"}
    ,{"fieldName": "f558", "fieldType": "float"}
    ,{"fieldName": "f559", "fieldType": "float"}
    ,{"fieldName": "f560", "fieldType": "float"}
    ,{"fieldName": "f561", "fieldType": "float"}
    ,{"fieldName": "f562", "fieldType": "float"}
    ,{"fieldName": "f563", "fieldType": "float"}
    ,{"fieldName": "f564", "fieldType": "float"}
    ,{"fieldName": "f565", "fieldType": "float"}
    ,{"fieldName": "f566", "fieldType": "float"}
    ,{"fieldName": "f567", "fieldType": "float"}
    ,{"fieldName": "f568", "fieldType": "float"}
    ,{"fieldName": "f569", "fieldType": "float"}
    ,{"fieldName": "f570", "fieldType": "float"}
    ,{"fieldName": "f571", "fieldType": "float"}
    ,{"fieldName": "f572", "fieldType": "float"}
    ,{"fieldName": "f573", "fieldType": "float"}
    ,{"fieldName": "f574", "fieldType": "float"}
    ,{"fieldName": "f575", "fieldType": "float"}
    ,{"fieldName": "f576", "fieldType": "float"}
    ,{"fieldName": "f577", "fieldType": "float"}
    ,{"fieldName": "f578", "fieldType": "float"}
    ,{"fieldName": "f579", "fieldType": "float"}
    ,{"fieldName": "f580", "fieldType": "float"}
    ,{"fieldName": "f581", "fieldType": "float"}
    ,{"fieldName": "f582", "fieldType": "float"}
    ,{"fieldName": "f583", "fieldType": "float"}
    ,{"fieldName": "f584", "fieldType": "float"}
    ,{"fieldName": "f585", "fieldType": "float"}
    ,{"fieldName": "f586", "fieldType": "float"}
    ,{"fieldName": "f587", "fieldType": "float"}
    ,{"fieldName": "f588", "fieldType": "float"}
    ,{"fieldName": "f589", "fieldType": "float"}
    ,{"fieldName": "f590", "fieldType": "float"}
    ,{"fieldName": "f591", "fieldType": "float"}
    ,{"fieldName": "f592", "fieldType": "float"}
    ,{"fieldName": "f593", "fieldType": "float"}
    ,{"fieldName": "f594", "fieldType": "float"}
    ,{"fieldName": "f595", "fieldType": "float"}
    ,{"fieldName": "f596", "fieldType": "float"}
    ,{"fieldName": "f597", "fieldType": "float"}
    ,{"fieldName": "f598", "fieldType": "float"}
    ,{"fieldName": "f599", "fieldType": "float"}
    ,{"fieldName": "f600", "fieldType": "float"}
    ,{"fieldName": "f601", "fieldType": "float"}
    ,{"fieldName": "f602", "fieldType": "float"}
    ,{"fieldName": "f603", "fieldType": "float"}
    ,{"fieldName": "f604", "fieldType": "float"}
    ,{"fieldName": "f605", "fieldType": "float"}
    ,{"fieldName": "f606", "fieldType": "float"}
    ,{"fieldName": "f607", "fieldType": "float"}
    ,{"fieldName": "f608", "fieldType": "float"}
    ,{"fieldName": "f609", "fieldType": "float"}
    ,{"fieldName": "f610", "fieldType": "float"}
    ,{"fieldName": "f611", "fieldType": "float"}
    ,{"fieldName": "f612", "fieldType": "float"}
    ,{"fieldName": "f613", "fieldType": "float"}
    ,{"fieldName": "f614", "fieldType": "float"}
    ,{"fieldName": "f615", "fieldType": "float"}
    ,{"fieldName": "f616", "fieldType": "float"}
    ,{"fieldName": "f617", "fieldType": "float"}
    ,{"fieldName": "f618", "fieldType": "float"}
    ,{"fieldName": "f619", "fieldType": "float"}
    ,{"fieldName": "f620", "fieldType": "float"}
    ,{"fieldName": "f621", "fieldType": "float"}
    ,{"fieldName": "f622", "fieldType": "float"}
    ,{"fieldName": "f623", "fieldType": "float"}
    ,{"fieldName": "f624", "fieldType": "float"}
    ,{"fieldName": "f625", "fieldType": "float"}
    ,{"fieldName": "f626", "fieldType": "float"}
    ,{"fieldName": "f627", "fieldType": "float"}
    ,{"fieldName": "f628", "fieldType": "float"}
    ,{"fieldName": "f629", "fieldType": "float"}
    ,{"fieldName": "f630", "fieldType": "float"}
    ,{"fieldName": "f631", "fieldType": "float"}
    ,{"fieldName": "f632", "fieldType": "float"}
    ,{"fieldName": "f633", "fieldType": "float"}
    ,{"fieldName": "f634", "fieldType": "float"}
    ,{"fieldName": "f635", "fieldType": "float"}
    ,{"fieldName": "f636", "fieldType": "float"}
    ,{"fieldName": "f637", "fieldType": "float"}
    ,{"fieldName": "f638", "fieldType": "float"}
    ,{"fieldName": "f639", "fieldType": "float"}
    ,{"fieldName": "f640", "fieldType": "float"}
    ,{"fieldName": "f641", "fieldType": "float"}
    ,{"fieldName": "f642", "fieldType": "float"}
    ,{"fieldName": "f643", "fieldType": "float"}
    ,{"fieldName": "f644", "fieldType": "float"}
    ,{"fieldName": "f645", "fieldType": "float"}
    ,{"fieldName": "f646", "fieldType": "float"}
    ,{"fieldName": "f647", "fieldType": "float"}
    ,{"fieldName": "f648", "fieldType": "float"}
    ,{"fieldName": "f649", "fieldType": "float"}
    ,{"fieldName": "f650", "fieldType": "float"}
    ,{"fieldName": "f651", "fieldType": "float"}
    ,{"fieldName": "f652", "fieldType": "float"}
    ,{"fieldName": "f653", "fieldType": "float"}
    ,{"fieldName": "f654", "fieldType": "float"}
    ,{"fieldName": "f655", "fieldType": "float"}
    ,{"fieldName": "f656", "fieldType": "float"}
    ,{"fieldName": "f657", "fieldType": "float"}
    ,{"fieldName": "f658", "fieldType": "float"}
    ,{"fieldName": "f659", "fieldType": "float"}
    ,{"fieldName": "f660", "fieldType": "float"}
    ,{"fieldName": "f661", "fieldType": "float"}
    ,{"fieldName": "f662", "fieldType": "float"}
    ,{"fieldName": "f663", "fieldType": "float"}
    ,{"fieldName": "f664", "fieldType": "float"}
    ,{"fieldName": "f665", "fieldType": "float"}
    ,{"fieldName": "f666", "fieldType": "float"}
    ,{"fieldName": "f667", "fieldType": "float"}
    ,{"fieldName": "f668", "fieldType": "float"}
    ,{"fieldName": "f669", "fieldType": "float"}
    ,{"fieldName": "f670", "fieldType": "float"}
    ,{"fieldName": "f671", "fieldType": "float"}
    ,{"fieldName": "f672", "fieldType": "float"}
    ,{"fieldName": "f673", "fieldType": "float"}
    ,{"fieldName": "f674", "fieldType": "float"}
    ,{"fieldName": "f675", "fieldType": "float"}
    ,{"fieldName": "f676", "fieldType": "float"}
    ,{"fieldName": "f677", "fieldType": "float"}
    ,{"fieldName": "f678", "fieldType": "float"}
    ,{"fieldName": "f679", "fieldType": "float"}
    ,{"fieldName": "f680", "fieldType": "float"}
    ,{"fieldName": "f681", "fieldType": "float"}
    ,{"fieldName": "f682", "fieldType": "float"}
    ,{"fieldName": "f683", "fieldType": "float"}
    ,{"fieldName": "f684", "fieldType": "float"}
    ,{"fieldName": "f685", "fieldType": "float"}
    ,{"fieldName": "f686", "fieldType": "float"}
    ,{"fieldName": "f687", "fieldType": "float"}
    ,{"fieldName": "f688", "fieldType": "float"}
    ,{"fieldName": "f689", "fieldType": "float"}
    ,{"fieldName": "f690", "fieldType": "float"}
    ,{"fieldName": "f691", "fieldType": "float"}
    ,{"fieldName": "f692", "fieldType": "float"}
    ,{"fieldName": "f693", "fieldType": "float"}
    ,{"fieldName": "f694", "fieldType": "float"}
    ,{"fieldName": "f695", "fieldType": "float"}
    ,{"fieldName": "f696", "fieldType": "float"}
    ,{"fieldName": "f697", "fieldType": "float"}
    ,{"fieldName": "f698", "fieldType": "float"}
    ,{"fieldName": "f699", "fieldType": "float"}
    ,{"fieldName": "f700", "fieldType": "float"}
    ,{"fieldName": "f701", "fieldType": "float"}
    ,{"fieldName": "f702", "fieldType": "float"}
    ,{"fieldName": "f703", "fieldType": "float"}
    ,{"fieldName": "f704", "fieldType": "float"}
    ,{"fieldName": "f705", "fieldType": "float"}
    ,{"fieldName": "f706", "fieldType": "float"}
    ,{"fieldName": "f707", "fieldType": "float"}
    ,{"fieldName": "f708", "fieldType": "float"}
    ,{"fieldName": "f709", "fieldType": "float"}
    ,{"fieldName": "f710", "fieldType": "float"}
    ,{"fieldName": "f711", "fieldType": "float"}
    ,{"fieldName": "f712", "fieldType": "float"}
    ,{"fieldName": "f713", "fieldType": "float"}
    ,{"fieldName": "f714", "fieldType": "float"}
    ,{"fieldName": "f715", "fieldType": "float"}
    ,{"fieldName": "f716", "fieldType": "float"}
    ,{"fieldName": "f717", "fieldType": "float"}
    ,{"fieldName": "f718", "fieldType": "float"}
    ,{"fieldName": "f719", "fieldType": "float"}
    ,{"fieldName": "f720", "fieldType": "float"}
    ,{"fieldName": "f721", "fieldType": "float"}
    ,{"fieldName": "f722", "fieldType": "float"}
    ,{"fieldName": "f723", "fieldType": "float"}
    ,{"fieldName": "f724", "fieldType": "float"}
    ,{"fieldName": "f725", "fieldType": "float"}
    ,{"fieldName": "f726", "fieldType": "float"}
    ,{"fieldName": "f727", "fieldType": "float"}
    ,{"fieldName": "f728", "fieldType": "float"}
    ,{"fieldName": "f729", "fieldType": "float"}
    ,{"fieldName": "f730", "fieldType": "float"}
    ,{"fieldName": "f731", "fieldType": "float"}
    ,{"fieldName": "f732", "fieldType": "float"}
    ,{"fieldName": "f733", "fieldType": "float"}
    ,{"fieldName": "f734", "fieldType": "float"}
    ,{"fieldName": "f735", "fieldType": "float"}
    ,{"fieldName": "f736", "fieldType": "float"}
    ,{"fieldName": "f737", "fieldType": "float"}
    ,{"fieldName": "f738", "fieldType": "float"}
    ,{"fieldName": "f739", "fieldType": "float"}
    ,{"fieldName": "f740", "fieldType": "float"}
    ,{"fieldName": "f741", "fieldType": "float"}
    ,{"fieldName": "f742", "fieldType": "float"}
    ,{"fieldName": "f743", "fieldType": "float"}
    ,{"fieldName": "f744", "fieldType": "float"}
    ,{"fieldName": "f745", "fieldType": "float"}
    ,{"fieldName": "f746", "fieldType": "float"}
    ,{"fieldName": "f747", "fieldType": "float"}
    ,{"fieldName": "f748", "fieldType": "float"}
    ,{"fieldName": "f749", "fieldType": "float"}
    ,{"fieldName": "f750", "fieldType": "float"}
    ,{"fieldName": "f751", "fieldType": "float"}
    ,{"fieldName": "f752", "fieldType": "float"}
    ,{"fieldName": "f753", "fieldType": "float"}
    ,{"fieldName": "f754", "fieldType": "float"}
    ,{"fieldName": "f755", "fieldType": "float"}
    ,{"fieldName": "f756", "fieldType": "float"}
    ,{"fieldName": "f757", "fieldType": "float"}
    ,{"fieldName": "f758", "fieldType": "float"}
    ,{"fieldName": "f759", "fieldType": "float"}
    ,{"fieldName": "f760", "fieldType": "float"}
    ,{"fieldName": "f761", "fieldType": "float"}
    ,{"fieldName": "f762", "fieldType": "float"}
    ,{"fieldName": "f763", "fieldType": "float"}
    ,{"fieldName": "f764", "fieldType": "float"}
    ,{"fieldName": "f765", "fieldType": "float"}
    ,{"fieldName": "f766", "fieldType": "float"}
    ,{"fieldName": "f767", "fieldType": "float"}
    ,{"fieldName": "f768", "fieldType": "float"}
    ,{"fieldName": "f769", "fieldType": "float"}
    ,{"fieldName": "f770", "fieldType": "float"}
    ,{"fieldName": "f771", "fieldType": "float"}
    ,{"fieldName": "f772", "fieldType": "float"}
    ,{"fieldName": "f773", "fieldType": "float"}
    ,{"fieldName": "f774", "fieldType": "float"}
    ,{"fieldName": "f775", "fieldType": "float"}
    ,{"fieldName": "f776", "fieldType": "float"}
    ,{"fieldName": "f777", "fieldType": "float"}
    ,{"fieldName": "f778", "fieldType": "float"}
    ,{"fieldName": "f779", "fieldType": "float"}
    ,{"fieldName": "f780", "fieldType": "float"}
    ,{"fieldName": "f781", "fieldType": "float"}
    ,{"fieldName": "f782", "fieldType": "float"}
    ,{"fieldName": "f783", "fieldType": "float"}
    ,{"fieldName": "f784", "fieldType": "float"}
    ,{"fieldName": "f785", "fieldType": "float"}
    ,{"fieldName": "f786", "fieldType": "float"}
    ,{"fieldName": "f787", "fieldType": "float"}
    ,{"fieldName": "f788", "fieldType": "float"}
    ,{"fieldName": "f789", "fieldType": "float"}
    ,{"fieldName": "f790", "fieldType": "float"}
    ,{"fieldName": "f791", "fieldType": "float"}
    ,{"fieldName": "f792", "fieldType": "float"}
    ,{"fieldName": "f793", "fieldType": "float"}
    ,{"fieldName": "f794", "fieldType": "float"}
    ,{"fieldName": "f795", "fieldType": "float"}
    ,{"fieldName": "f796", "fieldType": "float"}
    ,{"fieldName": "f797", "fieldType": "float"}
    ,{"fieldName": "f798", "fieldType": "float"}
    ,{"fieldName": "f799", "fieldType": "float"}
    ,{"fieldName": "f800", "fieldType": "float"}
    ,{"fieldName": "f801", "fieldType": "float"}
    ,{"fieldName": "f802", "fieldType": "float"}
    ,{"fieldName": "f803", "fieldType": "float"}
    ,{"fieldName": "f804", "fieldType": "float"}
    ,{"fieldName": "f805", "fieldType": "float"}
    ,{"fieldName": "f806", "fieldType": "float"}
    ,{"fieldName": "f807", "fieldType": "float"}
    ,{"fieldName": "f808", "fieldType": "float"}
    ,{"fieldName": "f809", "fieldType": "float"}
    ,{"fieldName": "f810", "fieldType": "float"}
    ,{"fieldName": "f811", "fieldType": "float"}
    ,{"fieldName": "f812", "fieldType": "float"}
    ,{"fieldName": "f813", "fieldType": "float"}
    ,{"fieldName": "f814", "fieldType": "float"}
    ,{"fieldName": "f815", "fieldType": "float"}
    ,{"fieldName": "f816", "fieldType": "float"}
    ,{"fieldName": "f817", "fieldType": "float"}
    ,{"fieldName": "f818", "fieldType": "float"}
    ,{"fieldName": "f819", "fieldType": "float"}
    ,{"fieldName": "f820", "fieldType": "float"}
    ,{"fieldName": "f821", "fieldType": "float"}
    ,{"fieldName": "f822", "fieldType": "float"}
    ,{"fieldName": "f823", "fieldType": "float"}
    ,{"fieldName": "f824", "fieldType": "float"}
    ,{"fieldName": "f825", "fieldType": "float"}
    ,{"fieldName": "f826", "fieldType": "float"}
    ,{"fieldName": "f827", "fieldType": "float"}
    ,{"fieldName": "f828", "fieldType": "float"}
    ,{"fieldName": "f829", "fieldType": "float"}
    ,{"fieldName": "f830", "fieldType": "float"}
    ,{"fieldName": "f831", "fieldType": "float"}
    ,{"fieldName": "f832", "fieldType": "float"}
    ,{"fieldName": "f833", "fieldType": "float"}
    ,{"fieldName": "f834", "fieldType": "float"}
    ,{"fieldName": "f835", "fieldType": "float"}
    ,{"fieldName": "f836", "fieldType": "float"}
    ,{"fieldName": "f837", "fieldType": "float"}
    ,{"fieldName": "f838", "fieldType": "float"}
    ,{"fieldName": "f839", "fieldType": "float"}
    ,{"fieldName": "f840", "fieldType": "float"}
    ,{"fieldName": "f841", "fieldType": "float"}
    ,{"fieldName": "f842", "fieldType": "float"}
    ,{"fieldName": "f843", "fieldType": "float"}
    ,{"fieldName": "f844", "fieldType": "float"}
    ,{"fieldName": "f845", "fieldType": "float"}
    ,{"fieldName": "f846", "fieldType": "float"}
    ,{"fieldName": "f847", "fieldType": "float"}
    ,{"fieldName": "f848", "fieldType": "float"}
    ,{"fieldName": "f849", "fieldType": "float"}
    ,{"fieldName": "f850", "fieldType": "float"}
    ,{"fieldName": "f851", "fieldType": "float"}
    ,{"fieldName": "f852", "fieldType": "float"}
    ,{"fieldName": "f853", "fieldType": "float"}
    ,{"fieldName": "f854", "fieldType": "float"}
    ,{"fieldName": "f855", "fieldType": "float"}
    ,{"fieldName": "f856", "fieldType": "float"}
    ,{"fieldName": "f857", "fieldType": "float"}
    ,{"fieldName": "f858", "fieldType": "float"}
    ,{"fieldName": "f859", "fieldType": "float"}
    ,{"fieldName": "f860", "fieldType": "float"}
    ,{"fieldName": "f861", "fieldType": "float"}
    ,{"fieldName": "f862", "fieldType": "float"}
    ,{"fieldName": "f863", "fieldType": "float"}
    ,{"fieldName": "f864", "fieldType": "float"}
    ,{"fieldName": "f865", "fieldType": "float"}
    ,{"fieldName": "f866", "fieldType": "float"}
    ,{"fieldName": "f867", "fieldType": "float"}
    ,{"fieldName": "f868", "fieldType": "float"}
    ,{"fieldName": "f869", "fieldType": "float"}
    ,{"fieldName": "f870", "fieldType": "float"}
    ,{"fieldName": "f871", "fieldType": "float"}
    ,{"fieldName": "f872", "fieldType": "float"}
    ,{"fieldName": "f873", "fieldType": "float"}
    ,{"fieldName": "f874", "fieldType": "float"}
    ,{"fieldName": "f875", "fieldType": "float"}
    ,{"fieldName": "f876", "fieldType": "float"}
    ,{"fieldName": "f877", "fieldType": "float"}
    ,{"fieldName": "f878", "fieldType": "float"}
    ,{"fieldName": "f879", "fieldType": "float"}
    ,{"fieldName": "f880", "fieldType": "float"}
    ,{"fieldName": "f881", "fieldType": "float"}
    ,{"fieldName": "f882", "fieldType": "float"}
    ,{"fieldName": "f883", "fieldType": "float"}
    ,{"fieldName": "f884", "fieldType": "float"}
    ,{"fieldName": "f885", "fieldType": "float"}
    ,{"fieldName": "f886", "fieldType": "float"}
    ,{"fieldName": "f887", "fieldType": "float"}
    ,{"fieldName": "f888", "fieldType": "float"}
    ,{"fieldName": "f889", "fieldType": "float"}
    ,{"fieldName": "f890", "fieldType": "float"}
    ,{"fieldName": "f891", "fieldType": "float"}
    ,{"fieldName": "f892", "fieldType": "float"}
    ,{"fieldName": "f893", "fieldType": "float"}
    ,{"fieldName": "f894", "fieldType": "float"}
    ,{"fieldName": "f895", "fieldType": "float"}
    ,{"fieldName": "f896", "fieldType": "float"}
    ,{"fieldName": "f897", "fieldType": "float"}
    ,{"fieldName": "f898", "fieldType": "float"}
    ,{"fieldName": "f899", "fieldType": "float"}
    ,{"fieldName": "f900", "fieldType": "float"}
    ,{"fieldName": "f901", "fieldType": "float"}
    ,{"fieldName": "f902", "fieldType": "float"}
    ,{"fieldName": "f903", "fieldType": "float"}
    ,{"fieldName": "f904", "fieldType": "float"}
    ,{"fieldName": "f905", "fieldType": "float"}
    ,{"fieldName": "f906", "fieldType": "float"}
    ,{"fieldName": "f907", "fieldType": "float"}
    ,{"fieldName": "f908", "fieldType": "float"}
    ,{"fieldName": "f909", "fieldType": "float"}
    ,{"fieldName": "f910", "fieldType": "float"}
    ,{"fieldName": "f911", "fieldType": "float"}
    ,{"fieldName": "f912", "fieldType": "float"}
    ,{"fieldName": "f913", "fieldType": "float"}
    ,{"fieldName": "f914", "fieldType": "float"}
    ,{"fieldName": "f915", "fieldType": "float"}
    ,{"fieldName": "f916", "fieldType": "float"}
    ,{"fieldName": "f917", "fieldType": "float"}
    ,{"fieldName": "f918", "fieldType": "float"}
    ,{"fieldName": "f919", "fieldType": "float"}
    ,{"fieldName": "f920", "fieldType": "float"}
    ,{"fieldName": "f921", "fieldType": "float"}
    ,{"fieldName": "f922", "fieldType": "float"}
    ,{"fieldName": "f923", "fieldType": "float"}
    ,{"fieldName": "f924", "fieldType": "float"}
    ,{"fieldName": "f925", "fieldType": "float"}
    ,{"fieldName": "f926", "fieldType": "float"}
    ,{"fieldName": "f927", "fieldType": "float"}
    ,{"fieldName": "f928", "fieldType": "float"}
    ,{"fieldName": "f929", "fieldType": "float"}
    ,{"fieldName": "f930", "fieldType": "float"}
    ,{"fieldName": "f931", "fieldType": "float"}
    ,{"fieldName": "f932", "fieldType": "float"}
    ,{"fieldName": "f933", "fieldType": "float"}
    ,{"fieldName": "f934", "fieldType": "float"}
    ,{"fieldName": "f935", "fieldType": "float"}
    ,{"fieldName": "f936", "fieldType": "float"}
    ,{"fieldName": "f937", "fieldType": "float"}
    ,{"fieldName": "f938", "fieldType": "float"}
    ,{"fieldName": "f939", "fieldType": "float"}
    ,{"fieldName": "f940", "fieldType": "float"}
    ,{"fieldName": "f941", "fieldType": "float"}
    ,{"fieldName": "f942", "fieldType": "float"}
    ,{"fieldName": "f943", "fieldType": "float"}
    ,{"fieldName": "f944", "fieldType": "float"}
    ,{"fieldName": "f945", "fieldType": "float"}
    ,{"fieldName": "f946", "fieldType": "float"}
    ,{"fieldName": "f947", "fieldType": "float"}
    ,{"fieldName": "f948", "fieldType": "float"}
    ,{"fieldName": "f949", "fieldType": "float"}
    ,{"fieldName": "f950", "fieldType": "float"}
    ,{"fieldName": "f951", "fieldType": "float"}
    ,{"fieldName": "f952", "fieldType": "float"}
    ,{"fieldName": "f953", "fieldType": "float"}
    ,{"fieldName": "f954", "fieldType": "float"}
    ,{"fieldName": "f955", "fieldType": "float"}
    ,{"fieldName": "f956", "fieldType": "float"}
    ,{"fieldName": "f957", "fieldType": "float"}
    ,{"fieldName": "f958", "fieldType": "float"}
    ,{"fieldName": "f959", "fieldType": "float"}
    ,{"fieldName": "f960", "fieldType": "float"}
    ,{"fieldName": "f961", "fieldType": "float"}
    ,{"fieldName": "f962", "fieldType": "float"}
    ,{"fieldName": "f963", "fieldType": "float"}
    ,{"fieldName": "f964", "fieldType": "float"}
    ,{"fieldName": "f965", "fieldType": "float"}
    ,{"fieldName": "f966", "fieldType": "float"}
    ,{"fieldName": "f967", "fieldType": "float"}
    ,{"fieldName": "f968", "fieldType": "float"}
    ,{"fieldName": "f969", "fieldType": "float"}
    ,{"fieldName": "f970", "fieldType": "float"}
    ,{"fieldName": "f971", "fieldType": "float"}
    ,{"fieldName": "f972", "fieldType": "float"}
    ,{"fieldName": "f973", "fieldType": "float"}
    ,{"fieldName": "f974", "fieldType": "float"}
    ,{"fieldName": "f975", "fieldType": "float"}
    ,{"fieldName": "f976", "fieldType": "float"}
    ,{"fieldName": "f977", "fieldType": "float"}
    ,{"fieldName": "f978", "fieldType": "float"}
    ,{"fieldName": "f979", "fieldType": "float"}
    ,{"fieldName": "f980", "fieldType": "float"}
    ,{"fieldName": "f981", "fieldType": "float"}
    ,{"fieldName": "f982", "fieldType": "float"}
    ,{"fieldName": "f983", "fieldType": "float"}
    ,{"fieldName": "f984", "fieldType": "float"}
    ,{"fieldName": "f985", "fieldType": "float"}
    ,{"fieldName": "f986", "fieldType": "float"}
    ,{"fieldName": "f987", "fieldType": "float"}
    ,{"fieldName": "f988", "fieldType": "float"}
    ,{"fieldName": "f989", "fieldType": "float"}
    ,{"fieldName": "f990", "fieldType": "float"}
    ,{"fieldName": "f991", "fieldType": "float"}
    ,{"fieldName": "f992", "fieldType": "float"}
    ,{"fieldName": "f993", "fieldType": "float"}
    ,{"fieldName": "f994", "fieldType": "float"}
    ,{"fieldName": "f995", "fieldType": "float"}
    ,{"fieldName": "f996", "fieldType": "float"}
    ,{"fieldName": "f997", "fieldType": "float"}
    ,{"fieldName": "f998", "fieldType": "float"}
    ,{"fieldName": "f999", "fieldType": "float"}
  ],
  "streamDef": {
    "info": "test",
    "version": 1,
    "streams": [
      {
        "info": "fais.csv",
        "source": "file://fais.csv",
        "columns": [
          "*"
        ],
        "last_record": 10000
      }
    ]
  },
  "inferenceType": "MultiStep",
  "inferenceArgs": {
    "predictionSteps": [
      1
    ],
    "predictedField": "move_x"
  },
  "iterationCount": -1,
  "swarmSize": "medium"
}




def swarm_over_data():
  return permutations_runner.runWithConfig(SWARM_CONFIG,
    {'maxWorkers': 12, 'overwrite': True})


def run_fais_experiment():
  input_file = "fais.csv"
  # from model_0 import model_params
  # model_params = swarm_over_data()

  # pickle.dump(model_params, open('model_params', 'wb'))

  # if PLOT:
  #   output = NuPICPlotOutput("fais_output", show_anomaly_score=True)
  # else:
  #   output = NuPICFileOutput("fais_output", show_anomaly_score=False)

  # model = ModelFactory.loadFromCheckpoint('/s/nupic/examples/fais/model_0.test.freeze/savedmodels/DefaultTask.nta')
  # model.enableInference({"predictedField": "move_x"})

  # print model.run({"move_x": 0.5, "f189": 0.00001})

  # with open(input_file, "rb") as fais_input:
  #   csv_reader = csv.reader(fais_input)
  #
  #   # skip header rows
  #   csv_reader.next()
  #   csv_reader.next()
  #   csv_reader.next()
  #
  #   # the real data
  #   for row in csv_reader:
  #     move_x = float(row[2])
  #     result = model.run({"move_x": move_x})
  #     output.write(move_x, result, prediction_step=1)
  #
  # output.close()

import cherrypy
from cherrypy.lib.httputil import parse_query_string
class HelloWorld(object):
    def index(self, f189, move_x):
        x = str(model.run({"move_x": float(move_x), "f189": float(f189)}).inferences['multiStepBestPredictions'][1])
        print str(f189), ' => ', x
        return x
    index.exposed = True


input_file = "fais.csv"
model = ModelFactory.loadFromCheckpoint('/s/nupic/examples/fais/model_0.test/savedmodels/DefaultTask.nta')
model.enableInference({"predictedField": "move_x"})

if __name__ == "__main__":
    # swarm_over_data()
    cherrypy.quickstart(HelloWorld())
    # run_fais_experiment()