/* Illustrations for gallery cards that have no thumbnail or video.
 *
 * Each picture is drawn from the entry itself: the robot (and its variant, such as
 * wheel-foot TRON1) and a scene picked from the section and the description, such as
 * stairs, a navigation path or a table to work at. They are diagrams, not footage, and
 * the card says so. build_gallery.py inlines this file into docs/index.html.
 */
(function () {
  "use strict";
  var G = 146; // ground line in a 320 x 180 picture
  var C = "currentColor";

  function rng(seed) { // small deterministic generator, so a card always looks the same
    var h = 2166136261;
    for (var i = 0; i < seed.length; i++) { h ^= seed.charCodeAt(i); h = Math.imul(h, 16777619); }
    return function () { h ^= h << 13; h ^= h >>> 17; h ^= h << 5; return ((h >>> 0) % 10000) / 10000; };
  }
  function f(n) { return Math.round(n * 10) / 10; }
  function line(x1, y1, x2, y2, w, op) {
    return '<path d="M' + f(x1) + " " + f(y1) + "L" + f(x2) + " " + f(y2) + '" stroke="' + C + '" stroke-width="' + w +
      '" stroke-linecap="round" fill="none"' + (op ? ' opacity="' + op + '"' : "") + "/>";
  }
  function poly(pts, w) { // a bent limb through several points
    return '<path d="M' + pts.map(function (p) { return f(p[0]) + " " + f(p[1]); }).join("L") + '" stroke="' + C +
      '" stroke-width="' + w + '" stroke-linecap="round" stroke-linejoin="round" fill="none"/>';
  }
  function fill(extra) { return extra === HL ? "var(--surface)" : C; }
  function rect(x, y, w, h, r, op, extra) {
    return '<rect x="' + f(x) + '" y="' + f(y) + '" width="' + f(w) + '" height="' + f(h) + '" rx="' + (r || 0) +
      '" fill="' + fill(extra) + '"' + (op != null ? ' fill-opacity="' + op + '"' : "") + "/>";
  }
  function circ(x, y, r, op, extra) {
    return '<circle cx="' + f(x) + '" cy="' + f(y) + '" r="' + f(r) + '" fill="' + fill(extra) + '"' +
      (op != null ? ' fill-opacity="' + op + '"' : "") + "/>";
  }
  function ring(x, y, r, w, op, dash) {
    return '<circle cx="' + f(x) + '" cy="' + f(y) + '" r="' + f(r) + '" fill="none" stroke="' + C + '" stroke-width="' + w + '"' +
      (op ? ' opacity="' + op + '"' : "") + (dash ? ' stroke-dasharray="' + dash + '"' : "") + "/>";
  }
  var HL = "hl"; // pass as `extra` to draw in the card's surface color (a highlight)

  /* ---------- robots: x is the centre between the feet, g the ground under them ---------- */

  function legs(x, g, s, foot, step, hipY) {
    var out = "";
    [-1, 1].forEach(function (side, i) {
      var hx = x + side * 11 * s, off = (i ? step : -step) * s;
      var fx = hx + off, kx = (hx + fx) / 2 + 9 * s, ky = (hipY + g) / 2 + 2 * s;
      var fy = foot === "wheel" ? g - 9 * s : g - 2 * s;
      out += poly([[hx, hipY], [kx, ky], [fx, fy]], 6.5 * s);
      if (foot === "wheel") out += ring(fx, g - 9 * s, 8.5 * s, 4 * s) + circ(fx, g - 9 * s, 2.4 * s);
      else if (foot === "sole") out += line(fx - 6 * s, g - 2 * s, fx + 8 * s, g - 2 * s, 5 * s);
      else out += circ(fx, g - 3 * s, 3.6 * s);
    });
    return out;
  }
  function tron1(x, g, s, foot, step) {
    var top = g - 90 * s;
    return legs(x, g, s, foot, step, top + 30 * s) +
      rect(x - 21 * s, top, 42 * s, 30 * s, 7 * s) +
      rect(x + 5 * s, top + 9 * s, 12 * s, 7 * s, 3 * s, null, HL);
  }
  function p1(x, g, s, foot, step) {
    var top = g - 98 * s;
    return legs(x, g, s, foot, step, top + 30 * s) +
      rect(x - 16 * s, top, 32 * s, 30 * s, 5 * s) + circ(x + 6 * s, top + 11 * s, 3.5 * s, null, HL);
  }
  function arms(x, sy, s, reach) { // two arms from shoulder height sy, reaching forward
    var out = "";
    [0, 1].forEach(function (i) {
      var sx = x + (i ? 15 : -15) * s, ex = sx + 10 * s + (i ? 4 : 0) * s, ey = sy + 18 * s;
      var hx = ex + (reach ? 20 : 8) * s, hy = ey + (reach ? 2 : 14) * s;
      out += poly([[sx, sy], [ex, ey], [hx, hy]], 5 * s);
      out += line(hx, hy, hx + 6 * s, hy - 4 * s, 3.2 * s) + line(hx, hy, hx + 6 * s, hy + 4 * s, 3.2 * s);
    });
    return out;
  }
  function tron2(x, g, s, foot, step, reach) {
    var base = g - 74 * s, top = base - 46 * s;
    return legs(x, g, s, foot, step, base + 22 * s) +
      rect(x - 20 * s, base, 40 * s, 24 * s, 6 * s) +
      rect(x - 13 * s, top, 26 * s, 48 * s, 6 * s) +
      rect(x - 8 * s, top - 16 * s, 16 * s, 13 * s, 4 * s) +
      rect(x - 4 * s, top - 12 * s, 9 * s, 5 * s, 2 * s, null, HL) +
      arms(x, top + 8 * s, s, reach);
  }
  function humanoid(x, g, s, step, reach, luna) {
    var hr = (luna ? 11 : 9) * s, top = g - (luna ? 104 : 112) * s;
    var hipY = top + 2 * hr + 50 * s, out = "";
    [-1, 1].forEach(function (side, i) {
      var hx = x + side * 7 * s, fx = hx + (i ? step : -step) * s, kx = (hx + fx) / 2 + 4 * s, ky = (hipY + g) / 2;
      out += poly([[hx, hipY], [kx, ky], [fx, g - 3 * s]], 6.5 * s) + line(fx - 3 * s, g - 2 * s, fx + 7 * s, g - 2 * s, 4.5 * s);
    });
    var sy = top + 2 * hr + 10 * s;
    [-1, 1].forEach(function (side, i) {
      var sx = x + side * 14 * s;
      if (reach) out += poly([[sx, sy], [sx + 10 * s, sy + 16 * s], [sx + 28 * s, sy + 14 * s]], 5 * s);
      else out += poly([[sx, sy], [sx + side * 4 * s + (i ? 5 : -3) * s, sy + 20 * s], [sx + side * 2 * s + (i ? 9 : -6) * s, sy + 38 * s]], 5 * s);
    });
    out += rect(x - 15 * s, top + 2 * hr + 4 * s, 30 * s, 48 * s, 9 * s);
    out += circ(x, top + hr, hr) + rect(x - 1 * s, top + hr - 3.5 * s, hr, 6 * s, 3 * s, null, HL);
    return out;
  }
  function w1(x, g, s, step) {
    var by = g - 52 * s, out = "";
    [-26, -14, 14, 26].forEach(function (dx, i) {
      var hx = x + dx * s, fx = hx + (i % 2 ? step : -step) * 0.6 * s, kx = hx + (dx < 0 ? -8 : 8) * s;
      out += poly([[hx, by + 10 * s], [kx, by + 26 * s], [fx, g - 9 * s]], 6 * s) + ring(fx, g - 9 * s, 8 * s, 3.6 * s) + circ(fx, g - 9 * s, 2.2 * s);
    });
    out += rect(x - 36 * s, by - 4 * s, 72 * s, 20 * s, 7 * s) + rect(x + 26 * s, by - 10 * s, 16 * s, 13 * s, 4 * s);
    out += rect(x + 31 * s, by - 7 * s, 8 * s, 5 * s, 2 * s, null, HL);
    return out;
  }
  function robotKind(item, text) {
    var r = item.robots[0];
    if (!r) return null;
    var foot = /wheel-foot|wheeled|wheel-legged|\bwheels?\b|wf_|\bwf\b|driving/.test(text) ? "wheel" : /sole-foot|\bsf\b|sf_/.test(text) ? "sole" : "point";
    if (r === "TRON2") foot = /wheel/.test(text) ? "wheel" : "point";
    return { name: r, foot: foot };
  }
  function drawRobot(k, x, g, s, step, reach) {
    if (!k) return "";
    switch (k.name) {
      case "TRON1": return tron1(x, g, s, k.foot, step);
      case "TRON2": return tron2(x, g, s, k.foot, step, reach);
      case "Oli": return humanoid(x, g, s, step, reach, false);
      case "Luna": return humanoid(x, g, s, step, reach, true);
      case "P1": return p1(x, g, s, "point", step);
      case "W1": return w1(x, g, s, step);
    }
    return "";
  }
  function hasArms(k) { return k && (k.name === "TRON2" || k.name === "Oli" || k.name === "Luna"); }

  /* ---------- scenes: each returns what goes behind and in front of the robot ---------- */

  function ground(op) { return line(0, G, 320, G, 2, op || 0.35); }
  function grid(r, op) { // perspective floor
    var out = "", vx = 160 + (r() - 0.5) * 60;
    for (var i = -6; i <= 6; i++) out += line(vx + i * 6, 88, 160 + i * 56, 180, 1, op);
    [96, 108, 124, 146, 176].forEach(function (y) { out += line(0, y, 320, y, 1, op); });
    return out;
  }
  function win(x, y, w, h) { // a window frame with a title bar
    return rect(x, y, w, h, 6, 0.12) + '<rect x="' + x + '" y="' + y + '" width="' + w + '" height="' + h + '" rx="6" fill="none" stroke="' + C +
      '" stroke-width="2" opacity=".55"/>' + line(x, y + 14, x + w, y + 14, 2, 0.55) + circ(x + 9, y + 7, 2.4, 0.6) + circ(x + 17, y + 7, 2.4, 0.6);
  }
  function pin(x, y, s) {
    s = s || 1;
    return '<path d="M' + x + " " + y + "c" + -9 * s + " " + -11 * s + " " + -11 * s + " " + -15 * s + " " + -11 * s + " " + -21 * s +
      "a" + 11 * s + " " + 11 * s + " 0 0 1 " + 22 * s + " 0c0 " + 6 * s + " " + -2 * s + " " + 10 * s + " " + -11 * s + " " + 21 * s +
      'z" fill="' + C + '"/>' + circ(x, y - 21 * s, 4 * s, null, HL);
  }

  var SCENES = {
    stairs: function (r) {
      var x0 = 178 + r() * 14, h = 13, w = 24, d = "M" + x0 + " " + G;
      for (var i = 0; i < 6; i++) d += "L" + (x0 + i * w) + " " + (G - (i + 1) * h) + "L" + (x0 + (i + 1) * w) + " " + (G - (i + 1) * h);
      d += "L320 " + G + "Z";
      return { back: '<path d="' + d + '" fill="' + C + '" fill-opacity=".2"/>' + ground(), x: x0 - 34 };
    },
    terrain: function (r) {
      var d = "M0 180L0 " + G, pts = [];
      for (var x = 0; x <= 320; x += 16) { var y = G - (x > 130 && x < 160 ? 2 : r() * 14); pts.push([x, y]); d += "L" + x + " " + f(y); }
      d += "L320 180Z";
      var rocks = "";
      for (var i = 0; i < 5; i++) rocks += '<ellipse cx="' + f(20 + r() * 280) + '" cy="' + f(G + 10 + r() * 20) + '" rx="' + f(5 + r() * 8) + '" ry="4" fill="' + C + '" fill-opacity=".22"/>';
      return { back: '<path d="' + d + '" fill="' + C + '" fill-opacity=".14"/>' + rocks, x: 145, g: G - 2 };
    },
    stones: function (r) {
      var out = rect(0, G, 320, 34, 0, 0.08);
      [36, 92, 148, 204, 262].forEach(function (x) { out += '<ellipse cx="' + f(x + (r() - 0.5) * 10) + '" cy="' + G + '" rx="19" ry="6" fill="' + C + '" fill-opacity=".3"/>'; });
      return { back: out, x: 148 };
    },
    nav: function (r) {
      var ex = 258 + r() * 20, ey = 112 + r() * 16;
      var path = '<path d="M108 ' + (G - 4) + "C170 " + (G + 4) + " 200 " + f(ey + 22) + " " + f(ex) + " " + f(ey + 2) +
        '" fill="none" stroke="' + C + '" stroke-width="3" stroke-dasharray="2 9" stroke-linecap="round" opacity=".7"/>';
      var arcs = ring(78, G - 66, 30, 2, 0.25, "3 6") + ring(78, G - 66, 48, 2, 0.15, "3 6");
      return { back: ground(0.25) + arcs + path + pin(ex, ey, 0.9), x: 78 };
    },
    map: function (r) {
      var out = "", rooms = [[40, 40, 120, 90], [168, 40, 110, 60], [168, 108, 110, 30]];
      rooms.forEach(function (rm) {
        for (var i = 0; i < 26; i++) {
          var t = r(), side = Math.floor(r() * 4), x, y;
          if (side === 0) { x = rm[0] + t * rm[2]; y = rm[1]; } else if (side === 1) { x = rm[0] + t * rm[2]; y = rm[1] + rm[3]; }
          else if (side === 2) { x = rm[0]; y = rm[1] + t * rm[3]; } else { x = rm[0] + rm[2]; y = rm[1] + t * rm[3]; }
          out += circ(x + (r() - 0.5) * 3, y + (r() - 0.5) * 3, 1.7, 0.55);
        }
      });
      out += '<path d="M80 130C110 100 150 120 200 70" fill="none" stroke="' + C + '" stroke-width="2.5" stroke-dasharray="2 7" stroke-linecap="round" opacity=".6"/>';
      return { back: out, x: 72, g: 150, s: 0.55, noGround: true };
    },
    gps: function (r) {
      var sx = 262, sy = 34;
      var sat = rect(sx - 8, sy - 7, 16, 14, 3) + rect(sx - 30, sy - 4, 18, 8, 1, 0.55) + rect(sx + 12, sy - 4, 18, 8, 1, 0.55);
      var sig = "";
      for (var i = 0; i < 3; i++) sig += line(sx - 6 - i * 7, sy + 12 + i * 6, sx - 22 - i * 22, sy + 34 + i * 16, 2, 0.35);
      return { back: ground() + sat + sig + pin(210, G - 4, 0.8), x: 110 };
    },
    teleop: function () {
      var vr = rect(28, 52, 64, 34, 13, 0.85) + circ(48, 69, 8, null, HL) + circ(72, 69, 8, null, HL) + rect(18, 62, 12, 14, 4, 0.4) + rect(90, 62, 12, 14, 4, 0.4);
      var waves = "";
      for (var i = 0; i < 3; i++) waves += '<path d="M' + (118 + i * 14) + " 56q10 13 0 26" + '" stroke="' + C + '" stroke-width="3" fill="none" stroke-linecap="round" opacity="' + (0.6 - i * 0.15) + '"/>';
      return { back: ground() + vr + waves, x: 228, reach: true };
    },
    carry: function () { return { back: ground(), x: 98, twin: 226, reach: true }; },
    dataset: function () {
      var out = "";
      for (var i = 2; i >= 0; i--) {
        var x = 176 + i * 16, y = 38 + i * 14;
        out += rect(x, y, 96, 62, 6, 0.16 + (2 - i) * 0.12) + '<rect x="' + x + '" y="' + y + '" width="96" height="62" rx="6" fill="none" stroke="' + C + '" stroke-width="2" opacity=".45"/>';
      }
      out += '<path d="M218 61l22 13-22 13z" fill="' + C + '" opacity=".75"/>';
      for (var j = 0; j < 6; j++) out += rect(180 + j * 15, 106, 8, 5, 1.5, 0.35);
      return { back: ground() + out, x: 92 };
    },
    voice: function () {
      var out = '<path d="M168 40h96a12 12 0 0 1 12 12v26a12 12 0 0 1-12 12h-62l-16 14v-14h-18a12 12 0 0 1-12-12v-26a12 12 0 0 1 12-12z" fill="' + C + '" fill-opacity=".18"/>';
      for (var i = 0; i < 9; i++) { var h = 6 + Math.abs(Math.sin(i * 1.3)) * 22; out += line(180 + i * 9, 65 - h / 2, 180 + i * 9, 65 + h / 2, 4, 0.7); }
      return { back: ground() + out, x: 110 };
    },
    language: function (r) {
      var out = '<path d="M176 34h108a12 12 0 0 1 12 12v32a12 12 0 0 1-12 12h-70l-16 14v-14h-22a12 12 0 0 1-12-12v-32a12 12 0 0 1 12-12z" fill="' + C + '" fill-opacity=".18"/>';
      [0, 1, 2].forEach(function (i) { out += line(184, 50 + i * 13, 184 + 60 + r() * 34, 50 + i * 13, 5, 0.55); });
      var tokens = "";
      for (var j = 0; j < 5; j++) tokens += rect(170 + j * 26, 118, 20, 12, 4, 0.22 + 0.1 * (j % 3));
      return { back: ground() + out + tokens, x: 100, reach: true };
    },
    manip: function (r) {
      var t = rect(176, G - 50, 124, 8, 3, 0.55) + line(186, G - 42, 186, G, 4, 0.45) + line(290, G - 42, 290, G, 4, 0.45);
      t += rect(206 + r() * 10, G - 70, 22, 20, 3, 0.75) + rect(246, G - 76, 14, 26, 6, 0.4) + circ(276, G - 56, 6, 0.6);
      return { back: ground() + t, x: 140, reach: true, gripper: true };
    },
    dance: function (r) {
      var notes = "";
      for (var i = 0; i < 4; i++) {
        var x = 190 + i * 26 + r() * 8, y = 44 + (i % 2) * 20 + r() * 10;
        notes += circ(x, y + 18, 6, 0.6) + line(x + 5, y + 18, x + 5, y, 3, 0.6) + (i % 2 ? line(x + 5, y, x + 14, y + 4, 3, 0.6) : "");
      }
      var arcs = '<path d="M60 70q60 -40 120 0" fill="none" stroke="' + C + '" stroke-width="2.5" stroke-dasharray="1 7" stroke-linecap="round" opacity=".55"/>';
      return { back: ground() + notes + arcs, x: 128, ghost: [-36, -18], step: 14 };
    },
    motion: function () {
      var arcs = '<path d="M40 100q30 -50 70 -50" fill="none" stroke="' + C + '" stroke-width="2.5" stroke-dasharray="1 7" stroke-linecap="round" opacity=".45"/>';
      return { back: ground() + arcs, x: 168, ghost: [-64, -32], step: 12 };
    },
    mpc: function () {
      var out = "";
      for (var i = 0; i < 5; i++) out += rect(140 + i * 30, G - 3 + (i % 2) * 7, 16, 6, 3, 0.4 - i * 0.05);
      var d = "M100 " + (G - 70);
      for (var j = 1; j <= 6; j++) d += "Q" + (100 + j * 30 - 15) + " " + (G - 78) + " " + (100 + j * 30) + " " + (G - 70);
      out += '<path d="' + d + '" fill="none" stroke="' + C + '" stroke-width="2" opacity=".5"/>';
      for (var k = 1; k <= 6; k++) out += circ(100 + k * 30, G - 70, 3, 0.65);
      return { back: ground() + out, x: 96 };
    },
    camera: function () {
      var board = "";
      for (var i = 0; i < 5; i++) for (var j = 0; j < 4; j++) if ((i + j) % 2 === 0) board += rect(200 + i * 16, 36 + j * 16, 16, 16, 0, 0.55);
      board = '<rect x="200" y="36" width="80" height="64" fill="none" stroke="' + C + '" stroke-width="2" opacity=".5"/>' + board;
      var cam = rect(40, 46, 46, 30, 6, 0.8) + rect(52, 40, 18, 8, 2, 0.8) + circ(63, 61, 9, null, HL) + circ(63, 61, 5, 0.8);
      return { back: ground() + board + cam + line(92, 61, 194, 68, 2, 0.3), x: 140 };
    },
    gui: function (r) {
      var out = win(178, 30, 120, 96);
      for (var i = 0; i < 4; i++) { var y = 60 + i * 16, k = 196 + r() * 80; out += line(192, y, 284, y, 4, 0.3) + circ(k, y, 5.5, 0.8); }
      return { back: ground() + out, x: 100 };
    },
    docker: function () {
      var out = "";
      [[186, 88], [236, 88], [211, 52]].forEach(function (p) {
        out += rect(p[0], p[1], 46, 32, 4, 0.3) + '<rect x="' + p[0] + '" y="' + p[1] + '" width="46" height="32" rx="4" fill="none" stroke="' + C + '" stroke-width="2" opacity=".55"/>';
        for (var i = 1; i < 5; i++) out += line(p[0] + i * 9.2, p[1] + 6, p[0] + i * 9.2, p[1] + 26, 2, 0.4);
      });
      return { back: ground() + out, x: 100 };
    },
    code: function (r) {
      var out = win(170, 30, 132, 92) + '<path d="M184 62l10 8-10 8" fill="none" stroke="' + C + '" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>';
      for (var i = 0; i < 3; i++) out += line(202, 70 + (i - 1) * 16 + 8, 202 + 30 + r() * 56, 70 + (i - 1) * 16 + 8, 4.5, 0.45);
      return { back: ground() + out, x: 100 };
    },
    bridge: function () {
      var out = rect(172, 44, 40, 40, 10, 0.3) + rect(256, 84, 40, 40, 10, 0.3) + rect(256, 20, 40, 40, 10, 0.3);
      out += line(212, 64, 256, 40, 3, 0.55) + line(212, 64, 256, 104, 3, 0.55) + circ(192, 64, 7, 0.8) + circ(276, 40, 7, 0.8) + circ(276, 104, 7, 0.8);
      return { back: ground() + out, x: 100 };
    },
    sim: function (r) {
      var axes = line(272, 52, 296, 52, 3, 0.7) + line(272, 52, 272, 28, 3, 0.7) + line(272, 52, 258, 64, 3, 0.7);
      return { back: grid(r, 0.2) + axes, x: 160, noGround: true };
    },
    rl: function (r) {
      var curve = "M196 70", y = 70;
      for (var i = 1; i <= 10; i++) { y = 70 - 46 * (1 - Math.exp(-i / 3)) + (r() - 0.5) * 6; curve += "L" + (196 + i * 9) + " " + f(y); }
      var chart = '<path d="M192 22v52h100" fill="none" stroke="' + C + '" stroke-width="2" opacity=".4"/>' +
        '<path d="' + curve + '" fill="none" stroke="' + C + '" stroke-width="3" stroke-linejoin="round" opacity=".8"/>';
      return { back: grid(r, 0.16) + chart, x: 124, ghost: [-58, 58], ghostScale: 0.62, ghostY: -14, noGround: true };
    },
    edu: function () {
      var book = '<path d="M180 64q30 -12 54 4v58q-24 -16 -54 -4z" fill="' + C + '" fill-opacity=".3"/><path d="M288 64q-30 -12 -54 4v58q24 -16 54 -4z" fill="' + C + '" fill-opacity=".45"/>';
      var cap = '<path d="M234 22l38 14-38 14-38-14z" fill="' + C + '"/>' + line(266, 38, 266, 54, 2.5, 0.8) + circ(266, 56, 3);
      return { back: ground() + book + cap, x: 100 };
    },
    trophy: function () {
      var out = rect(196, 112, 96, 34, 3, 0.25) + rect(216, 96, 56, 16, 3, 0.35);
      out += '<path d="M226 34h36v14a18 18 0 0 1-36 0z" fill="' + C + '"/>' + rect(239, 66, 10, 14, 2) + rect(232, 80, 24, 8, 2);
      out += '<path d="M226 38h-8a10 10 0 0 0 10 14M262 38h8a10 10 0 0 1-10 14" fill="none" stroke="' + C + '" stroke-width="3"/>';
      out += line(176, 30, 176, 60, 2.5, 0.6) + '<path d="M176 30l18 6-18 6z" fill="' + C + '" opacity=".7"/>';
      return { back: ground() + out, x: 120 };
    },
    award: function () {
      var out = '<path d="M228 26l12 30M264 26l-12 30" stroke="' + C + '" stroke-width="10" opacity=".4"/>' + circ(246, 74, 24) + circ(246, 74, 15, null, HL);
      out += '<path d="M246 64l3 7h7l-6 4 2 7-6-4-6 4 2-7-6-4h7z" fill="' + C + '"/>';
      return { back: ground() + out, x: 120 };
    },
    stage: function (r) {
      var out = '<path d="M110 0L150 0L190 ' + (G - 4) + 'L70 ' + (G - 4) + 'z" fill="' + C + '" fill-opacity=".1"/>' +
        '<path d="M240 0L262 0L210 ' + (G - 4) + 'L150 ' + (G - 4) + 'z" fill="' + C + '" fill-opacity=".07"/>';
      out += rect(40, G - 4, 240, 8, 2, 0.35);
      for (var i = 0; i < 14; i++) out += circ(24 + i * 21 + r() * 4, 168 + r() * 4, 6, 0.22);
      return { back: out, x: 130, g: G - 4, twinMaybe: 190, noGround: true };
    },
    partner: function () {
      var b1 = rect(52, 60, 70, 86, 4, 0.25), b2 = rect(198, 44, 70, 102, 4, 0.35), win2 = "";
      for (var i = 0; i < 3; i++) for (var j = 0; j < 4; j++) { win2 += rect(62 + i * 20, 72 + j * 18, 10, 10, 1, 0.5); win2 += rect(208 + i * 20, 58 + j * 20, 10, 12, 1, 0.5); }
      var link = line(124, 96, 196, 96, 5, 0.7) + ring(150, 96, 9, 4, 0.9) + ring(170, 96, 9, 4, 0.9);
      return { back: ground() + b1 + b2 + win2 + link, x: 160, s: 0.5 };
    },
    globe: function () {
      var g = circ(212, 78, 50, 0.16) + ring(212, 78, 50, 2.5, 0.6) + '<ellipse cx="212" cy="78" rx="22" ry="50" fill="none" stroke="' + C + '" stroke-width="2" opacity=".5"/>' +
        line(162, 78, 262, 78, 2, 0.5) + '<path d="M170 52h84M170 104h84" stroke="' + C + '" stroke-width="2" opacity=".35"/>';
      return { back: ground() + g + pin(232, 64, 0.85), x: 90 };
    },
    factory: function () {
      var out = '<path d="M150 ' + G + 'V86l30 18V86l30 18V86l30 18V56h18v' + (G - 56) + 'z" fill="' + C + '" fill-opacity=".2"/>';
      out += rect(270, 112, 30, 34, 2, 0.35) + rect(276, 90, 24, 22, 2, 0.25);
      return { back: ground() + out, x: 96 };
    }
  };

  // Scene from the description, then from the section. Order matters: the first match wins.
  var RULES = [
    ["stairs", /stair|step up|climb/], ["stones", /stepping stone/],
    ["gps", /gnss|\bgps\b|\brtk\b/], ["map", /lidar|odometry|slam|point cloud|\blio\b|multi-floor|occupancy/],
    ["terrain", /terrain|parkour|\brough\b|uneven|slope/],
    ["nav", /navigat|nav2|waypoint|planner|route|\bpath\b|pathfinding/],
    ["bridge", /bridge|websocket|\bdds\b|\bmcp\b|drivers?\b/],
    ["dataset", /dataset|episodes|data pipeline/],
    ["teleop", /teleop|\bvr\b|quest|pico/], ["carry", /carry|cooperative|transport/],
    ["dataset", /data collection|recording|recorded|replay|lerobot/],
    ["voice", /voice|dialogue|speech/], ["language", /\bvla\b|language|\bvlm\b|gr00t|pi0|world-action|fluxvla|openpi|agents?\b/],
    ["manip", /grasp|pick|manipulat|\barms?\b|\bhands?\b(?!-)|gripper|garment|bottle|bimanual|pedipulat|object/],
    ["dance", /dance|music|conduct/], ["motion", /retarget|motion tracking|whole-body tracking|mimic|imitation|\bmotions?\b|beyondmimic|sonic/],
    ["mpc", /\bmpc\b|lqr|riccati|sliding mode|pendulum|gait plan|\bwbc\b|estimator|stand-still|foothold|closed-loop|tracking error/],
    ["camera", /calibrat|camera|depth/], ["gui", /\bgui\b|panel|\bweb\b|workbench|measure|browse/],
    ["docker", /docker|container/], ["code", /\bros\b|ros 2|sdk|deploy|controller|description|urdf|model files/],
    ["sim", /simulat|mujoco|isaac|gazebo|unity|newton|\bsim\b/], ["rl", /\brl\b|reinforcement|ppo|policy|policies|training|\btrain/],
    ["edu", /course|tutorial|camp|lesson|notes|teaching|college|guide|learning log|template/],
    ["trophy", /challenge|competition|robocup|championship|\bcup\b|contest|\bwon\b/]
  ];
  // In Education & competitions, a contest or a course says more than the robot work inside it.
  var EDU_FIRST = [["trophy", /challenge|competition|robocup|championship|\bcup\b|contest|\bwon\b/],
                   ["edu", /course|tutorial|guide|lesson|teaching|college|learning log|study notes|template/]];
  var INDUSTRY = { 0: "factory", 1: null, 2: "stage", 3: "partner", 4: "globe", 5: "award" };
  var SECTION = ["rl", "nav", "manip", "language", "code", "edu", "code"];

  function pickScene(item, text, D) {
    if (item.section === 6) { // industry: the sub-section says more than the words
      var subs = [], en = D.items.filter(function (x) { return x.section === 6; });
      en.forEach(function (x) { if (subs.indexOf(x.t.en.sub) < 0) subs.push(x.t.en.sub); });
      var s = INDUSTRY[subs.indexOf(item.t.en.sub)];
      if (s) return s;
    }
    var rules = item.section === 5 ? EDU_FIRST.concat(RULES) : RULES;
    for (var i = 0; i < rules.length; i++) if (rules[i][1].test(text)) return rules[i][0];
    return SECTION[item.section] || "sim";
  }

  // One robot alone, standing at x = 160 on the ground line; used by scripts/og_cover.html.
  window.illustrateRobot = function (name, foot) {
    return '<svg viewBox="0 0 320 180" aria-hidden="true">' + drawRobot({ name: name, foot: foot || "point" }, 160, G, 1, 6, false) + "</svg>";
  };

  window.illustrate = function (item, D) {
    var e = item.t.en, text = (e.name + " " + e.desc).replace(/<[^>]+>/g, " ").toLowerCase();
    var r = rng(item.id), kind = robotKind(item, text), key = pickScene(item, text, D), sc = SCENES[key](r);
    var g = sc.g || G, step = sc.step != null ? sc.step : 5 + r() * 8;
    // Tall robots are drawn a little smaller so their heads stay clear of the label in the corner.
    var s = (sc.s || 1) * (kind ? ({ TRON2: 0.82, Oli: 0.86, Luna: 0.9 }[kind.name] || 1) : 1);
    var out = sc.back || "";
    if (kind) {
      (sc.ghost || []).forEach(function (dx, i) {
        var gs = s * (sc.ghostScale || 1);
        out += '<g opacity="' + (sc.ghostScale ? 0.28 : 0.16 + i * 0.12) + '">' + drawRobot(kind, sc.x + dx, g + (sc.ghostY || 0), gs, step * (i % 2 ? -1 : 1), false) + "</g>";
      });
      out += drawRobot(kind, sc.x, g, s, step, sc.reach && hasArms(kind));
      if (sc.twin) out += drawRobot(kind, sc.twin, g, s, -step, sc.reach && hasArms(kind));
      if (key === "carry") { // the load between them, at the height each robot can hold it
        var by = { TRON1: 98, P1: 106, W1: 70, TRON2: 95, Oli: 76, Luna: 72 }[kind.name] || 96;
        out += rect(sc.x + 16 * s, g - by * s, sc.twin - sc.x - 32 * s, 8, 3, 0.75);
      }
      if (sc.gripper && !hasArms(kind)) out += line(232, 26, 232, 52, 4, 0.6) + line(232, 52, 224, 62, 4, 0.6) + line(232, 52, 240, 62, 4, 0.6);
      if (item.robots.length > 1 && !sc.twin && key !== "rl") { // a second robot in the entry: show it small at the back
        var k2 = robotKind({ robots: [item.robots[1]] }, text);
        out += '<g opacity=".38">' + drawRobot(k2, sc.x + (sc.x > 160 ? -78 : 78) * s, g - 6, s * 0.62, -step, false) + "</g>";
      }
    }
    return '<svg class="illus" viewBox="0 0 320 180" preserveAspectRatio="xMidYMid slice" aria-hidden="true" data-scene="' + key + '">' + out + "</svg>";
  };
})();
