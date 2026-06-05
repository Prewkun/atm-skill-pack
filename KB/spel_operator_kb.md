# EPSON SPEL+ Operator Command Reference

# ATCLR Statement
**Type:** statement | **Section:** Operator

## Syntax
```
ATCLR
  [j1], [j2], [j3], [j4], [j5], [j6], [j7], [j8], [j9]
```

## Parameters
j1
		 - j9	Integer expression
		 representing the joint number.  If no parameters are supplied,
		 then the average torque values are cleared for all joints.

The additional
		 S axis is 8 and T axis is 9. If non-existent joint number is supplied,
		 an error occurs.

## Description
ATCLR clears the average torque values for the specified joints.

You must execute ATCLR before executing ATRQ.

## Examples
```spel
> atclr
```

```spel
> go p1
```

```spel
> atrq 1
```

```spel
0.028
```

```spel
> atrq
```

```spel
0.028    0.008
```

```spel
0.029    0.009
```

```spel
0.000    0.000
```

```spel
> atclr 4, 1, 5
```

```spel
> go p1
```

```spel
> ptrq 1
```

```spel
0.227
```

```spel
> ptrq 4
```

```spel
0.083
```

## See Also
Clears and intializes the average torque for one or more joints.

ATRQ

PTRQ

ATCLR Statement


---

# ATRQ Function
**Type:** function | **Section:** Operator

## Syntax
```
ATRQ(jointNumber)
```

## Parameters
jointNumber	Integer expression
		 representing the joint number.

The additional
		 S axis is 8 and T axis is 9.

## Description
The ATRQ function returns the average RMS (root-mean-square) torque of the specified joint.  The loading state of the motor can be obtained by this instruction.
  The result is a real value from 0 to 1 with 1 being maximum average torque.

You must execute ATCLR before this function is executed.

This instruction is time restricted.  You must execute ATRQ within 60 seconds after ATCLR is executed.  When this time is exceeded, error 4030 occurs.

## Examples
```spel
Function CheckAvgTorque Integer i Go P1 ATCLR Go P2 Print "Average torques:" For i = 1 To 4
    Print "Joint ", i, " = ", ATRQ(i) Next i
Fend
```

## See Also
Returns the average torque for the specified joint.

ATCLR

ATRQ Statement

PTCLR

PTRQ

ATRQ Function Example

This example uses the ATRQ function in a program:

Function CheckAvgTorque

  Integer i

  Go P1

  ATCLR

  Go P2

  Print "Average torques:"

  For i = 1 To 4

    Print "Joint ", i, " = ", ATRQ(i)

  Next i

Fend


---

# ATRQ Keyword
**Type:** reference | **Section:** Operator

## Description
ATRQ Keyword

ATRQ Keyword

The ATRQ keyword is used in these contexts:

ATRQ Statement

ATRQ Function


---

# ATRQ Statement
**Type:** statement | **Section:** Operator

## Syntax
```
ATRQ  [jointNumber]
```

## Parameters
jointNumber	Optional.
		  Integer expression representing the joint number.

The additional
		 S axis is 8 and T axis is 9.

## Description
ATRQ displays the average RMS (root-mean-square) torque of the specified joint.  The loading state of the motor can be obtained by this instruction.  The result is a real value from 0 to 1 with 1 being maximum average torque.

You must execute ATCLR before this command is executed.

This instruction is time restricted.  You must execute ATRQ within 60 seconds after ATCLR is executed.  When this time is exceeded, error 4030 occurs.

## Examples
```spel
> atclr
```

```spel
> go p1
```

```spel
> atrq 1
```

```spel
0.028
```

```spel
> atrq
```

```spel
0.028    0.008
```

```spel
0.029    0.009
```

```spel
0.000    0.000
```

## See Also
Displays the average torque for the specified joint.

ATCLR

ATRQ Function

PTRQ

ATRQ Statement Example

> atclr

> go p1

> atrq 1

   0.028

> atrq

0.028    0.008

   0.029    0.009

   0.000    0.000


---

# ATan Function
**Type:** reference | **Section:** Operator

## Syntax
```
Atan( number )
```

## Parameters
number	Numeric expression
		 representing the tangent of an angular value.

## Description
Atan returns the arctangent of the numeric expression.  The numeric expression (number) may be any numeric value. The value returned by Atan will range from -PI to PI radians.

To convert from radians to degrees, use the RadToDeg function.

## Examples
```spel
Function atantest Real x, y x = 0 y = 1 Print "Atan of ", x, " is ", Atan(x) Print "Atan of ", y, " is ", Atan(y)
Fend
```

## See Also
Abs, Val , Tan, Sin, Sgn, RadToDeg, DegToRad , Cos, Atan2 , Asin, Acos

Atan Function Example

The following example shows a simple program which uses Atan.

Function atantest

  Real x, y

  x = 0

  y = 1

  Print "Atan of ", x, " is ", Atan(x)

  Print "Atan of ", y, " is ", Atan(y)

Fend


---

# ATan2 Function
**Type:** reference | **Section:** Operator

## Syntax
```
Atan2
			(X, Y)
```

## Parameters
X	Numeric expression representing the X coordinate.

Y	Numeric expression representing the Y coordinate.

## Description
Atan2(X, Y) returns the angle of the line which connects points (0, 0) and (X, Y). This trigonometric function returns an arc tangent angle in all four quadrants.

## Examples
```spel
Function at2test
		  Real x, y
		  Print "Please enter a number for the X Coordinate:"
		  Input x
		  Print "Please enter a number for the Y Coordinate:"
		  Input y
		  Print "Atan2 of ", x, ", ", y, " is ", Atan2(x, y)
		Fend
```

## See Also
Abs, Acos, Asin, Atan, Cos, DegToRad, RadToDeg, Sgn, Sin, Tan, Val

Atan2 Function Example

The following example shows a simple program which uses Atan2.

Function at2test

		  Real x, y

		  Print "Please enter a number for the X Coordinate:"

		  Input x

		  Print "Please enter a number for the Y Coordinate:"

		  Input y

		  Print "Atan2 of ", x, ", ", y, " is ", Atan2(x, y)

		Fend


---

# Abs Function
**Type:** reference | **Section:** Operator

## Syntax
```
Abs(number)
```

## Parameters
number	Any valid
		 numeric expression.

## Description
The absolute value of a number is its unsigned magnitude.  For example, Abs(-1) and Abs(1) both return 1.

## Examples
```spel
> print abs(1)
```

```spel
1
```

```spel
> print abs(-1)
```

```spel
1
```

```spel
> print abs(-3.54)
```

```spel
3.54
```

```spel
>
```

## See Also
Atan	Sgn

Atan2	Sin

Cos	Sqr

Int	Str$

Mod	Tan

Not	Val

Abs Function Example

The following examples are done from the command window using the Print instruction.

> print abs(1)

1

> print abs(-1)

1

> print abs(-3.54)

3.54

>


---

# Accel Function
**Type:** function | **Section:** Operator

## Syntax
```
Accel(paramNumber)
```

## Parameters
paramNumber	Integer expression
		 which can have the following values:

1: acceleration
		 specification value

2: deceleration
		 specification value

3: depart
		 acceleration specification value of Z joint for Jump

4: depart
		 deceleration specification value of Z joint for Jump

5: approach
		 acceleration specification value of Z joint for Jump

6: approach
		 deceleration specification value of Z joint for Jump

Return Values

Integer 1% or more

## Description
Accel Function

Accel Function

See_Also     Example

Returns specified acceleration value.

## Examples
```spel
Function acceltest Integer currAccel, currDecel ' Get current accel and decel currAccel = Accel(1) currDecel = Accel(2) Accel 50, 50 Jump pick ' Retore previous settings Accel currAccel, currDecel
Fend
```

## See Also
Accel Statement

Accel Function Example

This example uses the Accel function in a program:

Function acceltest

  Integer currAccel, currDecel

  ' Get current accel and decel

  currAccel = Accel(1)

  currDecel = Accel(2)

  Accel 50, 50

  Jump pick

  ' Retore previous settings

  Accel currAccel, currDecel

Fend


---

# Accel Keyword
**Type:** reference | **Section:** Operator

## Description
Accel Keyword

Accel Keyword

The Accel keyword is used in these contexts:

Accel Statement

Accel Function


---

# Accel Statement
**Type:** statement | **Section:** Operator

## Syntax
```
(1) Accel accel, decel [, departAccel, departDecel, approAccel, approDecel]

(2) Accel
```

## Parameters
accel	Integer
		 expression 1 or more representing a percentage of maximum acceleration
		 rate.

decel	Integer
		 expression 1 or more representing a percentage of the maximum
		 deceleration rate.

departAccel	Depart
		 acceleration for Jump.  Valid Entries are 1 or more.

		Optional. Available only with Jump command.

departDecel	Depart deceleration
		 for Jump.  Valid Entries are 1 or more.

		Optional. Available only with Jump command.

approAccel	Approach
		 acceleration for Jump.  Valid Entries are 1 or more.

		Optional. Available only with Jump command.

approDecel	Approach deceleration
		 for Jump.  Valid Entries are 1 or more.

		Optional. Available only with Jump command.

## Description
Accel specifies the acceleration and deceleration for all Point to Point type motions.  This includes motion caused by the Go, Jump and Pulse robot motion instructions.

Each acceleration and deceleration parameter defined by the Accel instruction may be an integer value 1 or more.  This number represents a percentage of the maximum acceleration (or deceleration) allowed. Usually, the maximum value is 100. However, some robots allow setting larger than 100. Use AccelMax function to get the maximum value available for Accel.

The Accel instruction can be used to set new acceleration and deceleration values or simply to print the current values.  When the Accel instruction is used to set new accel and decel values, the first 2 parameters (accel and decel ) in the Accel instruction are required.

The optional departAccel, departDecel, approAccel, and approDecel parameters are effective for the Jump instruction only and specify acceleration and deceleration values for the depart motion at the beginning of Jump and the approach motion at the end of Jump.

The Accel value initializes to the default values (low acceleration) when any one of the following conditions occurs:

Controller
			 Startup

			Motor On

			SFree, SLock, Brake

			Reset, Reset Error

			Stop button or Quit All stops tasks

## Notes
Executing the Accel command in Low Power Mode (Power Low)

If Accel is executed when the robot is in low power mode (Power Low), the new values are stored, but the current values are limited to low values.

The current acceleration values are in effect when Power is set to High (Power High), and Teach mode is OFF.

Accel vs. AccelS

It is important to note that the Accel instruction does not set the acceleration and deceleration rates for straight line and arc motion.  The AccelS instruction is used to set the acceleration and deceleration rates for the straight line and arc type moves.

Accel setting larger than 100

Usually, the maximum value is 100. However, some robots allow setting larger than 100. In general use, Accel setting 100 is the optimum setting that maintains the balance of acceleration and vibration when positioning. However, you may require a operation with shorter cycle time by increasing the acceleration even with large vibration. In this case, set the Accel to larger than 100. Except in some operation conditions, the cycle time may not change by setting Accel to larger than 100.

## Examples
```spel
Function acctest Integer slow, accslow, decslow, fast, accfast, decfast slow = 20 'set slow speed variable fast = 100   'set high speed variable accslow = 20 'set slow acceleration variable decslow = 20 'set slow deceleration variable accfast = 100 'set fast acceleration variable decfast = 100 'set fast deceleration variable Accel accslow, decslow Speed slow Jump pick On gripper Accel accfast, decfast Speed fast Jump place
Fend
```

```spel
>accel 100,100,100,100,100,35
```

```spel
>accel
```

```spel
100 100
```

```spel
100 100
```

```spel
100 35
```

```spel
>
```

## See Also
AccelR, AccelS, Go, Jump, Jump3, Power, Pulse, Speed, TGo

Accel Statement Example

The following example shows a simple motion program where the acceleration (Accel) and speed (Speed) is set using predefined variables.

[Example 1]

Function acctest

  Integer slow, accslow, decslow, fast, accfast, decfast

slow = 20 'set slow speed variable

  fast = 100   'set high speed variable

  accslow = 20 'set slow acceleration variable

  decslow = 20 'set slow deceleration variable

  accfast = 100 'set fast acceleration variable

  decfast = 100 'set fast deceleration variable

  Accel accslow, decslow

  Speed slow

  Jump pick

  On gripper

  Accel accfast, decfast

  Speed fast

  Jump place

Fend

[Example 2]

Set the Z joint downward deceleration to be slow to allow a gentle placement of the part when using the Jump instruction.  This means we must set the Zdnd parameter low when setting the Accel values.

>accel 100,100,100,100,100,35

>accel

100 100

100 100

100 35

>


---

# AccelR Function
**Type:** reference | **Section:** Operator

## Syntax
```
AccelR(paramNumber)
```

## Parameters
paramNumber	Integer expression which can have the
		 following values:

1: acceleration
		 specification value

2: deceleration
		 specification value

## Description
AccelR Function

AccelR Function

## Examples
```spel
Real currAccelR, currDecelR
' Get current accel and decel
currAccelR = AccelR(1)
currDecelR = AccelR(2)
```

## See Also
Returns specified tool rotation acceleration value.

AccelR Statement

AccelR Function


---

# AccelR Keyword
**Type:** reference | **Section:** Operator

## Description
AccelR Keyword

AccelR Keyword

The AccelR keyword is used in these contexts:

AccelR Statement

AccelR Function


---

# AccelR Statement
**Type:** statement | **Section:** Operator

## Syntax
```
(1) AccelR accel , [ decel ]

(2) AccelR
```

## Parameters
accel	Real
		 expression in degrees / second2.

decel	Real
		 expression in degrees / second2.

Valid entries range of the parameters

accel
		 / decel (deg/sec2)

VT
		 series	0.1
		 to 1000

C
		 series, N series, T series,
		 G series, GX series, RS series,

LS-B
		 series	0.1
		 to 5000

## Description
AccelR is effective when the ROT modifier is used in the Move, Arc, Arc3, BMove, TMove, and Jump3CP motion commands.

The AccelR value initializes to the default values when any one of the following conditions occurs:

Controller Startup

		Motor On

		SFree, SLock, Brake

		Reset, Reset Error

		Stop button or Quit All stops tasks

## Examples
```spel
AccelR 360, 200
```

## See Also
Sets or displays the acceleration and deceleration values for tool rotation control of CP motion.

Arc, Arc3, BMove, Jump3CP, Power, SpeedR, TMove

AccelR Statement


---

# AccelS Function
**Type:** function | **Section:** Operator

## Syntax
```
AccelS(paramNumber)
```

## Parameters
paramNumber	Integer expression which can have the
		 following values:

1: acceleration value

2: deceleration
		 vvalue

3: depart acceleration
		 value for Jump3, Jump3CP

4: depart deceleration
		 value for Jump3, Jump3CP

5: approach
		 acceleration value for Jump3, Jump3CP

6: approach
		 deceleration value for Jump3, Jump3CP

7: acceleration
		 value adjusted by hand weight

8: deceleration
		 value adjusted by hand weight

9: depart acceleration
		 value for Jump3, Jump3CP adjusted by hand weight

10: depart deceleration
		 value for Jump3, Jump3CP adjusted by hand weight

11: approach
		 acceleration value for Jump3, Jump3CP adjusted by hand weight

12: approach
		 deceleration value for Jump3, Jump3CP adjusted by hand weight

## Description
AccelS Function

AccelS Function

See_Also Example

Returns acceleration or deceleration for straight line motion commands.

## Examples
```spel
Real savAccelS

savAccelS = AccelS(1)
```

## See Also
AccelS Statement

Arc3

SpeedS

Jump3

Jump3CP

AccelS Function


---

# AccelS Keyword
**Type:** reference | **Section:** Operator

## Description
AccelS Keyword

AccelS Keyword

The AccelS keyword is used in these contexts:

AccelS Statement

AccelS Function


---

# AccelS Statement
**Type:** statement | **Section:** Operator

## Syntax
```
(1) AccelS accel [, decel ] [, departAccel ], [ departDecel ], [ approAccel ], [ approDecel ]

(2) AccelS
```

## Parameters
accel	Real
		 expression represented in mm/sec2
		  units to define acceleration and deceleration values for
		 straight line and continuous path motion. If decel
		 is omitted, then accel
		 is used to specify both the acceleration and deceleration rates.

decel	Optional.
		  Real expression represented in mm/sec2
		 units to define the deceleration value.

departAccel	Optional.
		 Real expression for depart acceleration value for Jump3, Jump3CP.

departDecel	Optional.
		 Real expression for depart deceleration value for Jump3, Jump3CP.

approAccel	Optional.
		 Real expression for approach acceleration value for Jump3, Jump3CP.

approDecel	Optional.
		 Real expression for approach deceleration value for Jump3, Jump3CP.

When displays Accel and Decel values, displays adjusted Accel and Decel values according to the currently configured hand weight, for each accel, decel, departAccel, departDecel, approAccel, approDecel.

## Description
AccelS specifies the acceleration and deceleration for all interpolated type motions including linear and curved interpolations.  This includes motion caused by the Move and Arc motion instructions.

The AccelS value initializes to the default values when any one of the following conditions occurs:

Controller Startup

		Motor On

		SFree, SLock, Brake

		Reset, Reset Error

		Stop button or Quit All stops tasks

## Notes
Executing the AccelS command in Low Power Mode (Power Low):

If AccelS is executed when the robot is in low power mode (Power Low), the new values are stored, but the current values are limited to low values.

The current acceleration values are in effect when Power is set to High (Power High), and Teach mode is OFF.

Accel vs. AccelS:

It is important to note that the AccelS instruction does not set the acceleration and deceleration rates for point to point type motion. (i.e. motions initiated by the Go, Jump, and Pulse instructions.)  The Accel instruction is used to set the acceleration and deceleration rates for Point to Point type motion.

Upper limit value

The AccelS upper limit value of SCARA robots (including RS series manipulators) varies depending on Weight setting and the position of the spline unit.  For details, refer to the Manipulator manuals (ACCELS Setting for CP Motions).

The AccelS upper limit value of 6-Axis robots varies depending on Weight setting.  For details, refer to the Manipulator manuals (Specifications).

## Examples
```spel
Function acctest Integer slow, accslow, fast, accfast slow = 20 'set slow speed variable fast = 100 'set high speed variable accslow = 200 'set slow acceleration variable accfast = 5000 'set fast acceleration variable AccelS accslow SpeedS slow Move P1 On 1 AccelS accfast SpeedS fast Jump P2
Fend
```

## See Also
Robot motion commands

Accel

Arc

Arc3

Jump3

Jump3CP

Power

Move

SpeedS

AccelS Statement


---

# Acos Function
**Type:** function | **Section:** Operator

## Syntax
```
Acos(number)
```

## Parameters
number	Numeric
		 expression representing the cosine of an angle.

## Description
Acos returns the arccosine of the numeric expression.
  Values range is from -1 to 1.  The value returned by Acos will range from 0 to PI radians.  If number is -1 or 1, an error occurs.

To convert from radians to degrees, use the RadToDeg function

## Examples
```spel
Function acostest Double x x = Cos(DegToRad(30)) Print "Acos of ", x, " is ", Acos(x)
Fend
```

## See Also
Returns the arccosine of a numeric expression.

Abs, Asin, ATan, ATan2, Cos, DegToRad, RadToDeg, Sgn, Sin, Tan, Val

Acos Function Example

Function acostest

  Double x

  x = Cos(DegToRad(30))

  Print "Acos of ", x, " is ", Acos(x)

Fend


---

# Additional Axis
**Type:** reference | **Section:** Operator

## Description
Additional Axis

Additional Axis

Overview

Specification


---

# Additional Axis Overview
**Type:** reference | **Section:** Operator

## Description
Additional Axis Overview

Overview

You can attach up to two drive axes (per manipulator) which can operate in association
with the manipulator. The position data of the additional axis is saved with the robot point
data. The additional axis can move simultaneously with the manipulator by motion
commands and you can realize the application using a traveling axis (manipulator on the
straight axis) with a simple programming.

Note: If you want to operate the manipulator and drive axis separately, you need to define the
additional axis as another manipulator using the multi-manipulators function.

Caution: When you use the additional axis as traveling axis and mount a manipulator(s) on the axis, the
reaction force of manipulator(s) is put on the traveling axis. Therefore, you should limit the
acceleration/deceleration speed with the Accel setting so that it is within the allowable
inertia of traveling axis. In addition, the manipulator may swing widely at the positioning
and possibly break the additional axis.


---

# Additional Axis Specification
**Type:** reference | **Section:** Operator

## Description
Additional Axis Specification

Specification

Types of additional axis

The supported additional axis is PG axis, controlled by the pulse generator board. However, note that the PG axis has some limitation.

Limitation of the PG additional axis

Synchronizes with the manipulator to start operating but it doesn't to finish.
Not support the Path motion with CP On and Pass. Stops for every motion.
Not go through the CVMove series of points
Calibration is necessary using the MCAL command.  Cannot operate the additional axis and the robot together until the calibration is complete.  If movement of the PG additional axis is "0", and Go and Move are executed to the point where only the robot moves, the robot will move singly.

Number of additional axis

Up to two additional axes are available for each of the SCARA robot (including RS series), Cartesian coordinate robot, 6-axis robot (including N series), and Joint type robot. However, the number of axes you can add is decided by how many axes are available with your controller.

Position data management

The additional axes are allocated to Joint #8 and #9 for all robot types the position data are shown in the S and T coordinate values of point data of the manipulator to which you add the additional axes.

The additional axis as Joint #8 is called the additional S axis and Joint #9 is the additional T axis.

The coordinate values of additional axes are saved with the robot point data but don't have any effect on the robot coordinate system.

How to operate

The additional axis can move simultaneously with the manipulator (synchronous start / stop). However, if you use the PG axis, it doesn't synchronize with manipulator to finish and operate by the different acceleration/deceleration speed from the manipulator. See below for the details of motion commands.

Also, you can operate the additional axis and manipulator separately by proper management of the point data. However, you cannot operate separately both of them in arbitrary timing. In this case, use the multi-manipulators function and set the drive axis as another manipulator.

Commands' specification

Pulse, Go, BGo, TGo, Pass

The additional axis can operate in association with the manipulator motion. However, if you use the PG axis, it synchronizes only to start the motion and a motion command completes when both of manipulator and axis finish the each motion. In addition, if the PG additional axis has a travel distance, the Path motion with CP On and Pass are prohibited and the axis moves with CP Off automatically.

Move, BMove, Tmove

The additional axis can operate in association with the manipulator motion. However, if you use the PG axis, it synchronizes only to start the motion and a motion command completes when both of manipulator and axis finish the each motion. In addition, if the PG additional axis has a travel distance, the Path motion with CP On is prohibited and the axis moves with CP Off automatically.

Arc, Arc3

The additional axis can operate in association with the manipulator motion. It doesn't go through the specified midPoint and directly goes to the end point. If you use the PG axis, it synchronizes only to start the motion and a motion command completes when both of manipulator and axis finish the each motion. In addition, if the PG additional axis has a travel distance, the Path motion with CP On is prohibited and the axis moves with CP Off automatically.

CVMove

The additional axis can operate in association with the manipulator motion. If you use the servo axis for the additional axis, for each of the S and T axis it creates a curve going through the S and T coordinates specified by a series of point data. However, if you use the PG axis for the additional axis, it doesn't go through the series of points and directly goes to the end point. Also, it synchronizes only to start the motion and a motion command completes when both of manipulator and axis finish the each motion. In addition, if the PG additional axis has a travel distance, the Path motion with CP On is prohibited and the axis moves with CP Off automatically.

Jump

The additional axis executes PTP motion in association with the manipulator horizontal motion. However, if you use the PG axis, it synchronizes only to start the motion and a motion command completes when both of manipulator and axis finish the each motion. In addition, if the PG additional axis has a travel distance, the Path motion with CP On is prohibited and the axis moves with CP Off automatically.

Jump3, Jump3CP

The additional axis can operate in association with the manipulator depart / span / approach motion. However, if you use the PG axis, it synchronizes only to start the motion and a motion command completes when both of manipulator and axis finish the each motion. In addition, if the PG additional axis has a travel distance, the Path motion with CP On and Pass are prohibited and the axis moves with CP Off automatically.

JTran, PTran

The additional axis can operate separately by specifying as Joint #8, #9.

## Examples
```spel
> JTran 8, 90 'Move the additional S axis by 90 mm
> PTran 9, 10000 'Move the additional T axis by 10000 pulse
```


---

# Additional Axis Usage
**Type:** reference | **Section:** Operator

## Description
Additional Axis Usage

## Examples
```spel
P1 = XY(10, 20, 30, 40) :ST(10, 20)         ' SCARA robot
```

```spel
P1 = XY(10, 20, 30, 40, 50, 60) :ST(10, 20) ' 6-axis robot
```

```spel
Go XY(10, 20, 30, 40) :ST(10, 20)
```

```spel
Go XY(10, 20, 30, 40, 50, 60) :ST(10, 20)
```

```spel
P1 = XY(10, 20, 30, 40) :S(10) :T(20)
```

```spel
P1 = XY(10, 20, 30, 40) :S(10)
```

```spel
P1 = XY(10, 20, 30, 40) :T(20)
```

```spel
P1 = ST(10, 20)
```

```spel
Go P1   ' Only additional axis moves and the manipulator remains at the current position.
```

```spel
Go ST(10, 20) ' Only the additional axis moves.
```

```spel
P1 = XY(10, 20, 30, 40)
```

```spel
Go P1 ' Only the manipulator moves and the additional axis remains at the current position.
```

```spel
Go XY(10, 20, 30, 40) ' Only the manipulator moves.
```

```spel
P1 = XY(10, 20, 30, 40, 50, 60) :ST(10, 20)
```

```spel
P2 = P1 + S(10) + T(20) ' Add the offset amount to the additional ST axes for P1.
```

```spel
P1 = XY(10, 20, 30, 40, 50, 60)
```

```spel
P2 = P1 + S(10) + T(20) ' Error (ST are undefined for P1 and you cannot use the point operator)
```

```spel
P1 = XY(10, 20, 30, 40, 50, 60) +ST(10, 20) ' Error
```

```spel
P1 = XY(10, 20, 30, 40, 50, 60) +S(10) +T(20) ' Error
```

```spel
Go ST(10, 20) + X(10) ' Error (XY are undefined and you cannot use the point operator)
```

```spel
Print CS(P1), CT(P1)
```


---

# Agl Function
**Type:** reference | **Section:** Operator

## Syntax
```
Agl(jointNumber)
```

## Parameters
jointNumber	Integer expression
		 representing the joint number.  Values are from 1 to the
		 number of joints on the robot. The additional S axis is 8 and
		 T axis is 9.

## Description
The Agl function is used to get the joint angle for the selected rotational joint or position for the selected linear joint.

If the selected joint is rotational, Agl returns the current angle, as measured from the selected joint's 0 position, in degrees.  The returned value is a real number.

If the selected joint is a linear joint, Agl returns the current position, as measured from the selected joint's 0 position, in mm.  The returned value is a real number.

If an auxiliary arm is selected with the Arm statement, Agl returns the angle (or position) from the standard arm's 0 pulse position to the selected arm.

## Examples
```spel
> print agl(1), agl(2)

17.234 85.355
```

## See Also
PAgl

Pls

PPls

Agl Function Example

The following examples are done from the command window using the Print instruction.

> print agl(1), agl(2)

17.234 85.355


---

# AglToPls Function
**Type:** function | **Section:** Operator

## Syntax
```
AglToPls(j1, j2, j3, j4, [ j5, j6 ], [ j7 ], [ j8, j9 ] )
```

## Parameters
j1
		 - j6	Real expressions
		 representing joint angles.

j7	Real expression
		 representing the joint #7 angle. For the JOINT type 7-axis robot.

j8	Real expression
		 representing the additional S axis angle.

j9	Real expression
		 representing the additional T axis angle.

## Description
Use AglToPls to create a point from joint angles.

Note

In certain cases, when the result of AglToPls is assigned to a point data variable, the arm moves to a joint position that is different from the joint position specified by AglToPls.

For Example:

P1 = AglToPls(0, 0, 0, 90, 0, 0)

Go P1 ' moves to AglToPls(0, 0, 0, 0, 0, 90) joint position

Similarly, when the AglToPls function is used as a parameter in a CP motion command, the arm may move to a different joint position from the joint position specified by AglToPls.

Move AglToPls(0, 0, 0, 90, 0, 0) ' moves to AglToPls(0, 0, 0, 0, 0, 90) joint position

When using the AglToPls function as a parameter in a PTP motion command, this problem does not occur.

## Examples
```spel
P1 = AglToPls(0, 0, 0, 90, 0, 0)
Go P1 ' moves to AglToPls(0, 0, 0, 0, 0, 90) joint position
```

```spel
Move AglToPls(0, 0, 0, 90, 0, 0) ' moves to AglToPls(0, 0, 0, 0, 0, 90) joint position
```

```spel
Go AglToPls(0, 0, 0, 90, 0, 0)
```

## See Also
Converts robot angles to pulses.

Agl, JA, Pls

AglToPls Function


---

# And Operator
**Type:** reference | **Section:** Operator

## Syntax
```
result = expr1 And expr2
```

## Parameters
expr1,
		 expr2	For logical
		 And, any valid expression which returns a Boolean result.  For
		 bitwise And, an integer expression.

result	For logical
		 And, result is a Boolean value.  For bitwise And, result
		 is an integer.

## Description
A logical And is used to combine the results of 2 or more expressions into 1 single Boolean result.  The following table indicates the possible combinations.

expr1	expr2	result

True	True	True

True	False	False

False	True	False

False	False	False

A bitwise And performs a bitwise comparison of identically positioned bits in two numeric expressions and sets the corresponding bit in result according to the following table:

If
		 bit in expr1 is	And bit in expr2 is	The
		 result is

0	0	0

0	1	0

1	0	0

1	1	1

## Examples
```spel
Function LogicalAnd(x As Integer, y As Integer) If x = 1 And y = 2 Then
    Print "The values are correct" EndIf
Fend
```

```spel
Function BitWiseAnd() If (Stat(0) And &H800000) = &H800000 Then
    Print "The enable switch is open" EndIf
Fend

>print 15 and 7
7
>
```

## See Also
LShift

Not

Or

RShift

Xor

And Operator Example

Function LogicalAnd(x As Integer, y As Integer)

  If x = 1 And y = 2 Then

    Print "The values are correct"

  EndIf

Fend

Function BitWiseAnd()

  If (Stat(0) And &H800000) = &H800000 Then

    Print "The enable switch is open"

  EndIf

Fend

>print 15 and 7

7

>


---

# Arc, Arc3 Statements
**Type:** reference | **Section:** Operator

## Syntax
```
(1) Arc midPoint, endPoint [ROT] [ CP ] [ searchExpr ] [!...!] [SYNC]

(2) Arc3 midPoint, endPoint [ROT] [ECP] [ CP ] [ searchExpr ] [!...!] [SYNC]
```

## Parameters
midPoint	Point expression.or XY function.  The middle point which the arm travels through on its way from the current point to endPoint.

endPoint	Point expression or XY function.The end point which the arm travels to during the arc type motion.  This is the final position at the end of the circular move.

ROT	Optional.  Decides the speed/acceleration/deceleration in favor of tool rotation.

ECP	Optional.  External control point motion.  This parameter is valid when the ECP option is enabled

CP	Optional.  Specifies continuous path motion.

searchExpr	Optional.  A Till or Find expression.

Till | Find

Till Sw(expr) = {On | Off}

Find Sw(expr) = {On | Off}

!...!	Parallel processing statements may be used with the Arc statement.  These are optional. (Please see the Parallel Processing description for more information.)

SYNC	Reserves a motion command. The robot will not move until SyncRobots is executed.

## Description
Arc and Arc3 are used to move the arm in a circular type motion from the current position to endPoint by way of midPoint.  The system automatically calculates a curve based on the 3 points (current position, endPoint, and midPoint) and then moves along that curve until the point defined by endPoint is reached.

Also, for SCARA robots, U coordinate moves to move from current point to end point. However, for 6-Axis robot, U, V and W coordinates moves with the shortest posture for rotation to move from current point to end point.

If using this, check the actual movement in advance.

Arc and Arc3 use the SpeedS speed value and AccelS acceleration and deceleration values. Refer to Using Arc, Arc3 with CP below on the relation between the speed/acceleration and the acceleration/deceleration.  If, however, the ROT modifier parameter is used, Arc and Arc3 use the SpeedR speed value and AccelR acceleration and deceleration values.  In this case SpeedS speed value and AccelS acceleration and deceleration value  have no effect.

Usually, when the move distance is 0 and only the tool orientation is changed, an error will occur. However, by using the ROT parameter and giving priority to the acceleration and the deceleration of the tool rotation, it is possible to move without an error. When there is not an orientational change with the ROT modifier parameter and movement distance is not 0, an error will occur.

Also, when the tool rotation is large as compared to move distance, and when the rotation speed exceeds the specified speed of the manipulator, an error will occur. In this case, please reduce the speed or append the ROT modifier parameter to give priority to the rotational speed/acceleration/deceleration.

When ECP is used (Arc3 only), the trajectory of the external control point coresponding to the ECP number specified by ECP instruction moves circular with respect to the tool coordinate system. In this case, the trajectory of tool center point does not follow a circular line.

Setting Speed and Acceleration for Arc Motion

SpeedS and AccelS are used to set speed and acceleration for the Arc and Arc3 instructions.  SpeedS and AccelS allow the user to specify a velocity in mm/sec and acceleration in mm/sec2.

## Notes
Arc Instruction works in Horizontal Plane Only

The Arc path is a true arc in the Horizontal plane.  The path is interpolated using the values for endPoint as its basis for Z and U.  Use Arc3 for 3 dimensional arcs.

Range Verification for Arc Instruction

The Arc and Arc3 statements cannot compute a range verification of the trajectory prior to the arc motion.  Therefore, even for target positions that are within an allowable range, en route the robot may attempt to traverse a path which has an invalid range, stopping with a severe shock which may damage the arm.  To prevent this from occurring, be sure to perform range verifications by running the program at low speeds prior to running at faster speeds.

Suggested Motion to Setup for the Arc Move

Because the arc motion begins from the current position, it may be necessary to use the Go, Jump or other related motion command to bring the robot to the desired position prior to executing Arc or Arc3.

Using Arc, Arc3 with CP

The CP parameter causes the arm to move to the end point without decelerating or stopping at the point defined by endPoint.  This is done to allow the user to string a series of motion instructions together to cause the arm to move along a continuous path while maintaining a specified speed throughout all the motion.  The Arc3 instruction without CP always causes the arm to decelerate to a stop prior to reaching the end point.

Potential Errors

Changing Hand (arm) Attributes

Pay close attention to the HAND attributes of the points used with the Arc instruction.  If the hand orientation changes (from Right Handed to Left Handed or vice-versa) during the circular interpolation move, an error will occur.  This means the arm attribute (/L Lefty, or /R Righty) values must be the same for the current position, midPoint, and endPoint points.

Attempt to Move Arm Outside Work Envelope

If the specified circular motion attempts to move the arm outside the work envelope of the arm, an error will occur.

## Examples
```spel
Function ArcTest Go P100 Arc P101, P102
Fend
```

## See Also
Robot motion commands

!Parallel Processing!

AccelS

Move

SpeedS

Arc Statement Example

The diagram below shows arc motion which originated at the point P100 and then moves through P101 and ends up at P102. The following function would generate such an arc:

Function ArcTest

  Go P100

  Arc P101, P102

Fend

Tip

When first trying to use the Arc instruction, it is suggested to try a simple arc with points directly in front of the robot in about the middle of the work envelope.  Try to visualize the arc that would be generated and make sure that you are not teaching points in such a way that the robot arm would try to move outside the normal work envelope.


---

# Arch Function
**Type:** function | **Section:** Operator

## Syntax
```
Arch(archNumber, paramNumber)
```

## Parameters
archNumber	Integer expression
		 representing arch setting to retrieve parameter from (0 to 6).

paramNumber	1: depart
		 distance

2: approach
		 distance

## Description
Arch Function

Arch Function

See_Also Example

Returns arch settings.

## Examples
```spel
Double archValues(6, 1)
Integer i

' Save current arch values
For i = 0 to 6 archValues(i, 0) = Arch(i, 1) archValues(i, 1) = Arch(i, 2)
Next i
```

## See Also
Arch Statement

Arch Function Example

Double archValues(6, 1)

Integer i

' Save current arch values

For i = 0 to 6

  archValues(i, 0) = Arch(i, 1)

  archValues(i, 1) = Arch(i, 2)

Next i


---

# Arch Keyword
**Type:** reference | **Section:** Operator

## Description
Arch Keyword

Arch Keyword

The Arch keyword is used in these contexts:

Arch Statement

Arch Function


---

# Arch Statement
**Type:** statement | **Section:** Operator

## Syntax
```
(1) Arch archNumber, departDist, approDist

(2) Arch archNumber

(3) Arch
```

## Parameters
archNumber	Integer expression
		 representing the Arch
		 number to define.  Valid
		 Arch
		 numbers are from 0 to 6 making
		 a total of 7 entries into the Arch
		 table. (see default Arch Table below)

departDist	The vertical
		 distance moved (Z) at the beginning of the Jump
		 move before beginning horizontal motion. (specified in millimeters)

For Jump3 and
		 Jump3CP, it specifies the depart distance before a span motion.
		 (specified in millimeters)

approDist	The vertical
		 distance required (as measured from the Z position of the point
		 the arm is moving to) to move in a completely vertical fashion
		 with all horizontal movement complete. (specified in millimeters)

For Jump3 and
		 Jump3CP, it specifies the approach distance before a span motion.
		 (specified in millimeters)

## Description
The primary purpose of the Arch instruction is to define values in the Arch Table which is required for use with the Jump motion instruction.  The Arch motion is carried out per the parameters corresponding to the arch number selected in the Jump C modifier. (To completely understand the Arch instruction, the user must first understand the Jump instruction.)

The Arch definitions allow the user to "round corners" in the Z direction when using the Jump C instruction.  While the Jump instruction specifies the point to move to (including the final Z joint position), the Arch table entries specify how much distance to move up before beginning horizontal motion (riseDist) and how much distance up from the final Z joint position to complete all horizontal motion (fallDist). (See the diagram below)

There are a total of 8 entries in the Arch Definition Table with 7 of them (0-6) being user definable.  The 8th entry (Arch 7)is the default Arch which actually specifies no arch at all which is referred to as Gate Motion.  (See Gate Motion diagram below) The Jump instruction used with the default Arch entry (Entry 8) causes the arm to do the following:

1) Begin the move with only Z-joint motion until it reaches the Z-Coordinate value specified by the LimZ command. (The upper Z value)

2) Next move horizontally to the target point position until the final X, Y, and U positions are reached.

3) The Jump instruction is then completed by moving the arm down with only Z-joint motion until the target Z-joint position is reached.

Arch Table Default Values:

Arch

Number	Depart

Distance	Approach Distance

0	30	30

1	40	40

2	50	50

3	60	60

4	70	70

5	80	80

6	90	90

## Notes
Caution for Arch motion

Jump motion trajectory is comprised of vertical motion and horizontal motion. It is not a continuous path trajectory. The actual Jump trajectory of arch motion is not determined by Arch parameters alone. It also depends on motion and speed.

Always use care when optimizing Jump trajectory in your applications.  Execute Jump with the desired motion and speed to verify the actual trajectory.

When speed is lower, the trajectory will be lower.
  If Jump is executed with high speed to verify an arch motion trajectory, the end effector may crash into an obstacle with lower speed.

In a Jump trajectory, the depart distance increases and the approach distance decreases when the motion speed is set high. When the fall distance of the trajectory is shorter than the expected, lower the speed and/or the deceleration, or change the fall distance to be larger.

Even if Jump commands with the same distance and speed are executed, the trajectory is affected by motion of the robot arms.  As a general example, for a SCARA robot the vertical upward distance increases and the vertical downward distance decreases when the movement of the first arm is large.  When the vertical fall distance decreases and the trajectory is shorter than the expected, lower the speed and/or the deceleration, or change the fall distance to be larger.

Another Cause of Gate Motion

When the specified value of the RisingDistance or Falling Distance is larger than the actual Z-joint distance which the robot must move to reach the target position, Gate Motion will occur. (i.e. no type Arch motion will occur.)

Arch values are Maintained

The Arch Table values are permanently saved and are not changed until the user changes them.

Arch Statement Example
 The following are examples of Arch settings done from the command window.

> arch 0, 15, 15

> arch 1, 25, 50

> jump p1 c1

> arch

arch0 = 15.000 15.000

arch1 = 25.000 50.000

arch2 = 50.000 50.000

arch3 = 60.000 60.000

arch4 = 70.000 70.000

arch5 = 80.000 80.000

arch6 = 90.000 90.000

>

## Examples
```spel
> arch 0, 15, 15
```

```spel
> arch 1, 25, 50
```

```spel
> jump p1 c1
```

```spel
> arch
```

```spel
arch0 = 15.000 15.000
```

```spel
arch1 = 25.000 50.000
```

```spel
arch2 = 50.000 50.000
```

```spel
arch3 = 60.000 60.000
```

```spel
arch4 = 70.000 70.000
```

```spel
arch5 = 80.000 80.000
```

```spel
arch6 = 90.000 90.000
```

```spel
>
```

## See Also
Jump

Jump3

Jump3CP


---

# Arch page, Robot Manager Window
**Type:** reference | **Section:** Operator

## Description
Arch page, Robot Manager Window

[Tools]-[Robot Manager]-[Arch] Page

This page allows you to configure the depart Z and approach Z settings in the robot's Arch table. Arch is used for the Jump, Jump3, and Jump3CP motion commands.

For more details on Arch settings, refer to the following manual:

SPEL+ Language Reference - Arch Statement

Navigating the grid

Press the [Tab] key to move to the next cell. Press the [Shift] + [Tab] key to move to the previous cell. Press the arrow [↑] or [↓] key to move to the cell above or below.

Item	Description

Arch	The Arch
		 number. There are up to seven different setting pairs in the Arch table.

Depart
		 Z	Specifies
		 the vertical rise distance of the arch motion.

Approach
		 Z	Specifies
		 the vertical descent distance of the arch motion.

Apply	Sets
		 the current values.

Restore	Reverts
		 to the previous values.

Defaults	Displays
		 factory default settings.

To change Arch settings

1. Put the cursor in the Depart Z or Approach Z cell of the row you want to change.

2. Type in the new value.


---

# Arm Function
**Type:** function | **Section:** Operator

## Syntax
```
Arm
```

## Description
Arm Function

Arm Function

See_Also Example

Returns the current arm number for the current robot.

## Examples
```spel
Print "The current arm number is: ", Arm
```

## See Also
Arm Statement

Arm Function Example

Print "The current arm number is: ", Arm


---

# Arm Keyword
**Type:** reference | **Section:** Operator

## Description
Arm Keyword

Arm Keyword

The Arm keyword is used in these contexts:

Arm Statement

Arm Function


---

# Arm Statement
**Type:** statement | **Section:** Operator

## Syntax
```
(1) Arm [armNumber]

(2) Arm
```

## Parameters
armNumber	Optional integer
		 expression. Valid range is from 0 - 15. The user may select up
		 to 16 different arms. Arm 0 is the standard (default) robot arm.
		 Arms 1 -15 are auxiliary arms defined by using the ArmSet
		 instruction. When omitted, the current arm number is displayed.

## Description
Allows the user to specify which arm to use for robot instructions.  Arm allows each auxiliary arm to use common position data. If no auxiliary arms are installed, the standard arm (arm number 0) operates.  Since at time of delivery the arm number is specified as 0, it is not necessary to use the Arm instruction to select an arm.  However, if auxiliary arms are used they must first defined with the ArmSet instruction.

The auxiliary arm configuration capability is provided to allow users to configure the proper robot parameters for their robots when the actual robot configuration is a little different than the standard robot.  For example, if the user mounted a 2nd orientation joint to the 2nd robot link, the user will probably want to define the proper robot linkages for the new auxiliary arm which is formed.  This will allow the auxiliary arm to function properly under the following conditions:

- Specifying that a single data point be moved through by 2 or more arms.

- Using Pallet

- Using Continuous Path motion

- Using relative position specifications

- Using Local coordinates

For SCARA robots (including RS series) with rotating joints used with a Cartesian coordinate system, joint angle calculations are based on the parameters defined by the ArmSet parameters.  Therefore, this command is critical if any auxiliary arm or hand definition is required.

Robot parameter data is stored in compact flash in controller.  Therefore, writing to command flash occurs when executing this command.  Frequent writing to compact flash affect to lifetime of compact flash.  We recommend to use this command minimally.

## Notes
Arm 0

Arm 0 cannot be defined or changed by the user through the ArmSet instruction.  It is reserved since it is used to define the standard robot configuration. When the user sets Arm to 0 this means to use the standard robot arm parameters.

Using the Arm Length Calibration Option

Applies the arm length calibration value to Arm 0 and automatically switches to Arm 0 when ArmCalib is turned On. Use Arm 0 to apply the arm length calibration value when moving the robot. The arm length calibration value will not be applied even if ArmCalib is On when using an arm number other than Arm 0.

To use standard robot arm parameters, use Arm 0 with ArmCalib turned Off.

Arm Number Not Defined

Selecting auxiliary arm numbers that have not been defined by the ArmSet command will result in an error.

## Examples
```spel
> armset 1, 300, -12, -30, 300, 0
```

```spel
> armset
```

```spel
arm0 250 0 0 300 0
```

```spel
arm1 300 -12 -30 300 0
```

```spel
> arm 0
```

```spel
> jump p1  'Jump to P1 using the Standard Arm Config
```

```spel
> arm 1
```

```spel
> jump p1  'Jump to P1 using auxiliary arm 1
```

## See Also
ArmClr

ArmSet

ECPSet

TLSet

ArmCalibSet

Arm Statement Example

The following examples are potential auxiliary arm definitions using the ArmSet and Arm instructions. ArmSet defines the auxiliary arm and Arm defines which Arm to use as the current arm. (Arm 0 is the default robot arm and cannot be adjusted by the user.)

From the command window:

> armset 1, 300, -12, -30, 300, 0

> armset

arm0 250 0 0 300 0

arm1 300 -12 -30 300 0

> arm 0

> jump p1  'Jump to P1 using the Standard Arm Config

> arm 1

> jump p1  'Jump to P1 using auxiliary arm 1


---

# ArmCalib Statement
**Type:** statement | **Section:** Operator

## Syntax
```
ArmCalib On | Off
```

## Parameters
On | Off	Select On to enable arm length calibration. Select Off to disable arm length calibration.

## Description
The ArmCalib On instruction enables arm length calibration.

Execute ArmCalib On to set the calibration value specified using ArmCalibSet to Arm 0, and switch the Arm to 0.

The ArmCalib Off instruction disables arm length calibration.

Execute ArmCalib Off to set the standard parameters to Arm 0. Note that the Arm will not switch automatically when ArmCalib Off is executed.

Arm length calibration is enabled by default when purchasing the Arm Length Calibration Option.

Even when arm length calibration is enabled, switching to an Arm other than 0 will use the settings configured for the Arm number set.

Robot parameter data is stored in the compact flash memory in the controller. Therefore, writing to the compact flash memory occurs when executing this command. Frequent writing to the compact flash memory affects the lifetime of the compact flash memory. We recommend limiting the use of this command at a minimum.

Note

This command is only available when the Arm Length Calibration Option is installed.

Do not restore backup files with ArmCalib On on a controller that has the Arm Length Calibration Option disabled.

Attempting to restore backup files with ArmCalib On on a controller that has the Arm Length Calibration Option disabled will automatically set ArmCalib Off. Keep this in mind when restoring to a separate controller.

## Examples
```spel
> ArmCalib On
```

```spel
> ArmCalib Off
```

## See Also
ArmCalibClr

ArmCalibSet

ArmCalibDef

ArmCalib Statement Example

The following example is executed from the Command window.

> ArmCalib On

> ArmCalib Off


---

# ArmCalibClr Statement
**Type:** statement | **Section:** Operator

## Syntax
```
ArmCalibClr
```

## Description
Robot parameter data is stored in the compact flash memory in the controller. Therefore, writing to the compact flash memory occurs when executing this command. Frequent writing to the compact flash memory affects the lifetime of the compact flash memory. We recommend limiting the use of this command at a minimum.

Note

Do not use ArmCalibClr unless absolutely necessary.

ArmCalibClr clears the arm length calibration parameters set using ArmCalibSet. ArmCalibSet contains factory settings that have been precisely set. (When purchasing the Arm Length Calibration Option) Accidentally clearing these settings will require precise measurements to be performed by the factory again. Do not use ArmCalibClr unless absolutely necessary.

## Examples
```spel
ArmCalibClr
```

## See Also
ArmCalib

ArmCalibSet

ArmCalibClr Statement Example

ArmCalibClr


---

# ArmCalibDef Statement
**Type:** statement | **Section:** Operator

## Syntax
```
ArmCalibDef
```

## Description
ArmCalibDef Statement

ArmCalibDef Statement

See_Also Example

Returns the arm length calibration configuration status.

## Examples
```spel
Function DisplayArmCalibDef Integer i
    If ArmCalibDef = False Then
     Print "ArmCalib is not defined" Else
     Print "ArmCalib Definition:"
     For i = 1 to 3
       Print ArmCalibSet(i)
     Next i EndIf
Fend
```

## See Also
ArmCalib

ArmCalibClr

ArmCalibSet

ArmCalibDef Statement Example

Function DisplayArmCalibDef
 Integer i

    If ArmCalibDef = False Then

     Print "ArmCalib is not defined"

  Else

     Print "ArmCalib Definition:"

     For i = 1 to 3

       Print ArmCalibSet(i)

     Next i

  EndIf

Fend


---

# ArmCalibSet Statement
**Type:** statement | **Section:** Operator

## Syntax
```
(1) ArmCalibSet setValue1, setValue2, setValue3

(2) ArmCalibSet
```

## Parameters
setValue	SCARA robots

1	Horizontal distance from Joint #1 to Joint #2 (mm)

2	Horizontal distance from Joint #2 to orientation center (mm)

3	Joint #2 angle offset ()

## Description
ArmCalibSet sets parameters related to the arm length and joint offsets. Distance accuracy can be increased by using the length and joint offset of each arm that were precisely calculated at the factory and configuring settings using this command.

Robot parameter data is stored in the compact flash memory in the controller. Therefore, writing to the compact flash memory occurs when executing this command. Frequent writing to the compact flash memory affects the lifetime of the compact flash memory. We recommend limiting the use of this command at a minimum.

Note

Do not use ArmCalibSet unless absolutely necessary.

ArmCalibSet contains factory settings that have been precisely set. (When purchasing the Arm Length Calibration Option)

Accidentally changing these settings adversely affects distance accuracy and trajectory accuracy. Do not change ArmCalibSet unless absolutely necessary.

## Examples
```spel
> ArmCalibSet 299.989, 250.001, 0.012
```

## See Also
ArmCalib

ArmCalibClr

ArmCalibDef

ArmCalibSet Statement Example

The following example is executed from the Command window.

> ArmCalibSet 299.989, 250.001, 0.012


---

# ArmClr Statement
**Type:** statement | **Section:** Operator

## Syntax
```
ArmClr
  armNumber
```

## Parameters
armNumber	Integer expression representing which
		 of 15 arms to clear (undefine).  (Arm 0 is the default arm
		 and cannot be cleared.)

## Description
Robot parameter data is stored in compact flash in controller.  Therefore, writing to command flash occurs when executing this command.  Frequent writing to compact flash affect to lifetime of compact flash.  We recommend to use this command minimally.

## See Also
Arm

ArmSet

Local

LocalClr

Tool

TLSet

ArmClr Example

ArmClr 1


---

# ArmSet Function
**Type:** function | **Section:** Operator

## Syntax
```
ArmSet(armNumber, paramNumber)
```

## Parameters
armNumber	Integer expression representing the arm number to retrieve values for.

paramNumber	Integer expression representing the parameter to retrieve (0 to 5), as described below.

SCARA Robots (including RS series)

paramNumber	Value Returned

1	Horizontal distance from joint #2 to orientation center (mm)

2	Joint #2 angle offset (degree)

3	Height offset (mm)

4	Horizontal distance from joint #1 to joint #2 (mm)

5	Orientation joint angle offset in degrees.

## Description
ArmSet Function

ArmSet Function

See_Also Example

Returns one ArmSet parameter.

## Examples
```spel
Real x
x = ArmSet(1, 1)
```

## See Also
ArmClr

ArmSet Statement

Armset Function Example

Real x

x = ArmSet(1, 1)


---

# ArmSet Statement
**Type:** statement | **Section:** Operator

## Syntax
```
(1) ArmSet armNumber, link2Dist, joint2Offset, zOffset, [link1Dist ], [orientAngOffset]

(2) ArmSet armNumber

(3) ArmSet
```

## Parameters
armNumber	Integer expression: Valid range from 1-15. The user may define up to 15 different auxiliary arms.

link2Dist	(For SCARA Robots) The horizontal distance from the center line of the elbow joint to the center line of the new orientation joint. (i.e. the position where the new auxiliary arm's orientation axis center line is located.)

joint2Offset	(For SCARA Robots) The offset (in degrees) between the line formed between the normal Elbow center line and the normal orientation Axis center line and the line formed between the new auxiliary arm elbow center line and the new orientation axis center line. (These 2 lines should intersect at the elbow center line and the angle formed is the joint2Offset.)

zOffset	(For SCARA Robots) The Z height offset difference between the new orientation axis center and the old orientation axis center. (This is a distance.)

link1Dist	(For SCARA Robots) The distance from the shoulder center line to the elbow center line of the elbow orientation of the new auxiliary axis.

orientAngOffset	(For SCARA Robots) The angular offset (in degrees) for the new orientation axis vs. the old orientation axis.

## Description
Allows the user to specify auxiliary arm parameters to be used in addition to the standard arm configuration. This is most useful when an auxiliary arm or hand is installed to the robot. When using an auxiliary arm, the arm is selected by the Arm instruction.

The link1Dist and orientAngOffset parameters are optional. If they are omitted, the default values are the standard arm values.

The auxiliary arm configuration capability is provided to allow users to configure the proper robot parameters for their robots when the actual robot configuration is a little different than the standard robot. For example, if the user mounted a 2nd orientation joint to the 2nd robot link, the user will probably want to define the proper robot linkages for the new auxiliary arm which is formed. This will allow the auxiliary arm to function properly under the following conditions:

- Specifying that a single data point be moved through by 2 or more arms.

- Using Pallet

- Using Continuous Path motion

- Using relative position specifications

- Using Local coordinates

For SCARA robots with rotating joints used with a Cartesian coordinate system, joint angle calculations are based on the parameters defined by the ArmSet parameters. Therefore, this command is critical if any auxiliary arm or hand definition is required.

Robot parameter data is stored in compact flash in controller.  Therefore, writing to command flash occurs when executing this command.  Frequent writing to compact flash affect to lifetime of compact flash.  We recommend to use this command minimally.

## Notes
Arm 0

Arm 0 cannot be defined or changed by the user. It is reserved since it is used to define the standard robot configuration. When the user sets Arm to 0 this means to use the standard robot arm parameters.

## Examples
```spel
> armset 1, 300, -12, -30, 300, 0
```

```spel
> armset
```

```spel
arm0 250 0 0 300 0
```

```spel
arm1 300 -12 -30 300 0
```

```spel
> arm 0
```

```spel
> jump p1  'Jump to P1 using the Standard Arm Config
```

```spel
> arm 1
```

```spel
> jump p1  'Jump to P1 using auxiliary arm 1
```

## See Also
Arm

Armset Function

ArmClr Statement

ArmSet Statement Example

The following examples are potential auxiliary arm definitions using the ArmSet and Arm instructions. ArmSet defines the auxiliary arm and Arm defines which Arm to use as the current arm. (Arm 0 is the default robot arm and cannot be adjusted by the user.)

From the command window:

> armset 1, 300, -12, -30, 300, 0

> armset

arm0 250 0 0 300 0

arm1 300 -12 -30 300 0

> arm 0

> jump p1  'Jump to P1 using the Standard Arm Config

> arm 1

> jump p1  'Jump to P1 using auxiliary arm 1


---

# Arms page: Robot Manager Window
**Type:** reference | **Section:** Operator

## Description
Arms page: Robot Manager Window

[Tools]-[Robot Manager]-[Arms] Page

This page allows you to define Arm settings for a robot. When the tab is selected, the current Arm values are displayed. The tab is disabled if the current robot does not support the Arm command.

A grid is used to display all the values for all 15 arm configurations you can define.

When an arm is undefined, then all fields for that arm will be blank.

When you enter a value in any of the fields for an undefined arm, then the remaining fields will be set to zero and the tool will be defined when you click the [Apply] button.

For more details on arm settings, refer to the following manual:

SPEL+ Language Reference - ArmSet Statement

Navigating the grid

Press the [Tab] key to move to the next cell. Press the [Shift] + [Tab] key to move to the previous cell. Press the arrow [↑] or [↓] key to move to the cell above or below.

Item	Description

Arm Wizard	Open
		 the wizard for configuring the additional arm using the camera.

Define the tool by following the instructions.

For more details, refer to the following
		 manual:

		Refer to 7. Vision Calibration in the Vision Guide 8.0 Software
		 manual.

L2 Dist	Distance
		 between the center of joint 2 and the center of the orientation
		 joint in millimeters.

J2 Offset	Angle
		 of the line from the center of joint 2 to the center of the orientation
		 joint in degrees.

Z Offset	The Z
		 offset between the new orientation axis and the standard orientation
		 axis.

L1 Dist	Distance
		 between the center of the shoulder joint and the center of the
		 elbow joint in millimeters.

U Offset	The angle
		 offset between the standard orientation zero position and the
		 new orientation axis zero position in degrees.

Apply	Sets
		 the current values.

Restore	Reverts
		 to the previous values.

Clear	Clears
		 all selected values.


---

# Armset Keyword
**Type:** reference | **Section:** Operator

## Description
Armset Keyword

Armset Keyword

The Armset keyword is used in these contexts:

ArmSet Statement

ArmSet Function


---

# Asc Function
**Type:** reference | **Section:** Operator

## Syntax
```
Asc(string)
```

## Parameters
string	Any valid string expression of at least one character in length.

## Description
The Asc function is used to convert a character to its ASCII numeric representation. The character string send to the Asc function may be a constant or a variable.

## Notes
Only the First Character ASCII Value is Returned

Although the Asc instruction allows character strings larger than 1 character in length, only the 1st character is actually used by the Asc instruction. Asc returns the ASCII value of the 1st character only.

## Examples
```spel
Function asctest Integer a, b, c a = Asc("a") b = Asc("b") c = Asc("c") Print "The ASCII value of a is ", a Print "The ASCII value of b is ", b Print "The ASCII value of c is ", c
Fend
```

```spel
>print asc("a")
```

```spel
97
```

```spel
>print asc("b")
```

```spel
98
```

```spel
>
```

## See Also
Chr$

InStr

Left$

Len

Mid$

Right$

Space$

Str$

Val

Asc Function Example

This example uses the Asc instruction in a program and from the command window as follows:

Function asctest

  Integer a, b, c

  a = Asc("a")

  b = Asc("b")

  c = Asc("c")

  Print "The ASCII value of a is ", a

  Print "The ASCII value of b is ", b

  Print "The ASCII value of c is ", c

Fend

From the Command window:

>print asc("a")

97

>print asc("b")

98

>


---

# Asin Function
**Type:** function | **Section:** Operator

## Syntax
```
Asin(number)
```

## Parameters
number	Numeric
		 expression representing the sine of an angle.

## Description
Asin returns the arcsine of the numeric expression.
  Values range is from -1 to 1.  The value returned by Asin will range from -PI / 2 to PI / 2 radians.  If number is -1 or 1, an error occurs.

To convert from radians to degrees, use the RadToDeg function.

## Examples
```spel
Function asintest Double x x = Sin(DegToRad(45)) Print "Asin of ", x, " is ", Asin(x)
Fend
```

## See Also
Returns the arcsine of a numeric expression.

Abs, Acos, ATan, ATan2, Cos, DegToRad, RadToDeg, Sgn, Sin, Tan, Val

Asin Function Example

Function asintest

  Double x

  x = Sin(DegToRad(45))

  Print "Asin of ", x, " is ", Asin(x)

Fend


---

# AutoStepID Property
**Type:** property | **Section:** Operator

## Description
Set whether to set StepID of force guide object automatically.

StepID is an ID which is recorded in the log data.
  It helps you to understand which log data support a process.

Values

True : Normal

False : When you want to set StepID manually.

## See Also
Applies To

Sequences
 Property

StepID Property


---

# AvgForces Result
**Type:** result | **Section:** Operator

## Description
Returns average values of force and torque during execution of a force guide object.

## Notes
Returns average values of force and torque during execution of a force guide object.

If the number of elements in a specified array variable is less than six, returns force and torque in each direction for the defined element numbers.  Also, if the number of elements in the array variable exceeds six, returns force and torque in each direction from element number 0 to 5, while making no change to element number 6 and above.

## Examples
```spel
Function AvgForceTest
     Double dArray(6)
    Motor On
     FGRun Sequence1
     FGGet Sequence1.Contact01.AvgForces, dArray()  ' Acquisition of AvgForces
    Print dArray(FG_FX)
Fend
```

## See Also
Result

FGGet


---

# BGo Statement
**Type:** statement | **Section:** Operator

## Syntax
```
BGo destination  [CP]
  [searchExpr]  [!...!] [SYNC]
```

## Parameters
destination	The target
		 destination of the motion using a point expression.

CP	Optional.
		  Specifies continuous path motion.

searchExpr	Optional.
		  A Till or Find expression.

Till
		 | Find

Till
		 Sw(expr) = {On
		 | Off}

Find
		 Sw(expr) = {On
		 | Off}

!...!	Optional.
		  Parallel Processing statements can be added to execute I/O
		 and other commands during motion.

SYNC	Reserves a
		 motion command. The robot will not move until SyncRobots is executed.

## Description
Executes point to point relative motion, in the selected local coordinate system that is specified in the destination point expression.

If a local coordinate system is not specified, relative motion will occur in local 0 (base coordinate system).

Arm orientation attributes specified in the destination point expression are ignored. The manipulator keeps the current arm orientation attributes.
  However, for a 6-Axis manipulator (including N series), the arm orientation attributes are automatically changed in such a way that joint travel distance is as small as possible. This is equivalent to specifying the LJM modifier parameter for Move statement.  Therefore, if you want to change the arm orientation larger than 180 degrees, execute it in several times.

The Till modifier is used to complete BGo by decelerating and stopping the robot at an intermediate travel position if the current Till condition is satisfied.

The Find modifier is used to store a point in FindPos when the Find condition becomes true during motion.

When Till is used and the Till condition is satisfied, the manipulator halts immediately and the motion command is finished. If the Till condition is not satisfied, the manipulator moves to the destination point.

When Find is used and the Find condition is satisfied, the current position is stored. Please refer to Find for details.

When parallel processing is used, other processing can be executed in parallel with the motion command.

The CP parameter causes acceleration of the next motion command to start when the deceleration starts for the current motion command.  In this case the robot will not stop at the destination coordinate and will continue to move to the next point.

## Examples
```spel
> BGo XY(100, 0, 0, 0)   'Move 100mm in X direction
```

```spel
'(in the local coordinate system)
```

```spel
Function BGoTest Speed 50 Accel 50, 50 Power High P1 = XY(300, 300, -20, 0) P2 = XY(300, 300, -20, 0) /L Local 1, XY(0, 0, 0, 45) Go P1 Print Here BGo XY(0, 50, 0, 0) Print Here Go P2 Print Here BGo XY(0, 50, 0, 0) Print Here BGo XY(0, 50, 0, 0) /1 Print Here

Fend
```

```spel
[Output]
```

```spel
X:  300.000 Y:  300.000 Z:  -20.000 U     0.000 V:    0.000 W     0.000 /N /0
```

```spel
X:  300.000 Y:  350.000 Z:  -20.000 U     0.000 V:    0.000 W     0.000 /N /0
```

```spel
X:  300.000 Y:  300.000 Z:  -20.000 U     0.000 V:    0.000 W     0.000 /L /0
```

```spel
X:  300.000 Y:  350.000 Z:  -20.000 U     0.000 V:    0.000 W     0.000 /L /0
```

```spel
X:  264.645 Y:  385.355 Z:  -20.000 U:    0.000 V:    0.000 W:    0.000 /L /0
```

## See Also
Executes Point to Point relative motion, in the selected local coordinate system.

Accel, BMove, Find, Parallel Processing, Point Assignment, Speed, Till, TGo, TMove, Tool

BGo Statement Example

Shown below is a simple example from the Command window.

> BGo XY(100, 0, 0, 0)   'Move 100mm in X direction

                         '(in the local coordinate system)

Function BGoTest

  Speed 50

  Accel 50, 50

  Power High

  P1 = XY(300, 300, -20, 0)

  P2 = XY(300, 300, -20, 0) /L

  Local 1, XY(0, 0, 0, 45)

  Go P1

  Print Here

  BGo XY(0, 50, 0, 0)

  Print Here

  Go P2

  Print Here

  BGo XY(0, 50, 0, 0)

  Print Here

  BGo XY(0, 50, 0, 0) /1

  Print Here

Fend

[Output]
 X:  300.000 Y:  300.000 Z:  -20.000 U     0.000 V:    0.000 W     0.000 /N /0
 X:  300.000 Y:  350.000 Z:  -20.000 U     0.000 V:    0.000 W     0.000 /N /0
 X:  300.000 Y:  300.000 Z:  -20.000 U     0.000 V:    0.000 W     0.000 /L /0
 X:  300.000 Y:  350.000 Z:  -20.000 U     0.000 V:    0.000 W     0.000 /L /0
 X:  264.645 Y:  385.355 Z:  -20.000 U:    0.000 V:    0.000 W:    0.000 /L /0


---

# BMove Statement
**Type:** statement | **Section:** Operator

## Syntax
```
BMove destination  [ROT] [CP]  [searchExpr]  [!...!] [SYNC]
```

## Parameters
destination	The target destination of the motion using a point expression.

ROT	Optional.  :Decides the speed/acceleration/deceleration in favor of tool rotation.

CP	Optional.  Specifies continuous path motion.

searchExpr	Optional.  A Till or Find expression.

Till | Find

Till Sw(expr) = {On | Off}

Find Sw(expr) = {On | Off}

!...!	Optional.  Parallel Processing statements can be added to execute I/O and other commands during motion.

SYNC	Reserves a motion command. The robot will not move until SyncRobots is executed.

## Description
Executes linear interpolated relative motion, in the selected local coordinate system that is specified in the destination point expression.

If a local coordinate system is not specified, relative motion will occur in local 0 (base coordinate system).

Arm orientation attributes specified in the destination point expression are ignored.  The manipulator keeps the current arm orientation attributes.  However, for a 6-Axis manipulator (including N series), the arm orientation attributes are automatically changed in such a way that joint travel distance is as small as possible. This is equivalent to specifying the LJM modifier parameter for Move statement.  Therefore, if you want to change the arm orientation larger than 180 degrees, execute it in several times.

BMove uses the SpeedS speed value and AccelS acceleration and deceleration values. Refer to Using Move with CP below on the relation between the speed/acceleration and the acceleration/deceleration.  If, however, the ROT modifier parameter is used, BMove uses the SpeedR speed value and AccelR acceleration and deceleration values.  In this case SpeedS speed value and AccelS acceleration and deceleration value  have no effect.

Usually, when the move distance is 0 and only the tool orientation is changed, an error will occur. However, by using the ROT parameter and giving priority to the acceleration and the deceleration of the tool rotation, it is possible to move without an error. When there is not an orientational change with the ROT modifier parameter and movement distance is not 0, an error will occur.

Also, when the tool rotation is large as compared to move distance, and when the rotation speed exceeds the specified speed of the manipulator, an error will occur. In this case, please reduce the speed or append the ROT modifier parameter to give priority to the rotational speed/acceleration/deceleration.

The Till modifier is used to complete BMove by decelerating and stopping the robot at an intermediate travel position if the current Till condition is satisfied.

The Find modifier is used to store a point in FindPos when the Find condition becomes true during motion.

When Till is used and the Till condition is satisfied, the manipulator halts immediately and the motion command is finished.  If the Till condition is not satisfied, the manipulator moves to the destination point.

When Find is used and the Find condition is satisfied, the current position is stored.  Please refer to Find for details.

When parallel processing is used, other processing can be executed in parallel with the motion command.

## Notes
Using BMove with CP

The CP parameter causes the arm to move to destination without decelerating or stopping at the point defined by destination.  This is done to allow the user to string a series of motion instructions together to cause the arm to move along a continuous path while maintaining a specified speed throughout all the motion.  The BMove instruction without CP always causes the arm to decelerate to a stop prior to reaching the point destination.

## Examples
```spel
> BMove XY(100, 0, 0, 0)    'Move 100mm in the X direction
```

```spel
'(in the local coordinate system)
```

```spel
Function BMoveTest Speed 50 Accel 50, 50 SpeedS 100 AccelS 1000, 1000 Power High P1 = XY(300, 300, -20, 0) P2 = XY(300, 300, -20, 0) /L Local 1, XY(0, 0, 0, 45) Go P1 Print Here BMove XY(0, 50, 0, 0) Print Here Go P2 Print Here BMove XY(0, 50, 0, 0) Print Here BMove XY(0, 50, 0, 0) /1 Print Here

Fend
```

```spel
[Output]
```

```spel
X:  300.000 Y:  300.000 Z:  -20.000 U     0.000 V:    0.000 W     0.000 /N /0
```

```spel
X:  300.000 Y:  350.000 Z:  -20.000 U     0.000 V:    0.000 W     0.000 /N /0
```

```spel
X:  300.000 Y:  300.000 Z:  -20.000 U     0.000 V:    0.000 W     0.000 /L /0
```

```spel
X:  300.000 Y:  350.000 Z:  -20.000 U     0.000 V:    0.000 W     0.000 /L /0
```

```spel
X:  264.645 Y:  385.355 Z:  -20.000 U:    0.000 V:    0.000 W:    0.000 /L /0
```

## See Also
Executes linear interpolation relative motion, in the selected local coordinate system

Accel, BGo, Find, Parallel Processing, Point Assignment, Speed, Till, TGo, TMove, Tool

BMove Statement Example

Shown below is a simple example from Command window.

> BMove XY(100, 0, 0, 0)    'Move 100mm in the X direction

                            '(in the local coordinate system)

Function BMoveTest

  Speed 50

  Accel 50, 50

  SpeedS 100

  AccelS 1000, 1000

  Power High

  P1 = XY(300, 300, -20, 0)

  P2 = XY(300, 300, -20, 0) /L

  Local 1, XY(0, 0, 0, 45)

  Go P1

  Print Here

  BMove XY(0, 50, 0, 0)

  Print Here

  Go P2

  Print Here

  BMove XY(0, 50, 0, 0)

  Print Here

  BMove XY(0, 50, 0, 0) /1

  Print Here

Fend

[Output]
 X:  300.000 Y:  300.000 Z:  -20.000 U     0.000 V:    0.000 W     0.000 /N /0
 X:  300.000 Y:  350.000 Z:  -20.000 U     0.000 V:    0.000 W     0.000 /N /0
 X:  300.000 Y:  300.000 Z:  -20.000 U     0.000 V:    0.000 W     0.000 /L /0
 X:  300.000 Y:  350.000 Z:  -20.000 U     0.000 V:    0.000 W     0.000 /L /0
 X:  264.645 Y:  385.355 Z:  -20.000 U:    0.000 V:    0.000 W:    0.000 /L /0


---

# Base Statement
**Type:** reference | **Section:** Operator

## Syntax
```
(1) Base pCoordinateData

(2) Base pOrigin, pXaxis, pYaxis, [ { X | Y } ]
```

## Parameters
pCoordinateData	Point data representing the coordinate data of the origine and direction.

pOrigin	Integer expression representing the origin point using robot coordinate system.

pXaxis	Integer expression representing a point along the X axis using robot coordinate system if X alignment is specified.

pYaxis	Integer expression representing a point along the Y axis using robot coordinate system if Y alignment is specified.

X | Y	Optional.  If X alignment is specified, then pXaxis is on the X axis of the new coordinate system and only the Z coordinate of pYaxis is used.  If Y alignment is specified, then pYaxis is on the Y axis of the new coordinate system and only the Z coordinate of pXaxis is used.  If omitted, X alignment is assumed.

## Description
Defines the robot base coordinate system by specifying base coordinate system origin and rotation angle in relation to the robot absolute coordinate system.

To reset the Base coordinate system to default, execute the following statement. This will make the base coordinate system the same as the robot absolute coordinate system.

Base XY(0, 0, 0, 0)

Robot parameter data is stored in compact flash in controller.  Therefore, writing to command flash occurs when executing this command.  Frequent writing to compact flash affect to lifetime of compact flash.  We recommend to use this command minimally.

## Notes
Changing the base coordinate system deletes affects all local definitions

When base coordinates are changed, all local coordinate systems must be re-defined.

## Examples
```spel
Base XY(0, 0, 0, 0)
```

```spel
> Base XY(100, 100, 0, 0)
```

## See Also
Local

Base Statement Example

Define base coordinate system origin at 100 mm on X axis and 100 mm on Y axis

> Base XY(100, 100, 0, 0)


---

# Binary Coded Decimal
**Type:** reference | **Section:** Operator

## Description
Binary Coded Decimal

Binary Coded Decimal

Binary numbers normally convert to hexadecimal or octal numbers quite easily. Binary Coded Decimal means to convert a binary number back to decimal (base 10). This means that each group of 4 binary digits can only be converted into an equivalent decimal number between 0-9. The values 10-15 (which are easily represented with hexadecimal numbers) are not usable in the BCD format. Binary Coded Decimal numbers are normally used to convert H/W input lines to a base 10 number which can then be used for a thumbwheel switch or some other device which mostly uses base 10 numbers.


---

# Boolean Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Boolean varName [( subscripts )] [, varName [( subscripts )]...
```

## Parameters
varName	Variable name which the user wants to declare as type Boolean.

subscripts	Optional.  Dimensions of an array variable; up to 3 dimensions may be declared.  The subscripts syntax is as follows

(ubound1, [ubound2], [ubound3])

ubound1, ubound2, ubound3 each specify the maximum upper bound for the associated dimension.

The elements in each dimension of an array are numbered from 0 and the available number of array elements is the upper bound value + 1.

When specifying the upper bound value, make sure the number of total elements is within the range shown below:

Local variable   2000

Global Preserve variable   4000

Global variable and module variable   100000

## Description
Boolean is used to declare variables as type Boolean. Variables of type Boolean can contain one of two values, False and True.  Local variables should be declared at the top of a function.  Global and module variables must be declared outside of functions.

## Examples
```spel
Boolean partOK
Boolean A(10) 'Single dimension array of boolean
Boolean B(10, 10) 'Two dimension array of boolean
Boolean C(5, 5, 5) 'Three dimension array of boolean

partOK = CheckPart()
If Not partOK Then Print "Part check failed"
EndIf
```

## See Also
Data Types Overview

Variable Naming Conventions

Variable Declarations

Byte

Double

Global

Int32

Integer

Long

Real

Short

String

UByte

UInt32

UShort

Boolean Statement Example

Boolean partOK

Boolean A(10) 'Single dimension array of boolean

Boolean B(10, 10) 'Two dimension array of boolean

Boolean C(5, 5, 5) 'Three dimension array of boolean

partOK = CheckPart()

If Not partOK Then

  Print "Part check failed"

EndIf


---

# Box Statement
**Type:** reference | **Section:** Operator

## Syntax
```
(1) Box AreaNum, [robotNumber], minX, maxX, minY, maxY, minZ, maxZ [localNumber]

(2) Box AreaNum, robotNumber, minX, maxX, minY, maxY, minZ, maxZ, remoteOutLogic [localNumber]

(3) Box AreaNum, robotNumber

(4) Box
```

## Parameters
AreaNum	Integer expression
		 representing the area number from 1 to 15.

robotNumber	Integer expression
		 that specifies which robot you want to configure.

If robotNumber
		 is omitted in syntax (1), the current robot number is used.

You cannot omit
		 robotNumber in syntax (2) and (3).

minX	The minimum
		 X coordinate position which can be set to the approach check area.

maxX	The maximum
		 X coordinate position which can be set to the approach check area.

minY	The minimum
		 Y coordinate position which can be set to the approach check area.

maxY	The maximum
		 Y coordinate position which can be set to the approach check area.

minZ	The minimum
		 Z coordinate position which can be set to the approach check area.

maxZ	The maximum
		 Z coordinate position which can be set to the approach check area.

Remote
		 output logic	Set the Remote
		 output logic.  To set I/O output to On when the Box approaches,
		 use On. To set I/O output to Off when the Box approaches, use
		 Off. When the parameter is omitted, On will be used.

[localNumber]	Specify the
		 local coordinate system number from 0 to 15.

Be sure to add
		 "/LOCAL" before the number.  When the parameter is omitted,
		 the local coordinate system number "0" will be used.

## Description
Box is used to set the approach check area. The approach check area is for checking approaches of the robot end effector in the approach check area. The position of the end effector is calculated by the current tool. The approach check area is set on the base coordinate system of the robot and is between the specified maximum and minimum X, Y, and Z.

When the approach check area is used, the system detects approaches in any motor power status during the controller is ON.

You can also use GetRobotInsideBox function or InsideBox function to get the result of the approach check. GetRobotInsideBox function can be used for wait condition of Wait command. You can provide the check result to the I/O by setting the remote output setting.

When several robots use one area, you should define the area from each robot coordinate system.

Configure the Box 1 from Robot 1 position

Box 1, 1, 100, 200, 0, 100, 0, 100

Lower limit of axes X, Y, Z is (100,0,0) and upper limit is (200,100,100)

Configure the Box 1 from Robot 2

Box 1, 2, -200, -100, 0, 100, 0, 100

Lower limit of axes X, Y, Z is (200,0,0) and upper limit is (-100,100,100)

Robot parameter data is stored in compact flash in controller.  Therefore, writing to command flash occurs when executing this command.  Frequent writing to compact flash affect to lifetime of compact flash.  We recommend to use this command minimally.

## Notes
Turning off Approach Check Area

You can turn off the approach check area of each coordinate axis. To turn off only the Z axis, define minZ and maxZ to be 0. For example Box 1, 200, 300, 0, 500, 0, 0.

In this case, it checks if the robot end effector is in the XY dimensional area.

Default Values of Approach Check Area

The default values for the Box statement are "0, 0, 0, 0, 0, 0". (Approach Check Area Checking is turned off.)

Tool Selection

The approach check is executed for the current tool. When you change the tool, the approach check may display the tool approach from inside to outside of the area or the other way although the robot is not operating.

Additional Axis

For the robot which has the additional ST axis (including the running axis), the approach check plane to set doesn't depend on the position of additional axis, but is based on the robot base coordinate system.

Tip

Set Box statement from Robot Manager

Epson RC+ has a point and click dialog box for defining the approach check area. The simplest method to set the Box values is by using the Box page on the Robot Manager.

## Examples
```spel
Box 1, 1, 100, 200, 0, 100, 0, 100
```

```spel
Box 1, 2, -200, -100, 0, 100, 0, 100
```

```spel
> Box 1, -200, 300, 0, 500, -100, 0
> Box
Box 1: 1, -200.000, 300.000, 0.000, 500.000, -100.000, 0.000, ON /LOCAL0
```

```spel
Function SetBox Integer i Box 1, -200, 300, 0, 500, -100, 0 /LOCAL1 i = 2 Box 2, 100, 200, 0, 100, -200, 100 /LOCAL(i)
Fend
```

## See Also
Specifies and displays the approach check area.

BoxClr

BoxDef

GetRobotInsideBox

InsideBox

Plane

Box Statement Example

[Example 1]

These are examples to set the approach check area using Box statement.

> Box 1, -200, 300, 0, 500, -100, 0

> Box

Box 1: 1, -200.000, 300.000, 0.000, 500.000, -100.000, 0.000, ON /LOCAL0

[Example 2]

The following is a simple program to set the Box values by specifying the local coordinate system numbers 1 and 2.

Function SetBox

  Integer i

  Box 1, -200, 300, 0, 500, -100, 0 /LOCAL1

  i = 2

  Box 2, 100, 200, 0, 100, -200, 100 /LOCAL(i)

Fend


---

# BoxClr
**Type:** reference | **Section:** Operator

## Syntax
```
BoxClr AreaNum [,robotNumber]
```

## Parameters
AreaNum	Integer expression representing the area number from 1 to 15.

robotNumber	Optional. Integer expression that specifies which robot you want to configure. If omitted, the current robot number is used.

## Description
Robot parameter data is stored in compact flash in controller.  Therefore, writing to command flash occurs when executing this command.  Frequent writing to compact flash affect to lifetime of compact flash.  We recommend to use this command minimally.

## Examples
```spel
Function ClearBox If BoxDef(1) = True Then
    BoxClr 1 EndIf
Fend
```

## See Also
Clears the definition of approach check area.

Box

BoxDef

GetRobotInsideBox

InsideBox

BoxClr Function Example

This example uses BoxClr function in a program.

Function ClearBox

  If BoxDef(1) = True Then

    BoxClr 1

  EndIf

Fend


---

# BoxDef
**Type:** reference | **Section:** Operator

## Syntax
```
BoxDef (AreaNum[, robotNumber])
```

## Parameters
AreaNum	Integer expression representing the area number from 1 to 15.

robotNumber	Integer expression representing a robot number you want to configure. If omitted, the current robot will be specified.

## Description
BoxDef

BoxDef Function

## Examples
```spel
Function ClearBox If BoxDef(1) = True Then
    BoxClr 1 EndIf
Fend
```

## See Also
Returns whether Box has been defined or not.

Box

BoxClr

InsideBox

BoxDef Function Example

This example uses BoxDef function in a program.

Function ClearBox

  If BoxDef(1) = True Then

    BoxClr 1

  EndIf

Fend


---

# Brake Function
**Type:** function | **Section:** Operator

## Syntax
```
Brake(jointNumber)
```

## Parameters
jointNumber	Integer expression representing the joint number.  Values are from 1 to the number of joints on the robot.

## Description
Brake Function

Brake Function

## Examples
```spel
If Brake(1) = Off Then
		  Print "Joint 1 brake is off"
		EndIf
```

## See Also
Returns brake status for specified joint.

Brake Statement

Brake Function Example

If Brake(1) = Off Then

		  Print "Joint 1 brake is off"

		EndIf


---

# Brake Statement
**Type:** statement | **Section:** Operator

## Syntax
```
Brake status, jointNumber
```

## Parameters
status	The keyword
		 On is used to turn the
		 brake on. The keyword Off
		 is used to turn the brake off.

jointNumber	The joint
		 number from 1 to 6.

## Description
The Brake command is used to turn brakes on or off for one joint of the 6 axis robot (including N series).

It's not available for SCARA Robot (include RS series).

This command is intended for use by maintenance personnel only.

When the Brake statement is executed, the robot control parameter is initialized.

See Motor On for the details.

WARNING	Use extreme caution when turning off
		 a brake.  Ensure that the joint is properly supported, otherwise
		 the joint can fall and cause damage to the robot and personnel.

Before releasing the brake, be ready to use the emergency stop switch so that you can immediately press it.  When the controller is in emergency stop status, the motor brakes are locked.
  Be aware that the robot arm may fall by its own weight when the brake is turned off with Brake command.

## Examples
```spel
> brake on, 1
```

```spel
> brake off, 1
```

## See Also
Turns brake on or off for specified joint of the current robot.

Brake Function

Motor

Power

Reset

SFree

SLock

Brake Example

> brake on, 1

> brake off, 1


---

# Byte Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Byte varName [( subscripts )] [, varName [( subscripts )]
```

## Parameters
varName	Variable name which the user wants to declare as type Byte.

subscripts	Optional.  Dimensions of an array variable; up to 3 dimensions may be declared.  The subscripts syntax is as follows

(ubound1, [ubound2], [ubound3])

ubound1, ubound2, ubound3 each specify the maximum upper bound for the associated dimension.

The elements in each dimension of an array are numbered from 0 and the available number of array elements is the upper bound value + 1.

When specifying the upper bound value, make sure the number of total elements is within the range shown below:

Local variable   2000

Global Preserve variable   4000

Global variable and module variable   100000

## Description
Byte is used to declare variables as type Byte.  Variables of type Byte can contain whole numbers ranging in value from -128 to +127.  Local variables should be declared at the top of a function.  Global and module variables must be declared outside of functions.

## Examples
```spel
Function Test Byte A(10) 'Single dimension array of byte Byte B(10, 10) 'Two dimension array of byte Byte C(5, 5, 5) 'Three dimension array of byte Byte test_ok test_ok = 15 Print "Initial Value of test_ok = ", test_ok test_ok = (test_ok And 8) If test_ok <> 8 Then
    Print "test_ok high bit is ON" Else
    Print "test_ok high bit is OFF" EndIf
Fend
```

## See Also
Data Types Overview

Variable Naming Conventions

Variable Declarations

Boolean

Double

Global

Int32

Integer

Long

Real

Short

String

UByte

UInt32

UShort

Byte Statement Example

The following example declares a variable of type Byte and then assigns a value to it.  A bitwise And is then done to see if the high bit of the value in the variable test_ok is On (1) or Off (0).  The result is printed to the display screen. (Of course in this example the high bit of the variable test_ok will always be set since we assigned the variable the value of 15.)

Function Test

  Byte A(10) 'Single dimension array of byte

  Byte B(10, 10) 'Two dimension array of byte

  Byte C(5, 5, 5) 'Three dimension array of byte

  Byte test_ok

  test_ok = 15

  Print "Initial Value of test_ok = ", test_ok

  test_ok = (test_ok And 8)

  If test_ok <> 8 Then

    Print "test_ok high bit is ON"

  Else

    Print "test_ok high bit is OFF"

  EndIf

Fend


---

# CFEnabled Property
**Type:** property | **Section:** Operator

## Description
Set whether to continue the force control functions to the next force guide object.

Values

False : Normal

Turn OFF the force control functions once, then execute the next force guide object.

True : When you want to execute the next force guide object with remaining a steady force after contacting:

The next force guide object must maintain the force control in the direction set in ContactOrient.

See Also: CFEnabled Property

Enabled Property

## See Also
Applies To

Contact Object


---

# CP Function
**Type:** function | **Section:** Operator

## Syntax
```
CP
```

## Description
CP Function

CP Function

See_Also Example

Returns status of path motion.

## Examples
```spel
If CP = Off Then
		  Print "CP is off"
		EndIf
```

## See Also
CP Statement

CP Function Example

If CP = Off Then

		  Print "CP is off"

		EndIf


---

# CP Keyword
**Type:** reference | **Section:** Operator

## Description
CP Keyword

CP Keyword

The CP keyword is used in these contexts:

CP Statement

CP Function


---

# CP Statement
**Type:** statement | **Section:** Operator

## Syntax
```
CP { On | Off }
```

## Parameters
On | Off	The keyword On is used to enable path motion. The keyword Off is used to disable CP mode.

## Description
CP (Continuous Path) motion mode can be used for the Arc, Arc3, Go, Jump, Jump3, Jump3CP and Move robot motion instructions.

When CP mode is On, each motion command executes the next statement as deceleration starts.  Continuous path motion will continue regardless of whether the CP parameter is specified in each motion command or not.

When CP is Off, this function is active only when the CP parameter is specified in each motion command.

When CP is On, path motion will continue without full deceleration between two CP motions (Arc, Arc3, Jump3, Jump3CP, Move), or two PTP motions (Go, Jump).

In contrast, full deceleration will occur between a CP motion and a PTP motion.

In addition, in the CP motion which target is wrist singular point in a vertical 6-axis robot (including the N series), the next motion and the motion trajectory will not be combined and full deceleration will occur.

CP will be set to Off in the following cases

Controller Startup

Motor On

SFree, SLock, Brake

Reset, Reset Error

Stop button or Quit All stops tasks

## Examples
```spel
CP On
Move P1
Move P2
CP Off
```

## See Also
CP Function

Arc

Go

Move

CP Statement Example

CP On

Move P1

Move P2

CP Off


---

# CP motion priority
**Type:** reference | **Section:** Operator

## Description
CP motion priority

CP Motion Speed / Acceleration and Tool Orientation

When you attempt to change only the tool orientation while keeping the tool tip of the robot arm at the specified coordinate point or when the tool orientation variation is larger than the travel distance of the tool tip, moving the arm by normal CP motion commands will cause an increase in the variation of speed, acceleration and deceleration of tool orientation.  In some cases, an error will occur.

To prevent these situations, add the ROT parameter to the CP motion commands.  The arm will be moved based on the specified angular velocity and acceleration/deceleration of the main axis regarding the orientation variation.

The angular velocity and acceleration/deceleration of the main axis regarding the orientation variation should be specified with the SpeedR and AccelR commands in advance.

For example:

SpeedR 50 ' degree/sec

AccelR 200, 200 ' degree/sec2

Move P1 ROT

Note:  The tool orientation variation is normally comprised of orientation variations of more than one rotation axis.

The SpeedR and AccelR parameters specify the angular velocity and acceleration/deceleration of the main axis regarding the orientation variation.  Therefore, actual angular velocity and acceleration/deceleration of the orientation variation are different from the parameters except for the case where the rotation axis of the orientation is only one.

While the motion command with the ROT parameter is executed, the specified SpeedS and AccelS parameters are invalid.

The ROT parameter can be used with the following motion commands:

Move	BMove

Arc	TMove

Arc3	Jump3CP

## Examples
```spel
SpeedR 50 ' degree/sec
```

```spel
AccelR 200, 200 ' degree/sec2
```

```spel
Move P1 ROT
```


---

# CTReset Statement
**Type:** reference | **Section:** Operator

## Syntax
```
CTReset(bitNumber)
```

## Parameters
bitNumber	Number of the input bit set as a counter. This must be an integer expression representing a valid Hardware input bit. Only 16 counters can be active at the same time.

## Description
CTReset works with the CTR function to allow inputs to be used as counters.  CTReset sets the specified input bit as a counter and then starts the counter.
  If the specified input is already used as a counter, it is reset and started again.

## Notes
Turning Off Power and It's Effect on H/W Counters

Turning off main power releases all counters.

Using the Ctr Function

Use the Ctr function to retrieve current Hardware Input counter values.

## Examples
```spel
CTReset 3 'Reset Counter 3 to 0

On 0 'Turn an output switch on

Do While Ctr(3) < 5

Loop

Off 0 'When 5 input cycles are counted for Input 3 turn

'switch off (output 0 off)
```

## See Also
Ctr

CTReset Statement Example

The following example shows a sample of code which could be used to get a hardware input counter value.

CTReset 3 'Reset Counter 3 to 0

On 0 'Turn an output switch on

Do While Ctr(3) < 5

Loop

Off 0 'When 5 input cycles are counted for Input 3 turn

'switch off (output 0 off)


---

# CVMove Statement
**Type:** reference | **Section:** Operator

## Syntax
```
CVMove fileName [CP] [searchExpr]
```

## Parameters
fileName	String expression for the path and name of the file to use for the continuous path motion data. This file must be previously created by the Curve instruction and stored on a PC hard disk.

You cannot specify a file path and fileName doesn't have any effect from ChDisk. See ChDisk for the details.

CP	Optional. Specifies continuous path motion after the last point.

searchExpr	Optional. A Till or Find expression.

Till | Find

Till Sw(expr) = {On | Off}

Find Sw(expr) = {On | Off}

## Description
CVMove performs the continuous spline path motion defined by the data in the file fileName, which is located in the controller memory. The file must be previously created with the Curve command.

Multiple files may exist at the same time on the system.  If the file name does not have an extension, .CVT is added automatically.

The user can change the speed and acceleration for the continuous path motion for CVMove by using the Speeds and AccelS instructions.

When the Curve instruction has been previously executed using points with Local definitions, you can change the operating position by using the Local instruction.

When executing CVMove, be careful that the robot doesn't collide with peripheral equipment.  When you attempt to change the hand orientation of the 6-axis robot (including N series) between adjacent points suddenly, due to the nature of cubic spline function, the 6-axis robot may start changing its orientation from the previous and following points and move in an unexpected trajectory.  Verify the trajectory thoroughly prior to a CVMove execution and be careful that the robot doesn't collide with peripheral equipment.

Specify points closely to each other and at equal intervals.  Do not change the hand (arm) orientation between adjacent points suddenly.

The CP parameter causes acceleration of the next motion command to start when the deceleration starts for the current motion command.  In this case the robot will not stop at the destination coordinate and will continue to move to the next point.

## Examples
```spel
Set up curve
```

```spel
> curve "mycurve", O, 0, 4, P1, P2, On 2, P(3:7)
```

```spel
Move the arm to P1 in a straight line
```

```spel
> jump P1
```

```spel
Move the arm according to the curve definition called mycurve
```

```spel
> cvmove "mycurve"
```

## See Also
Robot motion commands

AccelS

Arc

Curve

Move

Speeds

CVMove Example

The following example designates the free curve data file name as MYCURVE.CVT, creates a curve tracing P1-P7, switches ON output port 2 at P2, and decelerates the arm at P7.

Set up curve

> curve "mycurve", O, 0, 4, P1, P2, On 2, P(3:7)

Move the arm to P1 in a straight line

> jump P1

Move the arm according to the curve definition called mycurve

> cvmove "mycurve"


---

# CX, CY, CZ, CU, CV, CW, CR, CS, CT Functions
**Type:** function | **Section:** Operator

## Syntax
```
CX( point )

CY( point )

CZ( point )

CU( point )

CV( point )

CW( point )

CR(point)

CS(point)

CT(point)
```

## Parameters
point	Point expression.

## Description
Used to retrieve an individual coordinate value from a point.

To obtain the current X-Axis position of the robot, use Here for the point parameter.

## Examples
```spel
Function cxtest Real x x = CX(pick) Print "The X Axis Coordinate of point 'pick' is", x
Fend
```

## See Also
Point Expression

CX, CY, CZ, CU, CV, CW, CR, CS, CT Statements

CX, CY, CZ, CU, CV, CW, CR, CS, CT Functions Example

The following example extracts the X Axis coordinate value from point "pick" and puts the coordinate value in the variable x.

Function cxtest

  Real x

  x = CX(pick)

  Print "The X Axis Coordinate of point 'pick' is", x

Fend


---

# CX, CY, CZ, CU, CV, CW, CR, CS, CT Keywords
**Type:** reference | **Section:** Operator

## Description
CX, CY, CZ, CU, CV, CW, CR, CS, CT Keywords

CX, CY, CZ, CU, CV, CW, CR, CS, CT Keywords

The CX, CY, CZ, CU, CV, CW, CR, CS, CT keywords are used in these contexts:

CX, CY, CZ, CU, CV, CW, CR, CS, CT Statements

CX, CY, CZ, CU, CV, CW, CR, CS, CT Functions


---

# CX, CY, CZ, CU, CV, CW, CR, CS, CT Statements
**Type:** statement | **Section:** Operator

## Syntax
```
CX( point ) = value

CY( point ) = value

CZ( point ) = value

CU( point ) = value

CV( point ) = value

CW( point ) = value

CR( point ) = value

CS( point ) = value

CT( point ) = value
```

## Parameters
point	P number or P(expr) or point label.

value	Real expression representing the new coordinate value in millimeters.

## Description
CX, CY, CZ, CU, CV, CW, CR, CS, CT Statements

CX, CY, CZ, CU, CV, CW, CR, CS, CT Statements

See_Also Example

Sets the coordinate of a point data.

CV, CW are for only 6-axis robots (including N series).

CR is only for Joint type robots.

CS, CT are only for robots with additional axes.

## Examples
```spel
CX(pick) = 25.34
```

## See Also
CX, CY, CZ, CU, CV, CW, CR, CS, CT Functions

CX, CY, CZ, CU, CV, CW, CR, CS, CT Statements Example

CX(pick) = 25.34


---

# Call Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Call funcName [(argList)]
```

## Parameters
funcName	The name of
		 a Function
		 which is being called.

argList	Optional.
		  List of arguments that were specified in the Function declaration.

For the argument,
		 use the following syntax:

[ByRef]
		 varName [( )], or numerical expression

ByRefOptional.
		 Specify ByRef when you refer to the variable to be seen by the
		 calling function. In this case, the argument change in a function
		 can be reflected to the variable of the calling side. You can
		 change the values received as a reference.

## Description
The Call instruction causes the transfer of program control to a function (defined in Function...Fend).  This means that the Call instruction causes program execution to leave the current function and transfer to the function specified by Call.  Program execution then continues in that function until an Exit Function or Fend instruction is reached.  Control is then passed back to the original calling function at the next statement after the Call instruction.

You may omit the Call keyword and argument parentheses.
  For example, here is a call statement used with or without the Call keyword:

Call MyFunc(1, 2)

MyFunc 1, 2

You can call an external function in a dynamic link library (DLL). For details, refer to Declare Statement.

To execute a subroutine within a function, use GoSub...Return.

You can specify a variable as an argument. Specifying the ByRef parameter, you can reflect the change of argument in the function to the variable of the calling side.

When specifying the ByRef parameter, you need to specify ByRef as well for the argument list of the function definition (Function statement) and DLL function definition (Declare statement).

ByRef is necessary when giving an array variable as an argument.

## Examples
```spel
Call MyFunc(1, 2)
```

```spel
MyFunc 1, 2
```

```spel
Function main Call InitRobot
Fend
```

```spel
Function InitRobot If Motor = Off then
    Motor On EndIf Power High Speed 50 Accel 75,75
Fend
```

## See Also
Function...Fend

GoSub

Call Statement Example

[File1: MAIN.PRG]

Function main

  Call InitRobot

Fend

[File2: INIT.PRG]

Function InitRobot

  If Motor = Off then

    Motor On

  EndIf

  Power High

  Speed 50

  Accel 75,75

Fend


---

# ChkCom Function
**Type:** reference | **Section:** Operator

## Syntax
```
ChkCom (portNumber As Integer)
```

## Parameters
portNumber	Integer value that specifies the RS-232C port number

Real Part1 ~ 8

Windows Part 1001 ~ 1008

## Description
ChkCom Function

ChkCom Function

See_Also Example

Returns number of characters in the reception buffer of a communication port

## Examples
```spel
Integer numChars
numChars = ChkCom(1)
```

## See Also
CloseCom

OpenCom

Read

Write

ChkCom Function Example

Integer numChars

numChars = ChkCom(1)


---

# ChkNet Function
**Type:** reference | **Section:** Operator

## Syntax
```
ChkNet (portNumber As Integer)
```

## Parameters
portNumber	TCP/IP port number (201 ~ 216)

## Description
ChkNet Function

ChkNet Function

See_Also Example

Returns number of characters in the reception buffer of a network port.

## Examples
```spel
Integer numChars

numChars = ChkNet(201)
```

## See Also
CloseNet

OpenNet

Read

SetNet

Write

ChkNet Function Example

Integer numChars

numChars = ChkNet(201)


---

# Chr$ Function
**Type:** reference | **Section:** Operator

## Syntax
```
Chr$ (number)
```

## Parameters
number	An integer expression between 1 and 255.

## Description
Chr$ returns a character string (1 character) having the ASCII value of the parameter number. When the number specified is outside of the range 1-255 an error will occur.

## Examples
```spel
Function Test String temp$ temp$ = Chr$(&H41) + Chr$(&H42) + Chr$(&H43) Print "The value of temp = ", temp$
Fend
```

## See Also
Asc

InStr

Left$

Len

Mid$

Right$

Space$

Str$

Val

Chr$ Function Example

The following example declares a variable of type String and then assigns the string "ABC" to it. The Chr$ instruction is used to convert the numeric ASCII values into the characters "A", "B" and "C". The &H means the number following is represented in hexadecimal form. (&H41 means Hex 41)

Function Test

  String temp$

  temp$ = Chr$(&H41) + Chr$(&H42) + Chr$(&H43)

  Print "The value of temp = ", temp$

Fend


---

# Circular Interpolation Definition
**Type:** reference | **Section:** Operator

## Description
Circular Interpolation Definition

Circular Interpolation

Circular Interpolation is a type of curved motion where an arc is defined with 3 points and the arm moves in an circular fashion through the 3 points until it finally arrives on the 3rd point.
  Circular Interpolated motion is normally used in process applications like dispensing.


---

# ClearPoints Command
**Type:** reference | **Section:** Operator

## Syntax
```
ClearPoints
```

## Description
ClearPoints initializes the position data area for the current robot. Use this instruction to erase point definitions which reside in memory before teaching new points.

## Examples
```spel
>P1=100,200,-20,0/R
```

```spel
>P2=0,300,0,20/L
```

```spel
>Plist
```

```spel
P1=100,200,-20,0/R
```

```spel
P2=0,300,0,20/L
```

```spel
>clearpoints
```

```spel
>Plist
```

```spel
>
```

## See Also
Plist

ClearPoints Statement Example

The example below shows simple examples of using the ClearPoints command (from the command Window). Notice that no teach points are shown when initiating the Plist command once the ClearPoints command is given.

>P1=100,200,-20,0/R

>P2=0,300,0,20/L

>Plist

P1=100,200,-20,0/R

P2=0,300,0,20/L

>clearpoints

>Plist

>


---

# CloseCom Statement
**Type:** reference | **Section:** Operator

## Syntax
```
CloseCom #portNum | All
```

## Parameters
portNum	RS-232C port number to close.

Real Part 1 ~ 8

Windows Part 1001 ~ 1008

If All is specified, the task will close all the open RS-232C port.

## Description
CloseCom Statement

CloseCom Statement

See_Also Example

Close the communication port previously opened with OpenCom.

## Examples
```spel
CloseCom #1
```

## See Also
ChkCom

OpenCom

CloseCom Statement Example

CloseCom #1


---

# CloseNet Statement
**Type:** reference | **Section:** Operator

## Syntax
```
CloseNet #portNumber | All
```

## Parameters
portNumber	TCP/IP port number to close ( 201 ~ 216)

If All is specified, the task will close all the open TCP/IP port.

## Description
CloseNet Statement

CloseNet Statement

See_Also Example

Close the network port previously opened with OpenNet.

## Examples
```spel
CloseNet #201
```

## See Also
ChkNet

OpenNet

CloseNet Statement Example

CloseNet #201


---

# Code Number 2000 to 2999
**Type:** reference | **Section:** Operator

## Description
Code Number 2000 to 2999

Code Number 2000 to 2999

To get help for any SPEL+ error, place the cursor on the error message in the run or command windows and press the F1 key.

No.	Message	Remedy	Note 1	Note 2

2000	Unsupported. Unsupported command was
		 attempted.	Rebuild the project.

When this message appears while the Health
		 ** command or Health ** function is used, robot maintenance data
		 may have been disabled. Check the settings.

(Reference: Epson RC+ 8.0 User's Guide

5.13.2 [System Configuration] Command
		 (Setup Menu)

[Setup]-[System Configuration]-[Controller]-[Preferences]
		 Page)

2001	Unsupported. Unsupported motion command
		 was attempted.	Rebuild the project.

2002	Unsupported. Unsupported conveyer
		 command was attempted.	Rebuild the project.

2003	Unsupported. Unsupported Function
		 argument was specified.	Rebuild the project.

2004	Unsupported. Unsupported Function
		 return value was specified.	Rebuild the project.

2005	Unsupported. Unsupported condition
		 was specified.	Rebuild the project.

2006	Unsupported. Unsupported I/O command
		 was specified.	Rebuild the project.

2007	Unsupported condition was specified.	Rebuild the project.

2008	Unsupported. Unknown error number.	Rebuild the project.

2009	Unsupported. Invalid Task number.	Rebuild the project.

2010	Object file error. Build the project.
		 Out of internal code range.	Rebuild the project.

2011	Object file error. Build the project.
		 Function argument error.

Invalid function parameter value	Rebuild the project.

Part Feeding:

Wrong command format or value settings.

Read the description for the corresponding
		 command provided in

Part Feeding 8.0  Introduction &
		 Hardware (Common) & Software

Software 3.  Part Feeding SPEL+ Command
		 Reference and correct the code.

2012	Object file error. Build the project.
		 Command argument error.

Invalid command parameter value	Rebuild the project.

Part Feeding:

Wrong command format or value settings.

Read the description for the corresponding
		 command provided in

Part Feeding 7.0  Introduction &
		 Hardware (Common) & Software

Software 3.  Part Feeding SPEL+ Command
		 Reference and correct the code.

2013	Object file error. Build the project.
		 Cannot process the code.	Rebuild the project.

2014	Object file error. Build the project.
		 Cannot process the variable type code.	Rebuild the project.

2015	Object file error. Build the project.
		 Cannot process the string type code.	Rebuild the project.

2016	Object file error. Build the project.
		 Cannot process the variable category code.	Rebuild the project.

2017	Object file error. Build the project.
		 Cannot process because of improper code.	Rebuild the project.

2018	Object file error. Build the project.
		 Failed to calculate the variable size.	Rebuild the project.

2020	Stack table number exceeded. Function
		 call or local variable is out of range.	Check whether the nested structure
		 is called infinitely. Reduce the nested structure calls depth.

2021	Stack area size exceeded. Stack error.
		 Function call or local variable is out of range.	If using many local variables, especially
		 String type, replace them to global variables.

2022	Stack failure. Required data not found
		 on the stack.	Rebuild the project.

2023	Stack failure. Unexpected tag found
		 on the stack.	Rebuild the project.

2024	Stack area size exceeded. Local variable
		 is out of range.	Change the size of the Local variable.

2025	Object file error. Invalid function
		 call.	Rebuild the project.

2031	System failure. Robot number is beyond
		 the maximum count.	Restore the controller configuration.

2032	System failure. Task number compliance
		 error.	Rebuild the project.

2033	System failure. Too many errors.	Remedy the errors occurring frequently.

2040	Thread failure. Failed to create the
		 thread.	Reboot the controller.

2041	Thread failure. Thread creation timeout.	Reboot the controller.

2042	Thread failure. Thread termination
		 timeout.	Reboot the controller.

2043	Thread failure. Thread termination
		 timeout.	Reboot the controller.

2044	Thread failure. Daemon process timeout.	Reboot the controller.

2045	Thread failure. Task continuance wait
		 timeout.	Reboot the controller.

2046	Thread failure. Task stop wait timeout.	Reboot the controller.

2047	Thread failure. Task startup wait
		 timeout.	Reboot the controller.

2050	Object file operation failure. Object
		 file size is beyond the allowable size.	Rebuild the project.

2051	Object file operation failure. Cannot
		 delete the object file during execution.	Reboot the controller.

2052	Object file operation failure. Cannot
		 allocate the memory for the object file.	Reboot the controller.

2053	Object file operation failure. Object file cannot be accessed while
		 it is updating.	Perform the same processing after
		 a while.  Rebuild the project.

2054	Object file operation failure. Function
		 ID failure. Rebuild the project.	Synchronize the files of the project.
		  Rebuild the project.

2055	Object file operation failure. Local
		 variable ID failure. Rebuild the project.	Synchronize the files of the project.
		  Rebuild the project.

2056	Object file operation failure. Global
		 variable ID failure. Rebuild the project.	Synchronize the files of the project.
		  Rebuild the project.

2057	Object file operation failure. Global
		 Preserve variable ID failure. Rebuild the project.	Synchronize the files of the project.
		  Rebuild the project.

2058	Object file operation failure. Failed
		 to calculate the variable size.	Synchronize the files of the project.
		  Rebuild the project.

2059	Exceed the global variable area. Cannot
		 assign the Global variable area because it failed to allocate
		 memory.	Reduce the number of Global variables
		 to be used.

2070	SRAM failure. SRAM is not mapped.	Replace the CPU board.

2071	SRAM failure. Cannot delete when Global
		 Preserve variable is in use.	Perform the same processing after
		 a while.  Rebuild the project.

2072	Exceed the backup variable area. Cannot
		 assign the Global Preserve variable area because it failed to
		 allocate memory.	Reduce the number of Global Preserve
		 variables to be used.	Maximum size	The size you attempted to use

2073	SRAM failure. Failed to clear the
		 Global Preserve variable area.	Rebuild the project.

2074	SRAM failure. Failed to clean up the
		 Global Preserve variable save area.	Reboot the controller.

2100	Initialization failure. Failed to
		 open the initialization file.	Restore the controller configuration.

2101	Initialization failure. Duplicated
		 initialization.	Reboot the controller.

2102	Initialization failure. Failed to
		 initialize MNG.	Reboot the controller.

2103	Initialization failure. Failed to
		 create an event.	Reboot the controller.

2104	Initialization failure. Failed to
		 setup a priority.	Reboot the controller.

2105	Initialization failure. Failed to
		 setup the stack size.	Reboot the controller.

2106	Initialization failure. Failed to
		 setup an interrupt process.	Reboot the controller.

2107	Initialization failure. Failed to
		 start an interrupt process.	Reboot the controller.

2108	Initialization failure. Failed to
		 stop an interrupt process.	Reboot the controller.

2109	Initialization failure. Failed to
		 terminate MNG.	Reboot the controller.

2110	Initialization failure. Failed to
		 allocate memory.	Reboot the controller.

2111	Initialization failure. Failed to
		 initialize motion.	Restore the controller configuration.

2112	Initialization failure. Failed to
		 terminate motion.	Reboot the controller.

2113	Initialization failure. Failed to
		 map SRAM.	Replace the CPU board.

2114	Initialization failure. Failed to
		 register SRAM.	Replace the CPU board.

2115	Initialization failure. Fieldbus board
		 is beyond the maximum count.	Check the number of fieldbus boards.

2116	Initialization failure. Failed to
		 initialize fieldbus.	Reboot the controller.

Check the fieldbus board.

Replace the fieldbus board.

2117	Initialization failure. Failed to
		 terminate fieldbus.	Reboot the controller.

2118	Initialization failure. Failed to
		 open motion.	Restore the controller configuration.

2119	Initialization failure. Failed to
		 initialize conveyor tracking.	Make sure the settings of conveyor
		 and encoder are correct.

2120	Initialization failure. Failed to
		 allocate the system area.	Reboot the controller.

2121	Initialization failure. Failed to
		 allocate the object file area.	Reboot the controller.

2122	Initialization failure. Failed to
		 allocate the robot area.	Reboot the controller.

2123	Initialization failure. Failed to
		 create event.	Reboot the controller.

2124	Initialization failure.

An unsupported Fieldbus module is installed.	Install the Fieldbus module purchased
		 from SEC.

2126	The settings are initialized since
		 the initial setting file is corrupted.  Restore the system.	Since the initial setting file has
		 significantly corrupted, the initial setting file of factory-default
		 is used.

2130	MCD failure. Failed to open the MCD
		 file.	Restore the controller configuration.

2131	MCD failure. Failed to map the MCD
		 file.	Restore the controller configuration.

2132	PRM failure. PRM file cannot be found.	Restore the controller configuration.

2133	PRM failure. Failed to map the PRM
		 file.	Restore the controller configuration.

2134	PRM failure. PRM file contents error.	Restore the controller configuration.

2135	PRM failure. Failed to convert the
		 PRM file.	Reboot the controller.

2136	PRM failure.

Failed to convert the PRM file.	Reboot the controller.

2137	PRM failure.

Failed to convert the PRM file.	Reboot the controller.

2140	DU lnit Error. Cannot use drive units.	Communication with drive units is
		 not available for the virtual controllers.  Return the configuration
		 file to original setting if it was changed.

2141	DU Init Error. Failed to initialize
		 drive units.	Check the connection with drive units.

2142	DU Init Error. Failed to initialize
		 drive units.	Check the connection with drive units.

2143	DU Init Error. Timeout during initialization
		 of drive units.	Check the connection with drive units.

2144	DU Init Error. No data to download
		 to drive units.	Reboot the control unit and drive
		 units.

2145	DU Init Error. Failed to start communication
		 with drive units.	Reboot the control unit and drive
		 units.

2146	DU Init Error. Timeout when starting
		 communication with drive units.	Reboot the control unit and drive
		 units.

2147	DU Init Error. Failed to update the
		 drive units software.	Review the software update setting.

Check the connection with the Drive Unit.

2148	DU Init Error. Failed to update the
		 drive units software.	Check the file name.

Check the update file.

2149	DU Init Error. Failed to update the
		 drive units software.	Check the Drive Unit power and connection.

Reboot the Controller.

2150	Operation failure. Task number cannot
		 be found.	Reboot the Controller.

2151	Operation failure. Executing the task.	Reboot the Controller.

2152	Operation failure. Object code size
		 failure.	Reboot the Controller.

2153	Operation failure. Jog parameter failure.	Reboot the Controller.

2154	Operation failure. Executing jog.	Reboot the Controller.

2155	Operation failure. Cannot execute
		 the jog function.	Reboot the Controller.

2156	Operation failure. Jog data is not
		 configured.	Reboot the Controller.

2157	Operation failure. Failed to change
		 the jog parameter.	Reboot the Controller.

2158	Operation failure. Failed to allocate
		 the area for the break point.	Reboot the Controller.

2159	Operation failure. Break point number
		 is beyond the allowable setup count.	Reduce the break points.

2160	Operation failure. Failed to allocate
		 the function ID.	Reboot the Controller.

2161	Operation failure. Failed to allocate
		 the local variable address.	Reboot the Controller.

2162	Operation failure. Not enough buffer
		 to store the local variable.	Review the size of the Local variable.

2163	Operation failure. Value change is
		 available only when the task is halted.	Halt the task by the break point.

2164	Operation failure. Failed to allocate
		 the global variable address.	Review the size of the global variable.

2165	Operation failure. Not enough buffer
		 to store the global variable.	Review the size of the global variable.

2166	Operation failure. Failed to obtain
		 the Global Preserve variable address.	Review the size of the global preserve
		 variable.

2167	Operation failure. Not enough buffer
		 to store the Global Preserve variable.	Review the size of the global preserve
		 variable.

2168	Operation failure. SRAM is not mapped.	Reboot the Controller.

2169	Operation failure. Cannot clear the
		 Global Preserve variable when loading the object file.	Reboot the Controller.

2170	Operation failure. Not enough buffer
		 to store the string.	Check the size of the string variable.

2171	Operation failure. Cannot start the
		 task after low voltage was detected.	Check the controller power.

Reboot the Controller.

2172	Operation failure. Duplicated remote
		 I/O configuration.	Reboot the Controller.

2173	Remote setup error. Cannot assign
		 non-existing input number to remote function.	Check the I/O input number.

2174	Remote setup error. Cannot assign
		 non-existing output number to remote function.	Check the I/O output number.

2175	Operation failure. Remote function
		 is not configured.	Reboot the Controller.

2176	Operation failure. Event wait error.	Reboot the Controller.

2177	Operation failure. System backup failed.	Reboot the Controller.

Install the Controller firmware.

2178	Operation failure. System restore
		 failed.	Reboot the Controller.

Install the Controller firmware.

2179	Remote setup error. Cannot assign
		 same input number to some remote functions.	Check the remote setting.

2180	Remote setup error. Cannot assign
		 same output number to some remote functions.	Check the remote setting.

2181	Operation failure. Task
		 number has not been reserved for RC+ API.	Set the number of RC+API tasks.

2190	Cannot calculate because it was queue
		 data.	Review the program.

2191	Cannot execute AbortMotion because
		 robot is not running from a task.	If you don't operate the robot from
		 a program, you cannot use AbortMotion.

2192	Cannot execute AbortMotion because
		 robot task is already finished.	Task is completed.

Review the program.

2193	Cannot execute Recover without motion
		 because AbortMotion was not executed.	Execute AbortMotion in advance to
		 execute Recover WithoutMove.

2194	Conveyor setting error.	Make sure the settings of conveyor
		 and encoder are correct.

2195	Conveyor setting error.	Make sure the settings of conveyor
		 and encoder are correct.

2196	Conveyor number is out of range.	Make sure the settings of conveyor
		 and encoder are correct.

2197	Command parameter prohibited for conveyor
		 tracking motion was used.	Delete LJM.

No.	Message	Remedy	Note 1	Note2

2200	Robot in use. Cannot execute the motion
		 command when other tasks are using the robot.	The motion command for the robot cannot
		 be simultaneously executed from more than one task.  Review
		 the program.

2201	Robot does not exist.	Check whether the robot setting is
		 performed properly.  Restore the controller configuration.

2202	Motion control module status failure.
		 Unknown error was returned.	Rebuild the project.

2203	Cannot clear local number '0'.	The Local number 0 cannot be cleared.
		  Review the program.

2204	Cannot clear an arm while in use.	The Arm cannot be cleared while it
		 is in use.  Check whether the Arm is not used.	The Arm number you attempted to clear

2205	Cannot clear arm number '0'.	The Arm number 0 cannot be cleared.
		  Review the program.

2206	Cannot clear a tool while in use.	The Tool cannot be cleared while it
		 is in use.  Check whether the Tool is not used.	The Tool number you attempted to clear

2207	Cannot clear tool number '0'.	The Tool number 0 cannot be cleared.
		  Review the program.

2208	Cannot clear ECP '0'.	The ECP number 0 cannot be cleared.
		  Review the program.

2209	Cannot clear an ECP while in use.	The ECP cannot be cleared while it
		 is in use.  Check whether the ECP is not used.	The ECP number you attempted to clear

2210	Cannot specify '0' as the local number.	The command processing the Local cannot
		 specify the Local number 0.  Review the program.

2211	Cannot clear VRT ' 0 '.	You cannot clear VRT number '0'. Review
		 the program.

2212	Cannot clear the specified VRT number
		 while in use.	You cannot clear the VRT in use. Make
		 sure that the VRT is not in use.	VRT number

2214	VRT number is out of range.	You can choose 1 to 15 for a VRT number.
		 Adjust the program.

2215	Parameter is not defined in specified
		 VRT number.	Parameters are not defined in the
		 specified VRT number. Adjust the VRT number.

2216	Box number is out of range.	Available Box numbers are from 1 to
		 15.  Review the program.

2217	Box number is not defined.	Specified Box is not defined.

Review the Box number.

2218	Plane number is out of range.	Available Plane numbers are from 1
		 to 15.  Review the program.

2219	Plane number is not defined.	Specified Plane is not defined.  Review
		 the Plane number.

2220	PRM failure. No PRM file data is found.	Reboot the controller.  Restore
		 the controller configuration.

2221	PRM failure. Failed to flash the PRM
		 file.	Reboot the controller.  Restore
		 the controller configuration.

2222	Local number is not defined.	Check the Local setting.  Review
		 the program.	The specified Local number

2223	Local number cannot be found.	Available Local number is from 1 to
		 15.  Review the program.	The specified Local number

2224	Unsupported.  MCOFS is not defined	-

2225	CalPls is not defined.	Check the CalPls setting.

2226	Arm number is out of range.	Available Arm number is from 0 to
		 15.  Depending on commands, the Arm number 0 is not available.
		  Review the program.	The specified Arm number

2227	Arm number is not defined.	Check the Arm setting.  Review
		 the program.	The specified Arm number

2228	Pulse for the home position is not
		 defined.	Check the HomeSet setting.

2229	Tool number cannot be found.	Available Tool number is from 0 to
		 15.  Depending on commands, the Tool number 0 is not available.
		  Review the program.	The specified Tool number

2230	Tool number is not defined.	Check the Tool setting.  Review
		 the program.	The specified Tool number

2231	ECP number cannot be found.	Available Tool number is from 0 to
		 15.  Depending on commands, the Tool number 0 is not available.
		  Review the program.	The specified ECP number

2232	ECP number is not defined.	Check the ECP setting.  Review
		 the program.	The specified ECP number

2233	Axis to reset the encoder was not
		 specified.	Be sure to specify the axis for encoder
		 reset.

2234	Cannot reset the encoder with motor
		 in the on state.	Turn the motor power OFF before reset.

2235	XYLIM is not defined.	Check the XYLim setting.  Review
		 the program.

2236	PRM failure. Failed to set up the
		 PRM file contents to the motion control status module.	Reboot the controller.  Restore
		 the controller configuration.

2237	Pallet number is our of range.	Available Pallet numbers are from
		 0 to 15.  Review the program.

2238	Pallet is not defined.	Check the Pallet setting.

2240	Array subscript is out of user defined
		 range. Cannot access or update beyond array bounds.	Check the array subscript.  Review
		 the program.	The dimensions exceeding the definition	The specified subscript

2241	Dimensions of array do not match the
		 declaration.	Check the array's dimensions.  Review
		 the program.

2242	Zero '0' was used as a divisor.	Review the program.

2243	Variable overflow. Specified variable
		 was beyond the maximum allowed value.	Check the variable type and calculation
		 result.  Review the program.

2244	Variable underflow. Specified variable
		 was below the minimum allowed value.	Check the variable type and calculation
		 result.  Review the program.

2245	Cannot execute this command with a
		 floating point number.	This command cannot be executed for
		 Real or Double type.  Review the program.

2246	Cannot calculate the specified value
		 using the Tan function.	Check the specified value.  Review
		 the program.	The specified value

2247	Specified array subscript is less
		 than '0'.	Check the specified value.  Review
		 the program.	The specified value

2248	Array failure. Redim can only be executed
		 for an array variable.	You attempted to Redim the variable
		 that is not array.  Rebuild the project.

2249	Array failure. Cannot specify Preserve
		 for other than a single dimension array.	Other than a single dimension array
		 was specified as Preserve for Redim.  Rebuild the project.

2250	Array failure. Failed to calculate
		 the size of the variable area.	Rebuild the project.

2251	Cannot allocate enough memory for
		 Redim statement.	Reduce the number of subscripts to
		 be specified for Redim.  Perform Redim modestly.

2252	Cannot allocate enough memory for
		 ByRef.	Reduce the number of array's subscripts
		 to be seen by ByRef.

2253	Cannot compare characters with values.	Check whether the string type and
		 the numeric data type are not compared.  Review the program.

2254	Specified data is beyond the array
		 bounds. Cannot refer or update beyond the array bounds.	Check the number of array's subscripts
		 and data.  Review the program.	The number of array subscripts	The number of data to be referred
		 or updated

2255	Variable overflow or underflow. Specified
		 variable is out of value range.	The value that exceeds the range of
		 Double type is specified.  Review the program.

2256	Specified array subscript is beyond
		 the maximum allowed range.	Reduce the number of subscripts to
		 be specified.  For available subscripts, see the online help.

2257	Cannot specify Int64 variable or UInt64
		 variable.	Int64 variable or UInt64 variable
		 cannot be specified.  Correct the program.

2260	Task number is out of the available
		 range.	For available task number, see the
		 online help.  Review the program.

2261	Specified task number does not exist.	Review the program.

2262	Robot number is out of the available
		 range.	The available Robot number is 1.  Review
		 the program.

2263	Output number is out of the available
		 range. The Port No. or the Device No. is out of the available
		 range.	For available output number, see the
		 online help.  Review the program.

2264	Command
		 argument is out of the available range. Check the arguments. Added
		 data 1
 Passed
		 value. Added data 2  argument order.

Command
		 parameter out of range	For available range of argument, see
		 the online help.  Review the program.

Part Feeding:

Wrong command format or value settings.

Read the description for the corresponding
		 command provided in

Part Feeding 7.0  Introduction &
		 Hardware (Common) & Software

Software 3.  Part Feeding SPEL+ Command
		 Reference and correct the code.

2265	Joint number is out of the available
		 range.	Available Joint number is from 1 to
		 9.  Review the program.

2266	Wait time is out of available range.	Available wait time is from 0 to 2147483.
		  Review the program.

2267	Timer number is out of available range.	Available timer number is from 0 to
		 15.  Review the program.

2268	Trap number is out of available range.	Available trap number is from 1 to
		 4.  Review the program.

2269	Language ID is out of available range.	For available language ID, see the
		 online help.  Review the program.

2270	Specified D parameter value for the
		 parallel process is out of available range.	Available D parameter value is from
		 0 to 100.  Review the program.

2271	Arch number is out of available range.	Available arch number is from 0 to
		 7.  Review the program.

2272	Device No. is out of available range.	The specified number representing
		 a control device or display device is out of available range.
		  For available device number, see the online help.  Review
		 the program.

2273	Output data is out of available range.	Available output data value is from
		 0 to 255.  Review the program.

2274	Asin argument is out of available
		 range. Range is from -1 to 1.	Review the program.

2275	Acos argument is out of available
		 range. Range is from -1 to 1.	Review the program.

2276	Sqr argument is out of available range.	Review the program.

2277	Randomize argument is out of available
		 range.	Review the program.

2278	Sin, Cos, Tan argument is out of available
		 range.	Review the program.

2280	Timeout period set by the TMOut statement
		 expired before the wait condition was completed in the WAIT statement.	Investigate the cause of timeout.
		  Check whether the set timeout period is proper.

2281	Timeout period set by TMOut statement
		 in WaitSig statement or SyncLock statement expired.	Investigate the cause of timeout.
		  Check whether the set timeout period is proper.

2282	Timeout period set by TMOut statement
		 in WaitNet statement expired.	Investigate the cause of timeout.
		  Check whether the set timeout period is proper.

2283	Timeout. Timeout at display device
		 setting.	Reboot the controller.

2285	Cannot clear an arm calibration while
		 in use.	Cannot clear the arm length calibration
		 while in use. Make sure that arm length calibration is not in
		 use.	The arm length calibration number
		 you tried to clear

2286	Cannot clear arm calibration number
		 '0'.	Cannot clear the arm length calibration
		 number "0" Review the program.

2287	Arm calibration number is out of range.	The specified arm calibration number
		 is out of range. Review the program.	The specified arm length calibration
		 number

2288	Arm calibration number is not defined.	Check the configuration of arm length
		 calibration. Review the program.	The specified arm length calibration
		 number

2290	Cannot execute a motion command.	Cannot execute the motion command
		 after using the user function in the motion command.  Review
		 the program.

2291	Cannot execute the OnErr command	Cannot execute OnErr in the motion
		 command when using user function in the motion command.  Review
		 the program.

2292	Cannot execute an I/O command while
		 the safeguard is open. Need Forced.	I/O command cannot be executed while
		 the safeguard is open.  Review the program

2293	Cannot execute an I/O command during
		 emergency stop condition. Need Forced.	I/O command cannot be executed during
		 emergency stop condition. Review the program.

2294	Cannot execute an I/O command when
		 an error has been detected. Need Forced.	I/O command cannot be executed while
		 an error occurs.  Review the program.

2295	Cannot execute this command from a
		 NoEmgAbort Task and Background Task.	For details on inexecutable commands,
		 refer to the online help.

Review the program.

2296	One or more source files are updated.
		 Please build the project.	Rebuild the project.

2297	Cannot execute an I/O command in TEACH
		 mode without the Forced parameter.	I/O command cannot be executed in
		 TEACH mode.  Review the program.

2298	Cannot continue execution in Trap
		 SGClose process.	You cannot execute Cont and Recover
		 statements with processing task of Trap SGClose.

2299	Cannot execute this command. Need
		 the setting [enable the advance taskcontrol commands] from RC+
		 controller preference settings.	Enable the [enable the advance task
		 control commands] from RC+ to execute the command.

2300	Robot in use. Cannot execute the motion
		 command when other task is using the robot.	The motion command for the robot cannot
		 be simultaneously executed from more than one task.  Review
		 the program.

2301	Cannot execute the motion command
		 until re-gripping the Enable Switch.	Execute the motion command with the
		 enable switch re-gripped.

2302	Cannot execute a Call statement in
		 a Trap Call process.	Another function cannot be called
		 from the function called by Trap Call.  Review the program.

2303	Cannot execute a Call statement in
		 a parallel process.	Review the program.

2304	Cannot execute an Xqt statement in
		 a parallel process.	Review the program.

2305	Cannot execute a Call statement from
		 the command window.	Execute Call from the program.

2306	Cannot execute an Xqt statement from
		 the task started by Trap Xqt.	Review the program.

2307	Cannot execute this command while
		 tasks are executing.	Check whether all tasks are completed.

2308	Cannot turn on the motor because of
		 a critical error.	Find the previously occurring error
		 in the error history and resolve its cause.  Then, reboot
		 the controller.

2309	Cannot execute a motion command while
		 the safeguard is open.	Check the safeguard status.

2310	Cannot execute a motion command while
		 waiting for continue.	Execute the Continue or Stop and then
		 execute the motion command.

2311	Cannot execute a motion command during
		 the continue process.	Wait until the Continue is complete
		 and then execute the motion command.

2312	Cannot execute a task during emergency
		 stop condition.	Check the emergency stop status.

2313	Cannot continue execution immediately
		 after opening the safeguard.	Need more than 1.5 seconds between
		 open the safeguard, close them and run the motor on.

When the above time has passed since the
		 safeguard was opened, the execution can be continued immediately
		 (with closed the safeguard).

2314	Cannot continue execution while the
		 safeguard is open.	Check the safeguard status.

2315	Cannot execute Cont and Restart command
		 in resume operation.	Wait until the Continue is completed.

2316	Cannot continue execution after an
		 error has been detected.	Check the error status.

2317	Cannot execute the task when an error
		 has been detected.	Reset the error by Reset and then
		 execute the task.

2318	Cannot execute a motion command when
		 an error has been detected.	Execute the motion command after resetting
		 the error by Reset.

2319	Cannot execute an I/O command during
		 emergency stop condition.	Check the emergency stop status.

2320	Function failure. Argument type does
		 not match.	Rebuild the project.

2321	Function failure. Return value does
		 not match to the function.	Rebuild the project.

2322	Function failure. ByRef type does
		 not match.	Rebuild the project.

2323	Function failure. Failed to process
		 the ByRef parameter.	Rebuild the project.

2324	Function failure. Dimension of the
		 ByRef parameter does not match.	Rebuild the project.

2325	Function failure. Cannot use ByRef
		 in an Xqt statement.	Rebuild the project.

2326	Cannot execute a Dll Call statement
		 from the command window.	Execute DII Call from the program.

2327	Failed to execute a Dll Call.	Check the DLL.

Review the program.

2328	Cannot execute the task before connection
		 with RC+.	You need to connect with RC+ before
		 executing the task.

2329	Cannot execute an Eval statement in
		 a Trap Call process.	Check the program.

2330	Trap failure. Cannot use the argument
		 in Trap Call or Xqt statement.	Check the program.

2331	Trap failure. Failed to process Trap
		 Goto statement.	Rebuild the project.

2332	Trap failure. Failed to process Trap
		 Goto statement.	Rebuild the project.

2333	Trap failure. Trap is already in process.	Rebuild the project.

2334	Cannot execute an Eval statement in
		 a Trap Finsh or a Trap Abort process.	Check the program.

2335	Cannot continue execution and Reset
		 Error in TEACH mode.	Check the program.

2336	Cannot use Here statement with a parallel
		 process.	Go Here :Z(0) ! D10; MemOn(1) !

is not executable.

Change the program to:

P999 = Here

Go P999 Here :Z(0) ! D10; MemOn(1) !

2337	Cannot execute except from an event
		 handler functions of GUI Builder.	Review the program.

2338	Cannot execute Xqt, data input, and
		 output for TP in a TEST mode.	Cannot execute in TEST mode.

Review the program.

2339	Cannot execute in stand-alone mode.	Change the setting to "cooperative
		 mode" and execute.

2340	Specified value allocated in InBCD
		 function is an invalid BCD value.	Review the program.

2341	Specified value in the OpBCD statement
		 is an invalid BCD value.	Review the program.

2342	Cannot change the status for output
		 bit configured as remote output.	Check the remote I/O setting.

2343	Output time for asynchronous output
		 commanded by On or Off statement is out of the available range.	Review the program.

2344	I/O input/output bit number is out
		 of available range or the board is not installed.	Review the program.

Check whether the expansion I/O board
		 and Fieldbus I/O board are correctly detected.

2345	I/O input/output byte number is out
		 of available range or the board is not installed.	Review the program.

Check whether the expansion I/O board
		 and Fieldbus I/O board are correctly detected.

2346	I/O input/output word number is out
		 of available range or the board is not installed.	Review the program.

Check whether the expansion I/O board
		 and Fieldbus I/O board are correctly detected.

2347	Memory I/O bit number is out of available
		 range.	Review the program.

2348	Memory I/O byte number is out of available
		 range.	Review the program.

2349	Memory I/O word number is out of available
		 range.	Review the program.

2350	Command allowed only when virtual
		 I/O mode is active.	The command can be executed only for
		 virtual I/O mode.

2353	Specified command cannot be executed
		 from the Command window.	Execute specified command from the
		 program.

Part Feeding:

The command cannot run on the Command
		 window.

2354	Cannot execute the I/O output command
		 when the Enable Switch is OFF.	Execute the I/O output command with
		 the enable switch gripped.

2360	File failure. Failed to open the configuration
		 file.	Restore the controller configuration.

2361	File failure. Failed to close the
		 configuration file.	Restore the controller configuration.

2362	File failure. Failed to open the key
		 of the configuration file.	Restore the controller configuration.

2363	File failure. Failed to obtain a string
		 from the configuration file.	Restore the controller configuration.

2364	File failure. Failed to write in the
		 configuration file.	Restore the controller configuration.

2365	File failure. Failed to update the
		 configuration file.	Restore the controller configuration.

2370	The string combination exceeds the
		 maximum string length.	The maximum string length is 255.
		  Review the program.

2371	String length is out of range.	The maximum string length is 255.
		  Review the program.

2372	Invalid character is specified after
		 the ampersand in the Val function.	Review the program.

2373	Illegal string specified for the Val
		 function.	Review the program.

2374	String Failure. Invalid character
		 code in the string.	Review the program.

2375	Label name length is out of range	The label name length is 32 words.
		  Review the label name.	1:VRT

2:Hand

2376	Description length is out of range.	Description length is 255 words.  Review
		 the Description.	1:VRT

2:Hand

2380	Cannot use '0' for Step value in For...Next.	Check the Step value.

2381	Relation between For...Next and GoSub
		 is invalid. Going in or out of a For...Next using a Goto statement.	Review the program.

2382	Cannot execute Return while executing
		 OnErr.	Review the program.

2383	Return was used without GoSub. Review
		 the program.	Review the program.

2384	Case or Send was used without Select.
		 Review the program.	Review the program.

2385	Cannot execute EResume while executing
		 GoSub.	Review the program.

2386	EResume was used without OnErr. Review
		 the program.	Review the program.

2391	During emergency stop condition, the
		 command cannot be executed.	Clear the emergency stop condition
		 and execute the command.

2400	Curve failure. Failed to open the
		 Curve file.	Reboot the controller.

Create a Curve file again.

2401	Curve failure. Failed to allocate
		 the header data of the curve file.	Reboot the controller.

Create a Curve file again.

2402	Curve failure. Failed to write the
		 curve file.	Reboot the controller.

Create a Curve file again.

2403	Curve failure. Failed to open the
		 curve file.	Reboot the controller.

Create a Curve file again.

2404	Curve failure. Failed to update the
		 curve file.	Reboot the controller.

Create a Curve file again.

2405	Curve failure. Failed to read the
		 curve file.	Reboot the controller.

Create a Curve file again.

2406	Curve failure. Curve file is corrupt.	Reboot the controller.

Create a Curve file again.

2407	Curve failure. Specified a file other
		 than a curve file.	Reboot the controller.

Create a Curve file again.

2408	Curve failure. Version of the curve
		 file is invalid.	Reboot the controller.

Create a Curve file again.

2409	Curve failure. Robot number in the
		 curve file is invalid.	Reboot the controller.

Create a Curve file again.

2410	Curve failure. Cannot allocate enough
		 memory for the CVMove statement.	Reboot the controller.

2411	Specified point data in the Curve
		 statement is beyond the maximum count.	The maximum number of points specified
		 in the Curve statement is 1000.  Review the program.

2412	Specified number of output commands
		 in the Curve statement is beyond the maximum count.	The maximum number of output commands
		 specified in the Curve statement is 16.  Review the program.

2413	Curve failure. Specified internal
		 code is beyond the allowable size in Curve statement.	Reboot the controller.

2414	Specified continue point data P() is beyond the
		 maximum count.	The maximum number of points specified
		 continuously is 1000.  Review the program.	Start point	End point

2415	Curve failure. Cannot create the curve
		 file.	Reboot the controller.

		Create a Curve file again.

2416	Curve file does not exist.	Check whether the specified Curve
		 file name is correct.

2417	Curve failure. Output command is specified
		 before the point data.	Check whether no output command is
		 specified before the point data.

2430	Error message failure. Error message
		 file does not exist.	Reboot the controller.

2431	Error message failure. Failed to open
		 the error message file.	Reboot the controller.

2432	Error message failure. Failed to obtain
		 the header data of the error message file.	Reboot the controller.

2433	Error message failure. Error message
		 file is corrupted.	Reboot the controller.

2434	Error message failure. Specified a
		 file other than the error message file.	Reboot the controller.

2435	Error message failure. Version of
		 the error message file is invalid.	Reboot the controller.

2440	File Error. File number is already
		 used.	Check the file number.

2441	File Error. Failed to open the file.	Make sure the file exists and you
		 specified the file correctly.

2442	File Error. The file is not open.	Open the file in advance.

2443	File Error. The file number is being
		 used by another task.	Check the program.

2444	File Error. Failed to close the file.	Check the file.

2445	File Error. File seek failed.	Review the program.

Check the pointer setting.

2446	File Error. All file numbers are being
		 used.	Close unnecessary files.

2447	File Error. No read permission.	Use ROpen or UOpen that has read access
		 to the file.

2448	File Error. No write permission.	Use WOpen or UOpen that has write
		 access to the file.

2449	File Error. No binary permision.	Use BOpen that has binary access to
		 the file.

2450	File Error. Failed to access the file.	Check the file.

2451	File Error. Failed to write the file.	Check the file.

2452	File Error. Failed to read the file.	Check the file.

2453	File Error. Cannot execute the command
		 for current disk.	The specified command is not available
		 in the current disk (ChDisk).

2454	File Error. Invalid disk.	Review the program.

2455	File Error. Invalid drive.	Review the program.

2456	File Error. Invalid folder.	Review the program.

2460	Database Error. The database number
		 is already being used.	Review the program.

Specify the number of other database.

Close the database.

2461	Database Error. The database is not
		 open.	Review the program.

Open the database.

2462	Database Error. The database number
		 is being used by another task.	Review the program.

2470	Windows Communication Error. Invalid
		 status.	Reboot the Controller.

Rebuild the project.

2471	Windows Communication Error. Invalid
		 answer.	Reboot the Controller.

Rebuild the project.

2472	Windows Communication Error. Already
		 initialized.	Reboot the Controller.

2473	Windows Communication Error. Busy.	Reboot the Controller.

Rebuild the project.

2474	Windows Communication Error. No request.	Reboot the Controller.

Rebuild the project.

2475	Windows Communication Error. Data
		 buffer overflow.	Reduce the data volume.

Review the program.

2476	Windows Communication Error. Failed
		 to wait for event.	Reboot the Controller.

2477	Windows Communication Error. Invalid
		 folder.	Make sure the specified folder is
		 correct.

2478	Windows Communication Error. Invalid
		 error code.	Rebuild the project.

2500	Specified event condition for Wait
		 is beyond the maximum count.	The maximum number of event conditions
		 is 8.  Review the program.

2501	Specified bit number in the Ctr function
		 was not initialized with a CTReset statement.	Review the program.	The specified bit number

2502	Task number is beyond the maximum
		 count to execute.	The available number of tasks that
		 can be executed simultaneously is 32 for normal tasks, and 16
		 for background tasks.  Review the program.

2503	Cannot execute Xqt when the specified
		 task number is already executing.	Review the program.	The specified task number

2504	Task failure. Specified manipulator
		 is already executing a parallel process.	Rebuild the project.

2505	Not enough data for Input statement
		 variable assignment.	Check the content of communication
		 data.  Review the program.

2506	Specified variable for the Input statement
		 is beyond the maximum count.	For OP, only one variable can be specified.
		  For other devices, up to 32 variables can be specified.

2507	All counters are in use and cannot
		 initialize a new counter with CTReset.	The available number of the counters
		 that can be set simultaneously is 16.  Review the program.

2508	OnErr failure. Failed to process the
		 OnErr statement.	Rebuild the project.

2509	OnErr failure. Failed to process the
		 OnErr statement.	Rebuild the project.

2510	Specified I/O label is not defined.	The specified I/O label is not registered.
		  Check the I/O label file.

2511	SyncUnlock statement is used without
		 executing a previous SyncLock statement. Review the program.	Review the program.	Signal number

2512	SyncLock statement was already executed.	The SyncLock statement cannot be executed
		 for the second time in a row.  Review the program.	Signal number

2513	Specified point label is not defined.	The specified point label is not registered.
		  Check the point file.

2514	Failed to obtain the motor on time
		 of the robot.	Reboot the controller.

2515	Failed to configure the date or the
		 time.	Check whether a date and time is set
		 correctly.

2516	Failed to obtain the debug data or
		 to initialize.	Reboot the controller.

2517	Failed to convert into date or time.	Check the time set on the controller.

Reboot the controller.

2518	Larger number was specified for the
		 start point data than the end point data.	Specify a larger number for the end
		 point data than that for the start point data.	Start point	End point

2519	Invalid format syntax for FmtStr$.	Check the format.

2520	Point file name is too long.	Check whether the specified point
		 file name is correct.  The maximum string length of the file
		 name is 32.

2521	Point failure. Point file path is
		 too long.	Check whether the specified point
		 file name is correct.

2522	Point file name is invalid.	Make sure you don't use improper characters
		 for file name.

2523	The continue process was already executed.	Review the program.

2524	Cannot execute Xqt when the specified
		 trap number is already executing.	Review the program.

2525	Password is invalid.	Check whether a password is set correctly.

2526	No wait terms.	Rebuild the project.

2527	Too many variables used for global
		 variable wait.	Review the program.

2528	The global variable that was not able
		 to be used for the wait command was specified.	Review the program.

2529	Cannot use Byref if the variable is
		 used for global variable wait.	Review the program.

2530	Too many point files.	Check the point file.

2531	The point file is used by another
		 robot.	Review the program.

2532	Cannot calculate the point position
		 because there is undefined data.	Check the point data.

2533	Error on INP or OUTP.	Review the program.

2534	No main function to start for Restart
		 statement.	Without executing main function, Restart
		 is called.

2535	Does not allow Enable setting in Teach
		 mode to be changed.	Setup the authority.

2536	Failed to change Enable setting in
		 Teach mode.	Reboot the Controller.

2537	Count of point data P(:) is not correct
		 or format of parameter is not correct.	Review the program.

2538	Force_GetForces failure.  Failed
		 to process Force_GetForces statement.	Review the program.

2539	Password is invalid.	Check the password.

2540	Not connected to RC+.	Connect to the RC+.

2541	Duplicate parameter.	Same robot number was specified.

Check the parameter.

2542	The specified work queue number is
		 invalid.	Available work queue numbers are from
		 1 to 16.  Review the program.

2543	Invalid sequence was specified.	Specified sequence name cannot be
		 found.  Review the sequence name.

2544	Invalid object was specified.	Specified object name cannot be found.
		  Review the object name.

2545	Invalid calibration was specified.	Specified calibration name cannot
		 be found.  Review the calibration name.

2546	Cannot turn on the motor immediately
		 after opening the safeguard.	Need more than 1.5 seconds between
		 open the safeguard, close them and run the motor on.

2547	Cannot use specified option	Part Feeding:

Wrong command format or value settings.

Read the description for the corresponding
		 command provided in

Part Feeding 8.0  Introduction &
		 Hardware (Common) & Software

Software 3.  Part Feeding SPEL+ Command
		 Reference and correct the code.	1:VRT

2548	Too many force files.

Delete the force files or use the existing
		 force files.	Reboot the controller.

Initialize the controller firmware.

Replace the controller.

2549	The force file which is not associated
		 with the robot cannot be specified.

Specify the correct force file.	Reboot the controller.

Initialize the controller firmware.

Replace the controller.

2550	Specified command is not supported
		 for joint type robot and cartesian type robot.	Specified robot is not supported.

Check the robot configuration.

2551	Failed to Get the health information.	Reboot the controller.

2552	Does not allow setting in UL mode
		 to be changed.	Setup the authority.

2553	Failed to change setting in UL mode.	Reboot the Controller.

2554	Duplicate data label. Specified label
		 name is already used. Change the label name.	Review the label name.	1:VRT

2555	Specified label was not defined. Specify
		 a defined Label.	Specified label was not defined.	1:VRT

2:Hand

2556	An excessive loop was detected.

Please reduce the number of looped tasks
		 or set Wait	This error messages are only displayed
		 in T/VT series Manipulators.

Do not perform any processing such as
		 infinite loop or any other similar processing as much as possible.

For more details, refer to Restrictions
		 of Functions in Maintenance, T/VT series manual.

2557	An error occurred in Trap.

Note 1: Detailed error information

Following the detailed error information,
		 take a relevant countermeasure.	An error occured in Trap.

Check the corresponding error code in
		 the system history and take countermeasures.	Detailed error information

2558	Argument parameter is too long.	Confirm a parameter of the argument.

2559	Cannot execute when the motor is in
		 the off state.	Change to the state to motor on and
		 execute.

2560	The current robot number and the robot
		 number of the force guide sequence property do not match. Please
		 check the robot number.	Confirm the current robot number and
		 the robot number of the force guide sequence.	Robot number

2561	The current robot type and the robot
		 type of the force guide sequence property do not match. Reconfigure
		 the RobotNumber property.	Confirm the current robot number and
		 the robot number of the force guide sequence property.

Reconfigure the RobotNumber property.

2562	The current tool number and the robot
		 tool of the force guide sequence property do not match. Please
		 check the tool number.	Confirm the current tool number and
		 the robot tool of the force guide sequence property.	Tool number

2563	The point file being loaded does not
		 match the point file of the force guide sequence property.

Please check the point file.	Confirm the loaded point file and
		 the the point file of the force guide sequence.

2564	An instruction that can not be executed
		 during torque control was executed.	Turn OFF the torque control and execute.

2565	Prohibited command while tracking
		 was executed.	Delete Prohibited commands from the
		 program.

2566	Cannot execute the FGRun command for
		 same robot.	Cannot execute the FGRun command for
		 same robot.  End the FGRun command or execute it in other
		 robot

2567	Cannot execute the FGGet command for
		 the running force guide sequence.	Cannot execute the FGGet command for
		 the running force guide sequence.

Execute it after the force guide sequence
		 ends.

2568	An instruction that can not be executed
		 by parallel processing was executed.

Review the program.	Review the program.

2569	Cannot get the force guide sequence
		 property.	Reboot the Controller.

2570	Sequence number is out of range. Please
		 check the specified sequence number.	Sequence number is from 1 to 64.  Confirm
		 the specified sequence number.	Sequence number

2571	Object number is out of range. Please
		 check the specified object number.	Object number is from 1 to 16.  Confirm
		 the specified object number.	Object number

2572	Cannot clear the result of the force
		 guide.	Reboot the Controller.

2573	Cannot set the result of the force
		 guide.	Reboot the Controller.

2574	Cannot get the result of the force
		 guide.	Reboot the Controller.

2575	Storing the force guide sequence result
		 in a variable failed.	Reboot the Controller.

2576	Force Sequence name that does not
		 exist was specified.	Confirm the specified force sequence
		 name.

2577	Force Object name that does not exist
		 was specified.	Confirm the specified force object
		 name.

2578	Cannot execute the FGGet command for
		 the unexecuted force guide sequence.	Confirm the specified force guide
		 sequence.

2579	Command execution failed.	Upgrade Epson RC+ and controller firmware
		 to the latest.

2580	Feeder name specified does not exist	Wrong feeder name specified.

Check the feeder name in Epson RC+ 8.0
		 - Menu - [Setup] - [System Configuration]

2581	Failed to reset feeder. Check connection.	Cannot connect to the feeder.

Check that feeder network settings (IP
		 Address, IP Mask, Port) are correct.

Check that the Ethernet connection between
		 the feeder and the Controller is functioning normally (have cables
		 become disconnected, is there a hub failure or a lack of power
		 supply to the hub, etc.).  Check the power supply to the
		 feeder.

2582	Feeder not connected. Check connection.	(As above)

2583	Feeder backlight not enabled	Wrong feeder specified.

Check that the backlight has been enabled
		 in Epson RC+ 8.0 - Menu - [Setup] - [System Configuration].

2584	Feeder output terminal not enabled	Wrong feeder specified.

Check that the hopper has been enabled
		 in Epson RC+ 8.0 - Menu - [Setup] - [System Configuration].

2585	Incorrect feeder type	It occurs when restoring a controller
		 backup, if the feeder configuration has been changed.

Once remove and register feeder settings
		 in "Epson RC+ 8.0 - Menu - Setup - System Settings".

2586	Cannot set of Part Feeding.	Cannot communicate with feeder.

Check that the Ethernet connection between
		 the feeder and the

Controller is functioning normally (have
		 cables become disconnected, is there a hub failure or a lack of
		 power supply to the hub, etc.).

Check the power supply to the feeder.

Check that feeder network settings (IP
		 Address, IP Mask, Port) are correct.

2587	Cannot execute with the virtual controller	PartFeeding option requires a real
		 controller to run.

2588	Failed to acquire partfeeding information	This command cannot be executed from
		 a command window or virtual controller. Check the description
		 of the relevant command in the "Part Feeding SPEL+ Command
		 Reference".

2589	Action command call that the feeder
		 cannot execute.	For PartFeeding IF-80, PF_Output command
		 cannot be used. Review the program.

For IF-240/380/530, check if the purge
		 gate is properly mounted.

2590	Could not change the vibration set.	Cannot communicate with feeder.

Check that the Ethernet connection between
		 the feeder and the

Controller is functioning normally (have
		 cables become disconnected, is there a hub failure or a lack of
		 power supply to the hub, etc.).

Check the power supply to the feeder.

Check that feeder network settings (IP
		 Address, IP Mask, Port) are correct.

2591	PF_ReleaseFeeder statement is used
		 without executing a previous PF_AccessFeeder statement. Review
		 the program.	Review the program.

2592	PF_AccessFeeder statement was already
		 executed.	The PF_AccessFeeder statement cannot
		 be executed for the second time in a row. Review the program.

2593	Purge Gate is not valid.	Check if the purge gate is properly
		 mounted.

2594	Failed to Set the health information	The specified robot is not supported.

2595	Invalid vision sequence index. Check
		 the index.	Please review the value specified
		 in Index.

2596	Invalid vision object index. Check
		 the Index.	Please review the value specified
		 in Index.

2597	Invalid data type.	The format of the specified data is
		 different for the parameter you want to set. (e.g. A Double value
		 is specified even though it must be specified as an Integer.)
		 Please review the value.

2598	The main circuit is being charged.
		 Reset the error after charging.

When using TP, do not turn off the Enable
		 switch until charging is complete.	The capacitor for the main circuit
		 needs to be charged, since the motor has not been turned on for
		 a long time.

Charging will complete in about 120 seconds.
		 After checking the 2599 message, reset the error.

When using TP

When you turn the motor on from TP, it
		 is not charged if you release the Enable switch.

Check the 2599 message to reset the error,
		 and then turn on the motor.

Charging will start again.

2599	The time to charge has passed. Reset
		 the error.

2600	Mass Property Object number is out
		 of the allowable range.

Check the range of numbers.	The MassProperties numbers that can
		 be specified are from 1 to 15.

Please review the program.

2601	Mass Property Object is not defined.

Check the setting.	Please confirm the setting of MassProperties.

Please review the program.

2602	Cannot clear Mass Property Object
		 while in use.

Specify another Mass Property Object before
		 clearing the previous object.	MP cannot be cleared while in use.

Please confirm whether MP is in use.

2603	Cannot clear Mass Property Object
		 number '0'	MP-number 0 cannot be cleared.

Please review the program.

2610	The hand number is incorrect.	You can specify a hand number from
		 1 to 15. Review the program.

2611	Hand is not defined.	Set a Hand.

You can set in Epson RC+ 8.0 - Menu -
		 [Tools] - [Robot Manager] - [Hands] tab.

2612	The hand setting is incorrect.	Review the hand setting.

You can set in Epson RC+ 8.0 - Menu -
		 [Tools] - [Robot Manager] - [Hands] tab.	Hand number

2613	This robot model cannot use Hand.	The hand function cannot be used with
		 this robot.

2614	This hand is already used in the other
		 task.	Motion commands cannot be executed
		 on a hand from multiple tasks at the same time. Review the program.

2615	The I/O bit number which does not
		 exist is specified for Hand.	Make sure that the specified bit number
		 is correct.

When you use extended board, make sure
		 it is recognized correctly.	Hand number

2616	The specified I/O bit number is already
		 assigned to the other function or remote I/O.	Review the I/O bit number specified
		 for a Hand.	Hand number

2617	This hand cannot be used for an event
		 conditional expression.	The event conditional expression only
		 supports hands with one input point.

Specify a hand with one input point.

2618	Could not get the specified hand information.	Restart the controller.

2700	Safety function is not available for
		 this Controller.	Use the Controller that supports Safety
		 function.

2702	Communication error occurred between
		 the safety function manager and the Safety Board	Do one of the following:

- Check the connection between the RC+
		 and the Controller and reset the Controller.

- Check the connection of the Safety Board
		 in the Controller.

- Replace the Safety Board.	Type of error

2: Controller detect

16: Response error

32: Main-Sub difference

64: Timeout

2708	Safety function is not available for
		 this robot model.	Select the Robot that supports Safety
		 function.	Robot Type number

2840	Failed in the confirmation of the
		 DU connection count.	Check whether the Drive Unit is connected
		 properly.

2841	Failed in the acquisition of the DU
		 connection count.	Check whether the Drive Unit is connected
		 properly.

2842	Failed in the confirmation of the
		 DU connection information.	Check whether the Drive Unit is connected
		 properly.

2843	Failed in the acquisition of the DU
		 connection information.	Check whether the Drive Unit is connected
		 properly.

2844	There is a missing number or repetition
		 in the dip switch setting of DU.	Check the dip switches of the Drive
		 Unit

2845	The drive unit (DU) used by the robot
		 is not connected.	Check whether the Drive Unit is connected
		 properly.

2846	Because the increase and decrease
		 of the drive unit was recognized, the controller unit is rebooted.	The controller was rebooted due to
		 change of connection with the Drive Unit.

2847	The dip switch setting of the force
		 sensor I/F unit is improper.	It is necessary to change the dip
		 switch setting.

Please inquire with us.

2848	The force sensor I/F unit to which
		 the force sensor is registered is not connected.

Check connection.	Please confirm whether it is possible
		 to connect it with force sensor I/F unit correctly.

2849	Failed to initialize the force sensor
		 I/F unit.

Check connection.	Please confirm whether it is possible
		 to connect it with force sensor I/F unit correctly.

2850	Failed to initialize the force sensor
		 I/F unit.

Check connection.	Please confirm whether it is possible
		 to connect it with force sensor I/F unit correctly.

2851	The force sensor which is different
		 from the registered sensor is connected.

Check connection or review the setting.	The serial number of the sensor connected
		 with the registered sensor is not corresponding.

Please exchange it for a new sensor after
		 confirming the connection, returning to the connected sensor,
		 or invalidating the sensor.  In case of intended replacement,
		 configure the connection settings again in the sensor setting.

2852	The registered force sensor is not
		 connected.

Check connection.	Please confirm whether it is possible
		 to connect it with the registered sensor correctly.

Please invalidate the sensor when you
		 do not connect the sensor.

2853	Failed to update the force sensor
		 I/F unit software.

Review the update procedure.	Please review the soft update setting.

Please confirm the connection with force
		 sensor I/F unit.

2854	Failed to update the force sensor
		 I/F unit software.

Review the update procedure.	Please confirm the file name.

Please confirm the update file.

2855	Failed to update the force sensor
		 I/F unit software.

Review the update procedure.	Please confirm the power supply and
		 the connection of force sensor I/F unit.

Reboot the controller.

2856	The force sensor I/F unit with an
		 old version is connected.

Update the force sensor I/F unit software.	The version of the connected force
		 sensor I/F unit needs to be updated.  Update the force sensor
		 I/F unit.  For update procedures, please inquiry with us.

2857	The robot registered to the force
		 sensor I/F unit is not connected.

Review the robot registration or the force
		 sensor configuration.	The robot that relates to the sensor
		 is not registered.

Please review the registration of the
		 robot or invalidate the robot connection.

2858	Failed to allocate memory for the
		 force monitor.	Reboot the controller.

Please inquire with us if a similar error
		 occurs after rebooting it.

2859	Failed to allocate memory for the
		 force log.	Reboot the controller.

Please inquire with us if a similar error
		 occurs after rebooting it.

2860	The force monitor object specified
		 in the force log is in use.

Specify another force monitor object.	The same FM number cannot be specified.

Please specify a different FM number.

2861	The maximum number of the force logs
		 is executed.

Review the log timing.	The greatest log number is used.

Please confirm the number of logs.

2862	Failed to allocate memory of force
		 function.	Reboot the controller.

Please inquire with us if a similar error
		 occurs after rebooting it.

2863	Execution of force guide sequence,
		 RecordStart, FCMStart and LogStart can not be executed at the
		 same time.

Please review the program.	Execute after the LogStart property
		 ends by LogEnd property.

2864	Execution of force guide sequence,
		 RecordStart, FCMStart and force monitor can not be executed at
		 the same time.

Please quit either.	Execute after quitting the Force Monitor.

2865	Execution of force guide sequence,
		 RecordStart, FCMStart and LogStart can not be executed at the
		 same time.

Please review the program.	Execute the LogStart property after
		 the RecordStart property ends by force guide sequence, force control
		 monitor, or the RecordEnd property.

2866	Execution of force guide sequence,
		 RecordStart, FCMStart and force monitor can not be executed at
		 the same time.

Please quit either.	Execute the force monitor after quitting
		 the RecordStart property by force guide sequence, force control
		 monitor, or the RecordEnd property.

2867	The specified channel in use.

Specify a another channel.	The same channel cannot be specified.
		  Specify a different channel to execute.

2868	The force monitor object being used
		 is specified. Please specify another force monitor object.	The same FM number cannot be specified.
		  Specify a different FM number to execute.

2869	The specified duration of measurement
		 is smaller than the specified measurement interval.

Check the parameter.	Specify the measurement time larger
		 than the measurement interval to execute.

2870	The product of the specified duration
		 of measurement and the specified measurement interval is out of
		 allowable range.

Check the parameter.	Check the measurement time and interval.

2871	Execution of force guide sequence,
		 RecordStart, FCMStart, force monitor can not be used more than
		 three at the same time.	To execute newly, make sure to quit
		 either of the two running items and execute.

2872	Force monitor can not be launched
		 twice.	To start force monitor newly, quit
		 the running force monitor and start a new one.

2873	Unsupported Drive unit is connected.

Check connection.	Disconnect the drive unit and restart
		 the controller.

2880	Failed to initialize the Force Sensor
		 I/F board.

Check connection.	Check connection of the controller
		 and Force Sensor I/F board.

Reboot the controller.

Please inquire with us if a similar error
		 occurs even after rebooting the controller.

2881	Failed to initialize the Force Sensor
		 I/F board.

Check connection.	Check connection of the controller
		 and Force Sensor I/F board.

Reboot the controller.

Please inquire with us if a similar error
		 occurs even after rebooting the controller.

2882	Detected one Force Sensor I/F board
		 and two RS-232C boards. If using the Force Sensor I/F board, RS-232C
		 board is available up to one board.	Remove either Force Sensor I/F board
		 or the second board of RS-232C board.

2883	Detected two boards: Force Sensor
		 I/F board and RS-232C board with the second board setting.

If using the Force Sensor I/F board, return
		 the setting to the first board of RS-232C board.	Return the setting to the first board
		 of RS-232C board.

2884	Failed to initialize the Force Sensor
		 I/F board.

Check connection.	Check connection of the controller
		 and Force Sensor I/F board.

Reboot the controller.

Please inquire with us if a similar error
		 occurs even after rebooting the controller.

2885	Sensor 3 and 4 of Force Sensors are
		 enabling.

If using Force Sensor I/F board, disable
		 the sensor 3 and 4 of Force Sensors.	Disable the sensor 3 and 4 of the
		 Force Sensor.

2886	Failed to communicate with Force Sensor
		 I/F board and Force Sensor.

Check connection of the Force Sensor.	Check connection of the Force Sensor
		 I/F board and Force Sensor. Reboot the controller.

Please inquire with us if a similar error
		 occurs even after rebooting the controller.

2887	Detected Force Sensor I/F board and
		 Force Sensor I/F unit.

Remove either Force Sensor I/F board or
		 Force Sensor I/F unit.	Unable to use the Force Sensor I/F
		 board and Force Sensor I/F unit at the same time.

Remove either Force Sensor I/F board or
		 Force Sensor I/F unit.

2888	Unsupported Force Sensor is set.

Check the configuration.	Check the configuration.

Firmware version may be old.  Check
		 whether the firmware version is supported and update it as necessary.

2889	An undefined or unsupported hand is
		 specified for RobotHand in the force guide sequence.

Check hand settings.	Make sure that the specified hand
		 is set.

For ScrewTighten sequences, make sure
		 that "Electric screwdriver" is set on the specified
		 hand type.

2900	Failed to open as server for the Ethernet
		 port.	Check whether the Ethernet port is
		 set properly.  Check whether the Ethernet cable is connected
		 properly.

2901	Failed to open TCP/IP port (client)	Parts Feeding:

Cannot connect to the feeder.

Check that feeder network settings (IP
		 Address, IP Mask, Port) are correct.

Check that the Ethernet connection between
		 the feeder and the Controller is functioning normally (have cables
		 become disconnected, is there a hub failure or a lack of power
		 supply to the hub, etc.).  Check the power supply to the
		 feeder.

2902	Failed to read from the Ethernet port.	Check whether the port of communication
		 recipient is not close.

2904	Invalid IP Address was specified.	Review the IP address.

2905	Ethernet failure. No specification
		 of Server/Client.	Review the program.

2906	Ethernet port was not configured.	Check whether the Ethernet port is
		 set properly.

2907	Ethernet port was already in use by
		 another task.	A single port cannot be used by more
		 than one task.

2908	Cannot change the port parameters
		 while the Ethernet port is open.	The port parameters cannot be changed
		 while the port is open.

2909	Ethernet port is not open.	To use the Ethernet port, execute
		 the OpenNet statement.

2910	Timeout reading from an Ethernet port.	Check the communication.

2911	Failed to read from an Ethernet port.	Check the communication.

2912	Ethernet port was already open by
		 another task.	A single port cannot be used by more
		 than one task.

2913	Failed to write to the Ethernet port.	Check whether the Ethernet port is
		 set properly.  Check whether the Ethernet cable is connected
		 properly.

2914	Ethernet port connection was not completed.	Check whether the port of communication
		 recipient is open.

2915	Data received from the Ethernet port
		 is beyond the limit of one line.	The maximum length of a line is 255
		 bytes.

2916	Failed to process a dummy file of
		 virtual Ethernet port	Check the content of the dummy file.	Port number

2920	RS-232C failure. RS-232C port process
		 error.	Check whether the RS-232C board is
		 correctly detected.

2921	Failed to read from the RS-232C port.	Check the parameter and communication.

2922	Failed to read from the RS-232C port.
		 Overrun error.	Slow down data transfer or reduce
		 data size.

2926	The RS-232C port hardware is not installed.	Check whether the RS-232C board is
		 correctly detected.

2927	RS-232C port is already open by another
		 task.	A single port cannot be used by more
		 than one task.

2928	Cannot change the port parameters
		 while the RS-232C port is open.	The port parameters cannot be changed
		 while the port is open.

2929	RS-232C port is not open.	To use the RS-232C port, execute the
		 OpenCom statement.

2930	Timeout reading from the RS-232C port.	Check the communication.

2931	Failed to read from the RS-232C port.	Check the communication.

2932	RS-232C port is already open by another
		 task.	A single port cannot be used by more
		 than one task.

2933	Failed to write to the RS-232C port.	Check the communication.

2934	RS-232C port connection not completed.	Check the RS-232C port.

2935	Data received from the RS-232C port
		 is beyond the limit of one line.	The maximum length of a line is 255
		 bytes.

2936	Failed to process a dummy file of
		 virtual RS-232C port	Check the content of the dummy file.	Port number

2937	Cannot execute while Remote RS-232C
		 are using.	Specified port is currently used.

Specify another port.

2938	Cannot execute while ModBus are using.	Specified port is currently used.

Specify another port.

2950	Daemon failure. Failed to create the
		 daemon thread.	Reboot the Controller.

2951	Daemon failure. Timeout while creating
		 the daemon thread.	Reboot the Controller.

2952	TEACH/AUTO switching key input signal
		 failure was detected.	Set the TP key switch to TEACH or
		 AUTO properly.  Check whether the TP is connected properly.

2953	ENABLE key input signal failure was
		 detected.	Check whether the TP is connected
		 properly.

2954	Relay weld was detected.	Overcurrent probably occurred due
		 to short-circuit failure.  Investigate the cause of the problem
		 and take necessary measures and then replace the DPB.

2955	Temperature of regeneration resistor
		 was higher than the specified temperature.	Check whether the filter is not clogged
		 up and the fan does not stop.

If there is no problem on the filter and
		 fan, replace the regenerative module.

2970	MNG failure. Area allocate error.	Reboot the Controller.

2971	MNG failure. Real time check error.	Reboot the Controller.

2972	MNG failure. Standard priority error.	Reboot the Controller.

2973	MNG failure. Boost priority error.	Reboot the Controller.

2974	MNG failure. Down priority error.	Reboot the Controller.

2975	MNG failure. Event wait error.	Reboot the Controller.

2976	MNG failure. Map close error.	Reboot the Controller.

2977	MNG failure. Area free error.	Reboot the Controller.

2978	MNG failure. AddIOMem error.	Reboot the Controller.

2979	MNG failure. AddInPort error.	Reboot the Controller.

2980	MNG failure. AddOutPort error.	Reboot the Controller.

2981	MNG failure. AddInMemPort error.	Reboot the Controller.

2982	MNG failure. AddOutMemPort error.	Reboot the Controller.

2983	MNG failure. IntervalOutBit error.	Reboot the Controller.

2984	MNG failure. CtrReset error.	Reboot the Controller.

2997	Collision Detection	If you use the simulator, check if
		 the object is placed in the direction of the robot motion.

2998	AbortMotion attempted when robot was
		 not moving	See Help for AbortMotion.

2999	AbortMotion attempted when robot was
		 moving	See Help for AbortMotion.


---

# Collision Detection Function
**Type:** function | **Section:** Operator

## Description
Collision Detection Function

Collision Detection Function (Detection Function of Robot Motion Error)

Detect the robot motion error from differentiation between desired speed and the actual speed (speed deviation value). Errors can be detected by this function is classified into A and B.

A: Collision or contact of robot arm or hand occurs

B: Robot motion errors other than collision or contact

Also, error B is classified into below according to the power condition.

Error in high power

B1: Torque saturation due to a low Weight or Inertia setting.

B2: Torque saturation due to combined motion of multiple joints and movement of a long object.

B3: Torque saturation due to supply voltage reduction.

B4: Error motion due to hardware error or software malfunction.

Error in low power

B4: Error motion due to hardware error or software malfunction.

B5: Torque saturation in low power due to a hand or a long object that exceeds the weight described in the specifications.

When an A or B error is detected, one of the messages below will be displayed and the robot will stop.Reduce the damage of the robot or equipment.

Error 5057: detect the collision in high power. (Detect the robot motion error.)

Error 5058: detect the collision in low power. (Detect the robot motion error.)

The following errors have previously existed; however, this function can detect the above errors quickly.

Error 5042, 5043: Position error.

Error is not detected by torque saturation in short time. Detect a state with high risk that causes a malfunction and stop the robot. The following phenomena may occur if you continue to use the robot in B1 or B2 status. Make a state that errors do not occur.

Loose binding parts such as screws.

Reduction gear is damaged.

Increase a risk of robot damage

Turn ON CollsionDetect command and detection is enabled. (Default: ON)

Default is different depending on the firmware version.

Ver.7.2.1.x  or later: default: ON

Before Ver.7.2.0.x : default: OFF

When upgrading before Ver.7.2.0.x or Ver7.2.1.x or later: default: OFF

Reboot a controller to return to the default.

The following describes the detail of error B when error 5057 or 5058 is detected without a collision or contact of the robot or arm.

In high power mode

Check the torque saturation by using PTRQ command. Torque saturation is occurred if the joint outputs "1" in PTRQ command.

In that case, make sure that the Weight setting is properly and in accord with the hand weight.

Also, make sure that Inertia setting is properly for joint #4 of SCARA robot and joint #6 of 6-axis robot.

Next, make sure that there is no torque saturation by using PTRQ command by combined motion that multiple joints (#2, #3 and #5 joints of 6-axis robot) operate in the same direction and throwing around the long object.

If torque saturation occurs, reduce acceleration/deceleration of Accel command until there is no torque saturation (the value: 1.0 or less is displayed in PTRQ).

Also, torque saturation may occur due to reduction of supply voltage that inputs to the controller. Check the power supply voltage is within the specifications.

You can turn ON/OFF the collision detection function per equipment if you want to use without performing those error detection due to equipment compatibility securement or similar reasons.

If other error occurs at the same time, take a countermeasure for that first.

In low power mode

Make sure that hand weight is within the specifications.

Also, check the torque saturation when errors occur on the joint #4 and 5 of 6-axis robot. When torque saturation is occurred, it is long object that cannot be hold by low power mode. Hold in high power mode.

If other error occurs at the same time, take a countermeasure for that first.

Immediately stop result of the torque saturation by combination of the following motion and command. Error of A and B can be detected faster.

HP motion: LimitTorqueStop Command

LP motion: LimitTorqueStopLP Command

The following describes details of collision of the robot arm A and contact detection.

For reduction of damage on the arms and the end effectors due to the collision with peripherals, there are two functions: Collision detection function, and torque restriction function described in the next section.

The collision detection function detects the collision and stops the robot immediately.

The torque restriction function restricts torque at the collision and also stops the robot immediately.

These are functions to reduce damage on the robot at the collision, but cannot avoid damage completely. Also, the functions cannot be used for the purpose of human safety.

As shown to the right, the force applied to the robot during a collision can be roughly divided into two types:

the impact of speed right before the collision, and the pressing force by motor torque after the collision.

The collision detection function and the torque restriction function reduce damage caused by the pressing force right after the collision. These functions do not have any effect on damage caused by the impact of speed.

The collision detection function detects collision by the speed deviation value for robot motion control (differentiation between the desired speed and the actual speed) showing an abnormal value which is greatly different from normal motion due to the collision.

Turn ON CollsionDetect command and the detection is enabled. (Default: ON)

Default is different depending on the firmware version.

Ver.7.2.1.x  or later: default: ON

Before Ver.7.2.0.x : default: OFF

Reboot a controller to return to the default.

When enabled, this function reduces the time of pressing force by the motor torque, by detecting the collision and stopping the robot immediately. This reduces the pressing force by about 20%. To reduce the damage more, use this function together with the torque restriction function.

The collision detection function is automatically disabled during the pressing motion and the force sensing operation described in "Pressing Motion".

Also, the function may have false detection in cases of powerful contact motion and significant acceleration and deceleration which may have consecutive torque saturation. To confirm if there is a risk of false detection, use PTRQ.

If PTRQ is less than 1 for all axes, there is no risk of false detection.

If PTRQ is one, torque saturation is occurring on the axis. This means excessive acceleration and deceleration are applied, and it is not preferable for motor control. It also has a risk of damage on the manipulator. In such a situation, take the following countermeasures.

For contacting operation,

Lower acceleration
	 and deceleration at a contact

Set a contacting
	 depth shallow

If you want to operate the manipulator without taking the above countermeasures, you can enable and disable the function for each axis. Set the function off for the axis which you want to disable the function.

For details of the command and function, refer to the following manual.

Epson RC+ 8.0 SPEL+ Language Reference

CollisionDetect Statement

CollisionDetect Function


---

# CollisionDetect Function
**Type:** function | **Section:** Operator

## Syntax
```
CollisionDetect( jointNumber )
```

## Parameters
jointNumber	Specify the joint by a joint number from 1 to 6.

## Description
CollisionDetect Function

CollisionDetect Function

## Examples
```spel
Print CollisionDetect(1)  'Displays CollisionDetect value of the Joint #1.
```

## See Also
Returns the setting value of CollisionDetect command.

CollisionDetect

CollisionDetect Function Example

Print CollisionDetect(1)  'Displays CollisionDetect value of the Joint #1.


---

# CollisionDetect Statement
**Type:** statement | **Section:** Operator

## Syntax
```
(1) CollisionDetect status

(2) CollisionDetect status, jointNumber

(3) CollisionDetect
```

## Parameters
status	On: Enables
		 the collision detection (detetction of robot motion error).

Off: Disables
		 the collision detection (detetction of robot motion error)..

jointNumber	SCARA robots
		 (including RS series): Specify the joint by a joint number from
		 1 to 4.

Vertical 6-axis
		 robots (including N series): Specify the joint by a joint number
		 from 1 to 6

Result

Returns the current CollisionDetect status when the parameters are omitted.

## Description
Detect the robot motion error from differentiation between desired speed and the actual speed (speed deviation value).  Errors can be detected by this function is classified into A and B.

A: Collision or contact of robot arm or hand occurs

B: Robot motion errors other than collision or contact

Also, error B is classified into below according to the power condition.

Error in high power

Torque saturation due to littile setting of Weight or Inertia.

Torque saturation due to combined motion of multiple joints and throwing around the long object.

Torque saturation due to supply voltage reduction.

Error motion due to hardware error or software malfunction.

Error in low power

Error motion due to hardware error or software malfunction.

Torque saturation in low power due to holding a hand or long object that exceeds the weight described in the specifications.

The collision detection is available for the general-purpose robots supported by the EPSON RC+7.0 Ver 7.2 or later (vertical 6-axis and SCARA robots).  If this command is used while unsupported robot (X5 series, etc.) is connected, an error occurs.

Execution of this command takes a little time.
  If cycle time is prioritized, minimize the use of this command in the program.

This function can be enabled or disabled for each joint or all joints.  The default is "all joints on". (The default is off if the firmware version is before Ver 7.2.0.x.)

The setting returns to the default when the Controller is turned off.  In other cases, the setting does not change unless otherwise configured by this command explicitly.

Output the following messages and stop the robot when the collisition is detected.

Error 5057 "Collision was detected in High power mode" (detetction of robot motion error).

Error 5058 "Collision was detected in Low power mode" (detetction of robot motion error).

For reducing damage in the High power mode, using the command with the upper torque limit by LimitTorque is also effective.   For reducing damage in Low power mode, using the command together with the upper limit torque restriction by LimitTorqueLP is also effective.

Also refer to Epson RC+ User's Guide "6.18.10  Collision Detection Function (Detection Function of Robot Motion Error)".

## Examples
```spel
CollisionDetect On       ' Turns On the collision detection for all joints
```

```spel
CollisionDetect Off, 5   ' Turns On the collision detection for only Joint #5
```

```spel
CollisionDetect          ' The result will be displayed as "on, on, on, on, off, on".
```

## See Also
LimitTorque

LimitTorque Function

CollisionDetect Statement Example

CollisionDetect On       ' Turns On the collision detection for all joints

CollisionDetect Off, 5   ' Turns On the collision detection for only Joint #5

CollisionDetect          ' The result will be displayed as "on, on, on, on, off, on".


---

# Contact Object
**Type:** reference | **Section:** Operator

## Description
Contact Object

Contact Object

Contact object moves the robot to the specified direction until it contacts with an object such as a workpiece, and stops it when contacting with the object.  This object is used for positioning of the start position for other force guide objects or the grasp position.  Even if the workpiece dimension or the grasp position of the workpiece have a margin of error, next motion or the force guide object can be executed stably since the contact position can be detected.

How to use

Properties

Results


---

# Contact Object How to Use
**Type:** reference | **Section:** Operator

## Description
Contact Object How to Use

Contact Object

How to use

1. Specify the basic information. (Name, Description, AutoStepID, StepID, AbortSeqOnFail property)

2. Specify the I/O operation of when starting this object. (IOPreprocEnabled, IOPreprocOutputBit, IOPreprocOutputStatus property)

3. Specify the mode and orientation of contact motion. (ContactPriorityMode, ContactOrient property)

4. Specify the expected distance or angle between start position and contact position. (ContactDist, ContactDistMargin, ContactAngle, ContactAngleMargin property)

5. Specify the firmness. (ContactFirmnessF, ContactFirmnessT property)

6. If you select speed priority mode, specify the speed and accel. (AccelS, AccelR, SpeedS, SpeedR property)

7. Specify the end condition. (ContactForceThresh, ContactTorqueThresh, Timeout property)

8. Specify whether to connect the force control of this object and next force guide object. (CFEnabled property)

9. Adjust parameter by cut and try. Mainly adjust the ContactStiffnessGainF, ContactStiffnessGainT, ContactForceThresh, ContactTorqueThresh, AccelS, AccelR, SpeedS, SpeedR property.


---

# Contact Properties
**Type:** reference | **Section:** Operator

## Description
Property	This property can set explanations for
		 objects.  The explanation can be freely written using up
		 to 255 characters.

Enabled
		 Property	This property can set whether to enable
		 the object.  When specifying True, the program executes the
		 object.  When specifying False, the program executes the
		 next object without executing the object.  Use this property
		 when you want to save the sequence temporary without executing
		 it or try with different parameters by copying objects during
		 sequence creation.

StepID
		 Property	This property can set an automatic assignment
		 of StepID during the object execution. When specifying True, assign
		 StepID automatically.  When specifying False, it will be
		 the value specified by StepID Property.  When assigning automatically,
		 (sequence number *100 + object number) is set.  StepID is
		 recorded to files that the force or the position during the sequence
		 execution is recorded.  It is used to determine which interval
		 corresponds to which object.

AbortSeqOnFail
		 Property	This property can set operations when
		 the object fails.  When specifying True, the program ends
		 the sequence and proceeds to the next SPEL statement if the object
		 fails.  When specifying False, the program proceeds to the
		 next force guide object without ending the sequence even if the
		 object fails.  It is used when you want to continue the sequence
		 (ex: the recovery processes are included in the sequence when
		 the object fails.)

IOPreProcEnabled
		 Property	This property sets I/O operations when
		 the force guide object starts.

I/O operations are defined by IOPreprocOutputBit
		 Property and IOPreprocOutputStatus Property.  Use this property
		 when you want to operate the hands or peripherals before the execution
		 of the force guide object.

ContactDist
		 Property	This property can set a distance between
		 the start position and the target contact position.  It is
		 used when ContactOrient is translation direction (+Fx ~ -Fz).

ContactOrient
		 Property	This property can set the target contact
		 position as seen from the start position.  You can set the
		 direction in the coordinate system specified by ForceOrient of
		 the sequence.  You can select from translation direction
		 (+Fx ~ -Fz) or rotation direction (+Tx ~ -Tz).  The robot
		 moves to the specified direction and pauses when contacting with
		 an object.

ContactDistMargin
		 Property	This property can set a margin that
		 is added to the distance between the start position and the target
		 contact position.  It is used when ContactOrient is translation
		 direction (+Fx ~ -Fz).  Normally, set 5mm.  When the
		 distance between the start position and the target contact position
		 is different such as the start position is detected by Vision
		 or height of workpieces is different, add the maximum difference.

ContactFirmnessF
		 Property	This property set a gain that shows
		 firmness of force control functions during execution of Contact
		 object.  It is used when ContactOrient is translation direction
		 (+Fx ~ -Fz).  When ContactFirmnessF increases, the force
		 control function will be strong.  Response to changes of
		 the force is slow, however, oscillation does not occur.  When
		 ContactFirmnessF decreases, the force control function will be
		 weak.  Response to changes of the force is fast, however,
		 oscillation is easy to occur.

ContactFirmnessT
		 Property	This property set a gain that shows
		 firmness of force control functions during execution of Contact
		 object.  It is used when ContactOrient is rotation direction
		 (+Tx ~ -Tz).  When ContactFirmnessT increases, the force
		 control function will be strong.  Response to changes in
		 the force control functions will be slow, however, oscillation
		 does not occur. When ContactFirmnessT decreases, the force control
		 function will be weak.  Response to changes of the force
		 is fast, however, oscillation is easy to occur.

CFEnabled
		 Property	This property set whether to continue
		 the force control functions after the objects are ended.  When
		 specifying True, the force control functions will continue even
		 if the objects are ended.  When specifying False, the force
		 control functions will end when the objects are ended.  When
		 the sequence ends even if CFEnabled is True, the force control
		 functions will end.

ContactForceThresh
		 Property	This property can set threshold of force
		 to determine contact.  It is used when ContactOrient is translation
		 direction (+Fx ~ -Fz).  If the threshold set by this property
		 is exceeded during execution of Contact object, the robot recognizes
		 the contact and pauses motion, then proceeds to the next object.

ContactTorqueThresh
		 Property	This property can set threshold of torque
		 to determine the contact.  It is used when ContactOrient
		 is rotation direction (+Tx ~ -Tz).  If the threshold set
		 by this property is exceeded during execution of Contact object,
		 the robot recognizes the contact and pauses motion, then proceeds
		 to the next object.


---

# Contact Results
**Type:** reference | **Section:** Operator

## Description
Result	Description

EndStatus	It is a result of the execution.

Time	It is the required time for execution.

TimedOut	It is whether the time-out period set
		 in Timeout property had been reached.

EndForces	It is force and torque when force guide
		 object ends.

EndPos	Positions when the force guide object
		 ends.

AvgForces	Average values of force and torque during
		 the force guide object execution.

PeakForces	Peak values of force and torque during
		 the force guide object execution.

ForceCondOK	It is whether to satisfy the end conditions
		 related to force.

TriggeredForces
		 Result	It is the force and torque when satisfying
		 the end conditions related to force.

Acquire values of Fx, Fy, Fz, Tx, Ty,
		 and Tz.

Unit: Fx, Fy, Fz [N] / Tx, Ty, Tz [N.mm]

TriggeredPos
		 Result	Positions when satisfying the end conditions
		 related to force.  Acquire values of X, Y, Z, U, V, and W.

Unit: X, Y, Z [mm] / U, V, W [deg]


---

# ContactDist Property
**Type:** property | **Section:** Operator

## Description
This property sets an assumed distance between the start position and the hole position.

When the robot moves ContactDist + ContactDistMargin, it determines as "a hole is detected" and proceeds to the next force object.

Values

Minimum value 0.1

Maximum value 50

Default:  10

See Also: ContractDist Property

ContactOrient Property

## See Also
Applies To

ContactProbe Object


---

# ContactDistMargin Property
**Type:** property | **Section:** Operator

## Description
This property sets a margin which is added to a distance between the start point and the hole position.

Be sure to set a value with consideration for the maximum difference of the each distance. When the robot moves ContactDist + ContactDistMargin, it determines as "a hole is detected" and proceeds to the next force object.

Values

Minimum value 0.1

Maximum value 50

Default:  10

See Also: ContractDistMargin Property

ContactDist Property

## See Also
Applies To

ContactProbe Object


---

# ContactFirmnessF Property
**Type:** property | **Section:** Operator

## Description
Set a firmness of the force control functions.

ContactFirmnessF : When ContactOrient is Fx, Fy, Fz

## Notes
When setting a large value:

The force control function will become stronger.

However, response to changes of the force/torque is slow.

When setting a small value:

The force control function will become weaker.  Response to changes of the force/torque is fast, however, vibration is easy to occur.

When setting a small absolute value:

Movement speed of the contact motion will be fast.

See Also: ContractFirmnessF Property

ContactFirmnessT Property

## See Also
Applies To

Contact Object, ContactProbe Object


---

# ContactFirmnessT Property
**Type:** property | **Section:** Operator

## Description
This property sets a firmness of force control functions during execution of the force guide object.

It is used when ContactOrient is rotation direction (+Tx to -Tz).

When the value of ContactFirmnessT increases, the force control function will become stronger.  Response to changes of the torque is slow, however, vibration does not occur.

When the value of ContactFirmnessT decreases, the force control function will become weaker.  Response to changes of the torque is fast, however, vibration is easy to occur.

Values

Minimum value 10

Maximum value 1000000

Default:  3000

See Also: ContractFirmnessT Property

ContactFirmnessF Property

## See Also
Applies To

Contact Object


---

# ContactForceThresh Property
**Type:** property | **Section:** Operator

## Description
This property sets a threshold of force to determine the contact.

It is used when ContactOrient is the translation direction (+Fx to -Fz).

If the threshold set by this property is exceeded during execution of Contact object, the robot recognizes that the robot is contacted and stops the motion.  Then, proceed to the next force guide object.

Values

When ContactOrient is in positive direction:

Minimum value -10

Maximum value 0

Default:  -5

When ContactOrient is in negative direction:

Minimum value 0

Maximum value 10

Default:  5

See Also: ContractForceThresh Property

ContactOrient Property

## See Also
Applies To

Contact Object, ContactProbe Object


---

# ContactOrient Property
**Type:** property | **Section:** Operator

## Description
Contact Object:

This property sets a target contact position as viewed from the start position.

Set the direction in the coordinate system specified by ForceOrient of the force guide sequence.  You can select from translation direction (+Fx to -Fz) or rotation direction (+Tx to -Tz).

The robot moves to the specified direction and stops when contacting with an object.

ContactProbe Object:

Set a hole direction.

Set the direction in the coordinate system specified by ForceOrient of the force guide sequence.  Select from translation direction (+Fx to -Fz).

The robot probes a hole while moving to the specified direction.

Values

Contact Object:

Value	Description

+Fx	Move to the positive direction in Fx.

-Fx	Move to the negative direction in Fx.

+Fy	Move to the positive direction in Fy.

-Fy	Move to the negative direction in Fy.

+Fz	Move to the positive direction in Fz.

-Fz	Move to the negative direction in Fz.

+Tx	Move to the positive direction in Tx.

-Tx	Move to the negative direction in Tx.

+Ty	Move to the positive direction in Ty.

-Ty	Move to the negative direction in Ty.

+Tz	Move to the positive direction in Tz.

-Tz	Move to the negative direction in Tz.

Default: +Fz

ContactProbe Object:

Value	Description

+Fx	Move to the positive direction in Fx.

-Fx	Move to the negative direction in Fx.

+Fy	Move to the positive direction in Fy.

-Fy	Move to the negative direction in Fy.

+Fz	Move to the positive direction in Fz.

-Fz	Move to the negative direction in Fz.

Default: +Fz

## Notes
See Also: ContractOrient Property

ContactDist Property

## See Also
Applies To

Contact Object, ContactProbe Object


---

# ContactTorqueThresh Property
**Type:** property | **Section:** Operator

## Description
This property sets a threshold of torque to determine the contact.

It is used when ContactOrient is rotation direction (+Tx to -Tz).

If the threshold set by this property is exceeded during execution of Contact object, the robot recognizes the contact and stops the motion.  Then, proceed to the next force guide object.

Values

When ContactOrient is in positive direction:

Minimum value -1000

Maximum value 0

Default:  -200

When ContactOrient is in negative direction:

Minimum value 0

Maximum value 1000

Default:  -200

See Also: ContractTorqueThresh Property

ContactOrient Property

## See Also
Applies To

Contact Object


---

# Control Panel page, Robot Manager Dialog
**Type:** reference | **Section:** Operator

## Description
Control Panel page, Robot Manager Dialog

Control Panel Page, Robot Manager Window

The [Robot Manager] window contains buttons for basic robot operations, such as turning motors on/off. It shows the emergency stop, safeguard, and error status.

Item	Description

Robot	Select
		 a robot.

Emergency
		 Stop	Indicates
		 if Emergency Stop has occurred. The display will show red if an
		 Emergency Stop has occurred.

To clear the Emergency Stop status, click
		 the [Reset] button.

Safeguard	Indicates
		 whether the Safeguard input is on or off. When on, the display
		 is yellow.

Error	Indicates
		 whether an error status has occurred. When an error occurs, the
		 display is red.

Motor:
		 Off / On	Turns
		 all robot motors on or off.

Power:
		 Low / High	Puts
		 the robot servo system in high power mode or low power mode.

Reset	Resets
		 the robot servo system and Emergency Stop condition.

Local	This
		 drop down list is used to select the local coordinate system for
		 jogging and teaching.

Tool	This
		 drop down list is used to select the tool for jogging and teaching.

Arm	This
		 drop down list is used to select the arm for jogging and teaching.
		 Vertical 6-axis robot (including the N series) are not shown.

ECP	This
		 drop down list is used to select the ECP for jogging.

VRT	This
		 drop down list is used to select the number set for VRT parameters.

When you switch to the [Robot Manager] window, the robot's speed setting will be set to the speed (high, low) on the Jog & Teach window.

Motion command after the above operation will be executed at this speed. Set the speed again by the commands such as Motor, Speed, and Accel.


---

# Controller command (Tools menu)
**Type:** reference | **Section:** Operator

## Description
Controller command (Tools menu)

[Controller] Command (Tools Menu)

Select Controller from the [Tools] menu to open the [Controller Tools] dialog box.

From the [Controller Tools] dialog box, you can save and restore the complete controller configuration and the project using the [Backup Controller] and [Restore Controller] commands. You can also save and view controller status, and reset the controller.

Before servicing the system, you should execute [Backup Controller] and store the system configuration on an external media such as a USB memory key.

If required, you can use [Restore Controller] to restore previously stored data.


---

# Controlling position accuracy
**Type:** reference | **Section:** Operator

## Description
Controlling position accuracy

Controlling position accuracy

Use the Fine command to adjust position accuracy for the end of a motion command.  Fine specifies, for each joint, the allowable positioning error for detecting completion of any given move.  The lower the Fine settings, the more accurate the final position of the joint, which can cause slower performance.  Conversely, large Fine settings can speed up motion commands, but position accuracy will decrease.  For many applications, the default settings can be used.


---

# Cos Function
**Type:** reference | **Section:** Operator

## Syntax
```
Cos(
			number
			)
```

## Parameters
number	Numeric expression in Radians.

## Description
Cos returns the cosine of the numeric expression.  The numeric expression (number) must be in radian units.  The value returned by the Cos function will range from -1 to 1

To convert from degrees to radians, use the DegToRad function.

## Examples
```spel
Function costest

Real x
		  Print "Please enter a value in degrees"
		  Input x
		  Print "COS of ", x, " is ", Cos(DegToRad(x))
		Fend
```

```spel
>print cos(0.55)
```

```spel
0.852524522059506
```

```spel
>
```

```spel
>print cos(DegToRad(30))
```

```spel
0.866025403784439
```

```spel
>
```

## See Also
Abs	Sgn

Atan	Sin

Atan2	Sqr

Int	Str$

Mod	Tan

Not	Val

Cos Function Example

The following example shows a simple program which uses Cos.

Function costest

Real x

		  Print "Please enter a value in degrees"

		  Input x

		  Print "COS of ", x, " is ", Cos(DegToRad(x))

		Fend

The following examples use Cos from the Command window.

Display the cosine of 0.55:

>print cos(0.55)

0.852524522059506

>

Display cosine of 30 degrees:

>print cos(DegToRad(30))

0.866025403784439

>


---

# Creating the simplest application
**Type:** reference | **Section:** Operator

## Description
Creating the simplest application

Creating the simplest application

The simplest SPEL+ application has one program and one point file. This is what is automatically defined for you when you create a new project. A blank program named "Main.prg" and a blank point file named "Points.pts" are created.

To write and run a simple application

Select
	 [New Project] from the [Project]
	 menu to create a new project.

Write
	 your program source code in the file that was created for you called
	 "Main.prg".

Teach
	 the robot points using the [Robot Manager]-[Jog
	 & Teach] page.

Run
	 the program by selecting [Run] Window from the [Run] menu or by pressing
	 [F5] (the shortcut key for the [Start] command).


---

# Ctr Function
**Type:** reference | **Section:** Operator

## Syntax
```
Ctr(bitNumber)
```

## Parameters
bitNumber	Number of the Hardware Input bit set as a counter. Only 16 counters can be active at the same time.

## Description
Ctr works with the CTReset statement to allow Hardware inputs to be used as counters.

Each time a hardware input specified as a counter is switched from the Off to On state that input causes the counter to increment by 1.

The Ctr function can be used at any time to get the current counter value for any counter input.  Any of the Hardware Inputs can be used as counters.  However, only 16 counters can be active at the same time.

Counter Pulse Input Timing Chart

## Examples
```spel
CTReset 3 'Reset counter for input 3 to 0
		On 0 'Turn an output switch on

Wait Ctr(3) >= 5
		Off 0 'When 5 input cycles are counted for Input 3 turn

			'switch off (output 0 off)
```

## See Also
CTReset

Ctr Function Example

The following example shows a sample of code which could be used to get a hardware input counter value.

CTReset 3 'Reset counter for input 3 to 0

		On 0 'Turn an output switch on

Wait Ctr(3) >= 5

		Off 0 'When 5 input cycles are counted for Input 3 turn

'switch off (output 0 off)


---

# Curve Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Curve fileName, closure, mode, numAxes, pointList
```

## Parameters
fileName	A string expression for the name of the file in which the point data is stored. The specified fileName will have the extension .CVT appended to the end so no extension is to be specified by the user. When the Curve instruction is executed, fileName will be created.

You cannot specify a file path and fileName doesn't have any effect from ChDisk. See ChDisk for the details.

closure	Specifies whether or not the defined Curve is Closed or left Open at the end of the curved motion.  This parameter must be set to one of two possible values, as shown below.
 C - Closed Curve
 O - Open Curve

When specifying the open curve, the Curve instruction creates the data to stop the arm at the last point of the specified point series.  When specifying the closed curve, the Curve instruction creates the data required to continue motion through the final specified point and then stopping motion after returning the arm to the starting point of the specified point series for the Curve instruction.

Mode Setting	Tangential Correction	ECP Number

Hexadecimal	Decimal	No

&H00	0	0

&H10	16	1

&H10	32	2

...	...	...

&HA0	160	10

&HB0	176	11

&HC0	192	12

&HD0	208	13

&HE0	224	14

&HF0	240	15

&H02	2	Yes	0

&H12	18	1

&H22	34	2

...	...	...

&HA2	162	10

&HB2	178	11

&HC2	194	12

&HD2	210	13

&HE2	226	14

&HF2	242	15

When specifying tangential correction, Curve uses only the U-Axis coordinate of the starting point of the point series.  Tangential correction continuously maintains tool alignment tangent to the curve in the XY plane.  It is specified when installing tools such as cutters that require continuous tangential alignment.  When specifying a closed curve (using the closure parameter) with Automatic Interpolation in the tangential direction of the U-Axis, the U-Axis rotates 360 degrees from the start point.  Therefore, before executing the CVMove instruction, set the U-Axis movement range using the Range instruction so the 360 degree rotation of the U-Axis does not cause an error.

When using ECP, specify the ECP number in the upper four bits.

When generating a curve considering the additional axis position included in the point data, specify the nineth bit as 1. For example, when using no orientation offset or ECP and generating a curve considering the additional axis position, specify &H100.

When generating a curve for the additional axis, join the continuous point data of S axis and T axis separately from the robot coordinate system.

However if the additional axis is consisted of the PG axis, it doesn't generate a curve with the continuous point but creates the data to move to the final point.

15

numAxes	Integer number 2, 3, 4 or 6 which specifies the number of axes controlled during the curve motion as follows:

2 - Generate a curve in the XY plane with no Z Axis movement or U Axis rotation.

(except for 6-Axis robots (including N series))

3 - Generate a curve in the XYZ space with no U axis rotation.

(except for 6-Axis robots (including N series))

4 - Generate a curve in the XYZ space with U-Axis rotation.

(except for 6-Axis robots (including N series))

6 - Generate a curve in the XYZ space with U, V, and W axes rotation

(6-Axis robots (including N series) only).

The axes not selected to be controlled during the Curve motion maintain their previous encoder pulse positions and do not move during Curve motion.

pointList	{ point expression | P(start : finish) } [, output command ] ...

This parameter is actually a series of Point Numbers and optional output statements either separated by commas or an ascended range of points separated by a colon.  Normally the series of points are separated by commas as shown below:
 Curve "MyFile", O, 0, 4, P1, P2, P3, P4
 Sometimes the user defines a series of points using an ascending range of points as shown below:
 Curve " MyFile", O, 0, 4, P(1:4)
 In the case shown above the user defined a curve using points P1, P2, P3, and P4.

output command is optional and is used to control output operation during curve motion. The command can be On or Off for digital outputs or memory outputs.  Entering an output command following any point number in the point series causes execution of the output command when the arm reaches the point just before the output command.  A maximum of 16 output commands may be included in one Curve statement.  In the example below, the "On 2" command is executed just as the arm reaches the point P2, then the arm continues to all points between and including P3 and P10.
 Curve "MyFile", C, 0, 4, P1, P2, ON 2, P(3:10)

## Description
Curve creates data that moves the manipulator arm along the curve defined by the point series pointList and stores the data in a file on the controller.  The CVMove instruction uses the data in the file created by Curve to move the manipulator in a continuous path type fashion.

The curve file is stored in the compact flash inside of the controller. Therefore, Curve starts writing into the compact flash. Frequent writing into the compact flash will shorten the compact flash lifetime. We recommend using Curve only for saving the point data.

The created data is Curve information defined on the orthogonal coordinate system.  It is not necessary to specify speeds or accelerations prior to executing the Curve instruction.  Arm speed and acceleration parameters can be changed anytime prior to executing CVMove by using the Speeds or Accels instructions.

Curve calculates independent X, Y, Z, U, V, W coordinate values for each point using a cubic spline function to create the trajectory.  Therefore, if points are far apart from each other or the orientation of the robot is changed suddenly from point to point, the desired trajectory may not to be realized.

It is not necessary to specify speeds or accelerations prior to executing the Curve instruction. Arm speed and acceleration parameters can be changed anytime prior to executing CVMove by using the Speeds or Accels instructions.

Points defined in a local coordinate system may be used in the series to locate the curve at the desired position.  By defining all of the specified points in the point series for the Curve instruction as points with local attributes, the points may be changed as points on the local coordinate system by the Local instruction following the Curve instruction.

## Notes
Use tangential correction when possible

It is recommended that you use tangential correction whenever possible, especially when using CVMove in a continuous loop throught the same points.  If you do not use tangential correction, the robot may not follow the correct path at higher speeds.

Open Curve Min and Max Number of Points Allowed

Open Curves may be specified by using from 3 to 200 points.

Closed Curve Min and Max Number of Points Allowed

Closed Curves may be specified by using from 3 to 50 points.

Compatibility of file

Files created after firmware Ver.7.5.1 are not available for earlier versions of firmware. Also, files created firmware Ver.7.5.1 or earlier can be used with firmware Ver.7.5.1 or later.

Potential Errors

Attempt to Move Arm Outside Work Envelope

The Curve instruction cannot check the movement range for the defined curve path.  This means that a user defined path may cause the robot arm to move outside the normal work envelope. In this case an "out of range" error will occur.

## Examples
```spel
Set up curve
```

```spel
> curve "mycurve", O, 0, 4, P1, P2, On 2, P(3:7)
```

```spel
Move the arm to P1 in a straight line
```

```spel
> jump P1
```

```spel
Move the arm according to the curve definition called mycurve
```

```spel
> cvmove "mycurve"
```

## See Also
Robot motion commands

Accels

Arc

CVMove

Move

Speeds

Curve Statement Example

The following example designates the free curve data file name as MYCURVE.CVT, creates a curve tracing P1-P7, switches ON output port 2 at P2, and decelerates the arm at P7.

Set up curve

> curve "mycurve", O, 0, 4, P1, P2, On 2, P(3:7)

Move the arm to P1 in a straight line

> jump P1

Move the arm according to the curve definition called mycurve

> cvmove "mycurve"


---

# Curves
**Type:** reference | **Section:** Operator

## Description
Curves

Curves

Curves commands move the robot in a circular arc.
  Curves is a CP (Continuous Path) motion.

To set the velocity (speed) for Curves, use the SpeedS command.  To set acceleration and deceleration, use the AccelS command.

Command	Description

Arc	Move the robot through one point to another point using circular interpolation.

Curve	Defines a free curve for CP motion control of the robot.

CVMove	Executes the continuous path defined with the Curve instruction.


---

# Data Types
**Type:** reference | **Section:** Operator

## Description
Data Types

Data Types

You can declare different types of data in your program. All variables must be declared.

The following table shows the different data types for the SPEL+ language.

Data Type	Size	Range

Boolean	2 byte	True or
		 False

Byte	2 byte	−128 to
		 +127

Double	8 bytes	−1.79E+308
		 to 1.79E+308  Number of significant figure is 14

Int32	4 bytes	−2147483648
		 to +2147483647

Int64	8 bytes	−9223372036854775808

to +9223372036854775807

Integer	2 byte	−32768 to
		 +32767

Long	4 bytes	−2147483648
		 to +2147483647

Real	4 bytes	−3.40E+38
		 to 3.40E+38 Number of significant figure is 6

Short	2 bytes	−32768 to
		 +32767

String	256 bytes	All ASCII
		 characters  Up to 255 characters

UByte	2 bytes	0 to +255

UInt32	4 bytes	0 to 4294967295

UInt64	8 bytes	0 to 18446744073709551615

UShort	2 bytes	0 to 65535


---

# Declare Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Declare funcName, "dllFile", "alias" [, (argList)] As type
```

## Parameters
funcName	The name of
		 the function as it will be called from your program.

dllFile	The path and
		 name of the library file. This must be a literal string (characters
		 delimited by quotation marks). You may also use a macro defined
		 by #define. If there is no path specified, then RC+ will look
		 for the file in the current project directory. If not found, then
		 it is assumed that the file is in the Windows system32 directory.
		 The file extension can be omitted, but is always assumed to be
		 .DLL.

alias	Optional.
		 The actual name of the function in the DLL or the function index.
		 The name is case sensitive. The alias must be a literal string
		 (characters delimited by quotation marks). If you use an index,
		 you must use a # character before the index. If omitted, a function
		 name specified by funcName can be used as a name of function in
		 DLL.

arglist	Optional.
		 List of the DLL arguments. See syntax below.

type	Required.
		 You must declare the type of function.

The arglist argument has the following syntax:

[ {ByRef | ByVal} ] varName [( )] As varType

ByRef	Optional.
		 Specify ByRef when you refer to the variable to be seen by the
		 calling function. In this case, the argument change in a function
		 can be reflected to the variable of the calling side. You can
		 change the values received as a reference.

ByVal	Optional.
		 Specify ByVal when you do not want any changes in the value of
		 the variable to be seen by the calling function. This is the default.

varName	Required.
		 Name of the variable representing the argument; follows standard
		 variable naming conventions. If you use an array variable as argument,
		 you must specify ByRef.

varType	Required.
		 You must declare the type of argument.

## Description
Use Declare to call DLL functions from any program in the current program group. Declare must be used outside of functions.

The Declare statement checks that the DLL file and function exist at compile time.

Passing Numeric Variables ByVal

SPEL: Declare MyDLLFunc, "mystuff.dll", "MyDLLFunc", (a As Long) As Long

VC++ long _stdcall MyDllFunc(long a);

Passing String Variables ByVal

SPEL: Declare MyDLLFunc, "mystuff.dll", "MyDLLFunc", (a$ As String) As Long

VC++ long _stdcall MyDllFunc(char *a);

Passing Numeric Variables ByRef

SPEL: Declare MyDLLFunc, "mystuff.dll", "MyDLLFunc", (ByRef a As Long) As Long

VC++ long _stdcall MyDllFunc(long *a);

Passing String Variables ByRef

SPEL: Declare MyDLLFunc, "mystuff.dll", "MyDLLFunc", (ByRef a$ As String) As Long

VC++ long _stdcall MyDllFunc(char *a);

When you pass a string using ByRef, you can change the string in the DLL.  Maximum string length is 256 characters.
  You must ensure that you do not exceed the maximum length.

You must also ensure that space is allocated for the string before calling the DLL.  It is best to allocate 256 bytes by using the Space$ function, as shown in the following example.

Declare ChangeString, "mystuff.dll", "ChangeString", (ByRef a$ As String) As Long

Function main

String a$

' Allocate space for string before calling DLL

a$ = Space$(256)

Call ChangeString(a$)

Print "a$ after DLL call is: ", a$

Fend

Passing Numeric Arrays ByRef

SPEL: Declare MyDLLFunc, "mystuff.dll", "MyDLLFunc", (ByRef a() As Long) As Long

VC++ long _stdcall MyDllFunc(long *a);

Returning Values from DLL Function

The DLL function can return a returning value for any data type, except String.  When it is needed to return string, refer to "Passing String Variables ByRef" described above and specify string variables as an argument.

If string variables are specified to a returning value, error 3614 "You cannot specify a String for Declare return data type." will occur.

VarType

Following shows table of data type of Epson RC+ 8.0 and variable type of C/C++.

Since there is no data for Epson RC+ 8.0, byte type of C/C++ and structure cannot be used.

Table of data type for Epson RC+ 8.0 and C/C++

Epson
		 RC+ 8.0	C/C++

Boolean	short

Byte	short

Short	short

Integer	short

Long	int

Real	float

Double	double

String	char [256]  * includes Null

For example:

Declare ReturnLong, "mystuff.dll", "ReturnLong", As Long

Function main

  Print "ReturnLong = ", ReturnLong

Fend

## Examples
```spel
Declare ChangeString, "mystuff.dll", "ChangeString", (ByRef a$ As String) As Long
```

```spel
Function main
String a$

' Allocate space for string before calling DLL
a$ = Space$(256)
Call ChangeString(a$)
Print "a$ after DLL call is: ", a$
Fend
```

```spel
Declare ReturnLong, "mystuff.dll", "ReturnLong", As Long

Function main Print "ReturnLong = ", ReturnLong
Fend
```

```spel
Declare MyDLLTest, "mystuff.dll", "MyDLLTest" As Long

Function main Print MyDLLTest
Fend
```

```spel
' Declare a DLL function with two integer arguments
' and use a #define to define the DLL file name

#define MYSTUFF "mystuff.dll"

Declare MyDLLCall, MYSTUFF, "MyTestFunc", (var1 As Integer, var2 As Integer) As Integer

' Declare a DLL function using a path and index.
Declare MyDLLTest, "c:\mydlls\mystuff.dll", "#1" As Long
```

## See Also
Call

Function...Fend

Declare Statement


---

# DegToRad Function
**Type:** reference | **Section:** Operator

## Syntax
```
DegToRad(
			degrees
			)
```

## Parameters
degrees	Real expression representing the degrees to convert to radians.

## Description
DegToRad Function

DegToRad Function

See_Also Example

Converts degrees to radians.

## Examples
```spel
s = Cos(
				DegToRad
			(x))
```

## See Also
Atan

Atan2

RadToDeg

DegToRad Function Example

s = Cos(
				DegToRad
			(x))


---

# Description Property
**Type:** property | **Section:** Operator

## Description
Force Guide

Property

This property sets descriptions about force guide sequences and objects.

You can set the character string up to 255 characters.

## See Also
Applies To

Sequence, All Objects
 Property

Name Property


---

# Do...Loop Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Do [ { While | Until } condition ]

[statements]

[Exit Do]

[statements]

Loop

Or, you can use this syntax:

Do

[statements]

[ Exit Do ]

[statements]

Loop [ { While | Until } condition ]

The Do Loop statement syntax has these parts:

Part	Description

condition	Optional.
		 Numeric expression or string expression that is True or False.
		 If condition is Null,
		 condition is treated as False.

statements	One or more
		 statements that are repeated while, or until, condition
		 is True.
```

## Description
Any number of Exit Do statements may be placed anywhere in the Do...Loop as an alternate way to exit a Do...Loop. Exit Do is often used after evaluating some condition, for example, If...Then, in which case the Exit Do statement transfers control to the statement immediately following the Loop.

When used within nested Do...Loop statements, Exit Do transfers control to the loop that is one nested level above the loop where Exit Do occurs.

Note

DO NOT use XQT command repeatedly in Loop statements.

Do not use XQT command repeatedly in Loop statements such as Do...Loop.

The controller may freeze up.  If you use Loop statements repeatedly, make sure to add  Wait command (Wait 0.1).

Avoid endless execution of empty Loop Statements and similar to them, use them with the Wait command instead

Do not use empty Do...Loop statements and similar commands to avoid effect on the system. The Controllers are detecting endless loop tasks. If the controller determines that the system will be affected, it will stop the program with error 2556 (An excessive loop was detected). When performing operations that require a loop or waiting for I/O, execute a Wait command (Wait 0.1) and more within the loop to avoid occupying the CPU.

When you exit the loop from the nested structure without using Exit Do

Error 2020 will occur when you repeatedly execute the program which exits the loop by the command other than the Exit For command (such as GoSub statement, Goto statement, and Call statement.)
  Be sure to use Exit Do command to exit the loop.

## Examples
```spel
Do While Not Lof(1) Line Input #1, tLine$ Print tLine$
Loop
```

## See Also
For...Next

Select...Send

Do Example

Do While Not Lof(1)

  Line Input #1, tLine$

  Print tLine$

Loop


---

# Double Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Double varName [( subscripts )] [, varName [( subscripts )]...]
```

## Parameters
varName	Variable name which the user wants to declare as type Double.

subscripts	Optional.  Dimensions of an array variable; up to 3 dimensions may be declared.  The subscripts syntax is as follows

(ubound1, [ubound2], [ubound3])

ubound1, ubound2, ubound3 each specify the maximum upper bound for the associated dimension.

The elements in each dimension of an array are numbered from 0 and the available number of array elements is the upper bound value + 1.

When specifying the upper bound value, make sure the number of total elements is within the range shown below:

Local variable   2000

Global Preserve variable   4000

Global variable and module variable   100000

## Description
Double is used to declare variables as type Double.  Local variables should be declared at the top of a function.  Global and module variables must be declared outside of functions.  Valid number of digits for Double is 14.

## Examples
```spel
Function doubletest Double var1 Double A(10) 'Single dimension array of double Double B(10, 10) 'Two dimension array of double Double C(5, 5, 5) 'Three dimension array of double Double arrayvar(10) Integer i Print "Please enter a Number:" Input var1 Print "The variable var1 = ", var1 For i = 1 To 5
    Print "Please enter a Number:"
    Input arrayvar(i)
    Print "Value Entered was ", arrayvar(i) Next I
Fend
```

## See Also
Data Types Overview

Variable Declarations

Variable Naming Conventions

Boolean

Byte

Global

Int32

Integer

Long

Real

Short

String

UByte

UInt32

UShort

Double Statement Example

The following example shows a simple program which declares some variables using Double.

Function doubletest

  Double var1

  Double A(10) 'Single dimension array of double

  Double B(10, 10) 'Two dimension array of double

  Double C(5, 5, 5) 'Three dimension array of double

  Double arrayvar(10)

  Integer i

  Print "Please enter a Number:"

  Input var1

  Print "The variable var1 = ", var1

  For i = 1 To 5

    Print "Please enter a Number:"

    Input arrayvar(i)

    Print "Value Entered was ", arrayvar(i)

  Next I

Fend


---

# ECP Coordinate Systems (Option)
**Type:** reference | **Section:** Operator

## Description
ECP Coordinate Systems (Option)

ECP Coordinate Systems (Option)

Specify a coordinate system whose origin point is on the tip of the outside fixed tool (hereafter referred to as the external control point or ECP) to move the robot arm holding a part in the trajectory made on the external control point along with the part's edges.

The following figures give a concrete example.

An ordinal Move statement controls the moving speed and orientation change of the tool center point (TCP). In the case of Move statement with the ECP argument, the part's edge is controlled to take a straight and constant-speed trajectory instead of TCP.

In the following example of no ECP, TCP takes a straight trajectory but the part's edge is distant from ECP.

If there is no orientation change, the trajectory is the same as normal operation of Move command.

The following commands are available for optional ECP:

	Move command
	Arc3 command
	Curve and CVMove commands
	ECP jog motion in Robot Manager

Use the ECPSet statement for defining an ECP coordinate system.  A maximum of 15 ECP coordinate systems can be defined.

For details, refer to ECP Motion.


---

# ECP Motion Title
**Type:** reference | **Section:** Operator

## Description
ECP Motion Title

ECP Motion

Overview

How to move the arm with ECP motion


---

# ECP Overview
**Type:** reference | **Section:** Operator

## Description
ECP Overview

ECP Overview

An ECP (external control point) motion is when the robot arm holding a part follows a specified trajectory (part's edges, etc.) using an outside fixed tool.

The ECP option supports the following:

ECP definition by ECPSet statement and selection by ECP statement
ECP motion commands (additional functions of Move, Arc3, Curve and CVMove commands)
Teaching with ECP jogging

This option is available for SCARA (including RS series), Cartesian and 6-axis robots (including N series).  Also, it can be used with multi-robot systems.

Up to 15 ECP coordinate systems can be defined.


---

# ECPSet Statement
**Type:** reference | **Section:** Operator

## Syntax
```
(1) ECPSet  ECPNum, ECPPoint

(2) ECPSet   ECPNum

(3) ECPSet
```

## Parameters
ECPNum	Integer number from 1-15 representing which of 15 external control points to define.

ECPPoint	P number or P(expr) or point label or point expression.

## Description
Defines an external control point.

Robot parameter data is stored in compact flash in controller.  Therefore, writing to command flash occurs when executing this command.  Frequent writing to compact flash affect to lifetime of compact flash.  We recommend to use this command minimally.

Note

This command will only work if the External Control Point option is installed.

ECPSet Example

ECPSet 1, P1

ECPSet 2, 100, 200, 0, 0

## Examples
```spel
ECPSet 1, P1
ECPSet 2, 100, 200, 0, 0
```


---

# ECPSet page: Robot Parameters
**Type:** reference | **Section:** Operator

## Description
ECPSet page: Robot Parameters

[Tools]-[Robot Manager]-[ECP] Page

This page allows you to define ECP (external control point) settings for a robot. When the page is selected, the current values are displayed. When an ECP is undefined, then all fields for that ECP will be blank. When you enter a value in any of the fields for an undefined ECP setting, then the remaining fields will be set to zero. The ECP will be defined when you press the [Apply] button.

If the ECP option is not enabled in the controller, this page will not be visible.

For detailed information on using external control points in your application, refer to ECP Coordinate Systems (Option).

Navigating the grid

Press the [Tab] key to move to the next cell. Press the [Shift] + [Tab] key to move to the previous cell. Press the arrow [↑] or [↓] key to move to the cell above or below.

Item	Description

X	The X
		 coordinate of the ECP.

Y	The Y
		 coordinate of the ECP.

Z	The Z
		 coordinate of the ECP.

U	Rotation
		 angle of the ECP about the Z axis. (roll)

V	Rotation
		 angle of the ECP about the Y axis. (pitch)

W	Rotation
		 angle of the ECP about the X axis. (yaw)

Apply	Sets
		 the current values.

Restore	Reverts
		 to the previous values.

Clear	Clears
		 all values.


---

# EResume Statement
**Type:** reference | **Section:** Operator

## Syntax
```
EResume [{ label | Next }
			]
```

## Description
EResume

If the error occurred in the same procedure as the error handler, execution resumes with the statement that caused the error. If the error occurred in a called procedure, execution resumes at the Call statement in the procedure containing the error-handler.

EResume Next

If the error occurred in the same procedure as the error handler, execution resumes with the statement immediately following the statement that caused the error.  If the error occurred in a called procedure, execution resumes with the statement immediately following the Call statement that last in the procedure containing the error-handler.

EResume { label }

If the error occurred in the same procedure as the error handler, execution resumes at the statement containing the label.

## Examples
```spel
Function main
		  Integer retry
		  OnErr GoTo eHandler
		  Do
		    RunCycle
		  Loop
		  Exit Function
```

```spel
eHandler:
		  Select Err
		    Case MyError
		      retry = retry + 1
		      If retry < 3 Then

			        EResume
   ' try again
		      Else
		        Print "MyError has occurred ", retry, " times
```

```spel
EndIf
		  Send
		Fend
```

## See Also
OnErr

EResume Statement Example

Function main

		  Integer retry

		  OnErr GoTo eHandler

		  Do

		    RunCycle

		  Loop

		  Exit Function

eHandler:

		  Select Err

		    Case MyError

		      retry = retry + 1

		      If retry < 3 Then

EResume
   ' try again

		      Else

		        Print "MyError has occurred ", retry, " times

      EndIf

		  Send

		Fend


---

# EStopOn Function
**Type:** reference | **Section:** Operator

## Syntax
```
EStopOn
```

## Description
EStopOn function is used only for NoEmgAbort task (special task using NoEmgAbort at Xqt)

## Notes
Forced Flag

This program example uses Forced flag for On/Off command.

Be sure that the I/O outputs change during error, or at Emergency Stop or Safety Door Open when designing the system.

Error Handling

As this program, finish the task promptly after completing the error handling.

Outputs OFF during Emergency Stop

As this program example, when the task executes I/O On/Off after the Emergency Stop, uncheck the [Controller]-[Preferences]-[Outputs off during emergency stop] check box. If this check box is checked, the execution order of turn Off by the controller and turn On using the task are not guaranteed.

Function main

  Xqt EStopMonitor, NoEmgAbort

  ...

  ...

Fend

Function EStopMonitor

  Wait EStopOn

   Print "EStop !!!"

  Off 10, Forced

  On 12, Forced

Fend

## See Also
Returns the Emergency Stop status.

ErrorOn

SysErr

Wait

Xqt

EStopOn Function Example

The following example shows a program that monitors the Emergency Stop and switches the I/O On/Off when Emergency Stop occurs.


---

# Elbow Function
**Type:** function | **Section:** Operator

## Syntax
```
Elbow [(point)]
```

## Parameters
point	Optional.  Point expression.  If point is ommitted, then the elbow orientation of the current robot position is returned.

## Description
Elbow Function

Elbow Function

See_Also

## Examples
```spel
Print Elbow(pick)

Print Elbow(P1)

Print Elbow

			Print Elbow(P1 + P2)
```

## See Also
Elbow Statement, Hand, Wrist, J4Flag, J6Flag

Elbow Function Example

Print Elbow(pick)

Print Elbow(P1)

Print Elbow

Print Elbow(P1 + P2)


---

# Elbow Keyword
**Type:** reference | **Section:** Operator

## Description
Elbow Keyword

Elbow Keyword

The Elbow keyword is used in these contexts:

Elbow Statement

Elbow Function


---

# Elbow Statement
**Type:** statement | **Section:** Operator

## Syntax
```
(1) Elbow
			point, [value ]

(2) Elbow
```

## Parameters
point	Pnumber or P(expr) or point label.

value	Integer expression.

1 = Above (/A)

2 = Below (/B)

## Description
Elbow Statement

Elbow Statement

## Examples
```spel
Elbow P0, Below

			Elbow pick, Above

			Elbow P(myPoint), myElbow

P1 = 0.000,  490.000, 515.000,
   90.000, -40.000, 180.000
```

## See Also
Elbow Function, Hand, J4Flag, J6Flag, Wrist

Elbow Statement Example

Elbow P0, Below

Elbow pick, Above

Elbow P(myPoint), myElbow

P1 = 0.000,  490.000,
  515.000,
   90.000,
  -40.000,
  180.000


---

# EndForces Result
**Type:** result | **Section:** Operator

## Description
Returns force and torque at end of a force guide object or force guide sequence.

## Notes
Returns force and torque at end of a force guide object or force guide sequence.

If the number of elements in a specified array variable is less than six, returns force and torque in each direction for the defined element numbers.  Also, if the number of elements in the array variable exceeds six, returns force and torque in each direction from element number 0 to 5, while making no change to element number 6 and above.

## Examples
```spel
Function EndForceTest
     Double dArray(6)
     Motor On
     FGRun Sequence1
     FGGet Sequence1.Contact01.EndForces, dArray()  ' Acquisition of EndForces
    Print dArray(FG_FX)
Fend
```

## See Also
FGGet


---

# EndPos Result
**Type:** property | **Section:** Operator

## Description
Positions when the force guide object ends.  Acquire values of X, Y, Z, U, V, and W.

## See Also
Applies To

Contact Object, Relax Object, FollowMove Object, SurfaceAlign Object, PressProbe Object, Press Object, ContactProbe Object
 Result

EndForces Result


---

# EndStatus Result
**Type:** result | **Section:** Operator

## Description
Returns end status for a force guide sequence or force guide object.

## Examples
```spel
Function EndStatusTest
     Integer iVar
     Motor On
     FGRun Sequence1
     FGGet Sequence1.Contact01.EndStatus, iVar ' Acquisition of EndStatus
     Print iVar
Fend
```

## See Also
Result

Contact object

FGGet


---

# Era Function
**Type:** reference | **Section:** Operator

## Syntax
```
Era(taskNumber)
```

## Parameters
taskNumber	Integer expression representing a task number from 0-32.

Task omission or 0 specifies the current task.

## Description
Era is used when an error occurs to determine if the error was caused by one of the robot joints and to return the number of the joint which caused the error.  If the current error was not caused by any joint, Era returns "0".

When the event "Error during Auto Mode" occurs, normal task and NoPause task in AUTO mode stop execution and end the task.

If the target task has already ended when using this function for NoEmgAbort task or background task, "Error 2261" is occurred.  Use OnErr to acquire information before the task ends.

## Examples
```spel
Function main OnErr Goto eHandler Do
    Call PickPlace Loop Exit Function
eHandler: Print "The Error code is ", Err Print "The Error Message is ", ErrMsg$(Err) errTask = Ert If errTask > 0 Then
    Print "Task number in which error occurred is ", errTask
    Print "The line where the error occurred is Line ", Erl(errTask)
    If Era(errTask) > 0 Then
      Print "Joint which caused error is ", Era(errTask)
    EndIf EndIf
Fend
```

## See Also
Error Handling

Error Codes

Erl

Err

ErrMsg$

Ert

OnErr

Trap

Era Function Example

The following example shows a simple program using the Ert function to determine which task the error occurred in along with; Erl: where the error occurred; Err: what error occurred; Era: if a joint caused the error.

Function main

  OnErr Goto eHandler

  Do

    Call PickPlace

  Loop

  Exit Function

eHandler:

  Print "The Error code is ", Err

  Print "The Error Message is ", ErrMsg$(Err)

  errTask = Ert

  If errTask > 0 Then

    Print "Task number in which error occurred is ", errTask

    Print "The line where the error occurred is Line ", Erl(errTask)

    If Era(errTask) > 0 Then

      Print "Joint which caused error is ", Era(errTask)

    EndIf

  EndIf

Fend


---

# Erf$ Function
**Type:** reference | **Section:** Operator

## Syntax
```
Erf$[(taskNumber)]
```

## Parameters
taskNumber	Integer expression representing a task number from 0-32.

Task omission or 0 specifies the current task.

## Description
Erf$ is used with OnErr.  Erf$ returns the function name in which the error occurred.  Erl returns the line number in which the error occurred.  Using Erf$ combined with Err, Ert, Erl and Era the user can determine much more about the error which occurred.

When the event "Error during Auto Mode" occurs, normal task and NoPause task in AUTO mode stop execution and end the task.

If the target task has already ended when using this function for NoEmgAbort task or background task, "Error 2261" is occurred.  Use OnErr to acquire information before the task ends.

## Examples
```spel
Function ErrHandler(errNum As Integer) 'Error handling routine Integer errTask Print "The Error code is ", errNum Print "The Error Message is ", ErrMsg$(errNum) errTask = Ert If errTask > 0 Then
    Print "Task number at which error occurred is ", errTask
    Print "Function at which error occurred is ", Erf$(errTask)
    Print "The line where the error occurred is Line ", Erl(errTask)
    If Era(errTask) > 0 Then
      Print "Joint which caused error is ", Era(errTask)
    EndIf EndIf
Fend
```

## See Also
Returns the name of the function in which the error occurred.

Era

Erl

Err

ErrMsg$

Ert

OnErr

Erf$ Function Example

The following example shows a simple program using the Ert function to determine which task the error occurred in along with; Erf$: the name of the function the error occurred in; Erl: the line number where the error occurred; Era: if a joint caused the error.

Function ErrHandler(errNum As Integer) 'Error handling routine

  Integer errTask

  Print "The Error code is ", errNum

  Print "The Error Message is ", ErrMsg$(errNum)

  errTask = Ert

  If errTask > 0 Then

    Print "Task number at which error occurred is ", errTask

    Print "Function at which error occurred is ", Erf$(errTask)

    Print "The line where the error occurred is Line ", Erl(errTask)

    If Era(errTask) > 0 Then

      Print "Joint which caused error is ", Era(errTask)

    EndIf

  EndIf

Fend


---

# Erl Function
**Type:** reference | **Section:** Operator

## Syntax
```
Erl[(taskNumber)]
```

## Parameters
taskNumber	Integer expression representing a task number from 0-32.

Task omission or 0 specifies the current task.

## Description
Erl is used with OnErr.  Erl returns the line number in which the error occurred.  Using Erl combined with Err, Ert and Era the user can determine much more about the error which occurred.

When the event "Error during Auto Mode" occurs, normal task and NoPause task in AUTO mode stop execution and end the task.

If the target task has already ended when using this function for NoEmgAbort task or background task, "Error 2261" is occurred.  Use OnErr to acquire information before the task ends.

## Examples
```spel
Function main OnErr Goto eHandler Do
    Call PickPlace Loop Exit Function
eHandler: Print "The Error code is ", Err Print "The Error Message is ", ErrMsg$(Err) errTask = Ert If errTask > 0 Then
    Print "Task number in which error occurred is ", errTask
    Print "The line where the error occurred is Line ", Erl(errTask)
    If Era(errTask) > 0 Then
      Print "Joint which caused error is ", Era(errTask)
    EndIf EndIf
Fend
```

## See Also
Error Handling

Error Codes

Era

Erf$

Err

ErrMsg$

Ert

OnErr

Erl Function Example

The following example shows a simple program using the Ert function to determine which task the error occurred in along with; Erl: where the error occurred; Err: what error occurred; Era: if an joint caused the error....

Function main

  OnErr Goto eHandler

  Do

    Call PickPlace

  Loop
 Exit Function

eHandler:

  Print "The Error code is ", Err

  Print "The Error Message is ", ErrMsg$(Err)

  errTask = Ert

  If errTask > 0 Then

    Print "Task number in which error occurred is ", errTask

    Print "The line where the error occurred is Line ", Erl(errTask)

    If Era(errTask) > 0 Then

      Print "Joint which caused error is ", Era(errTask)

    EndIf

  EndIf

Fend


---

# Err Function
**Type:** reference | **Section:** Operator

## Syntax
```
Err [ (taskNumber) ]
```

## Parameters
taskNumber	Optional. Integer expression representing a task number from 0-32.  0 specifies the current task.

## Description
Err allows the user to read the current error code.  This along with the SPEL+ Error Handling capabilities allows the user to determine which error occurred and react accordingly.  Err is used with OnErr. To get the controller error, use SysErr function.

When the event "Error during Auto Mode" occurs, normal task and NoPause task in AUTO mode stop execution and end the task.

If the target task has already ended when using this function for NoEmgAbort task or background task, "Error 2261" is occurred.  Use OnErr to acquire information before the task ends.

## Examples
```spel
Function errtest Integer i, errnum Real x OnErr Goto eHandle For i = 0 To 399
    x = CX(P(i)) Next i Exit Function ' ' '********************************************* '* Error Handler * '*********************************************
eHandle: errnum = Err ' Check if using undefined point If errnum = 78 Then
    Print "Point number P", i, " is undefined!" Else
    Print "ERROR: Error number ", errnum, " Occurred." EndIf EResume Next
Fend
```

## See Also
Error Handling

Error Codes

Era

Erf$

Erl

ErrMsg$

EResume

Ert

OnErr

Return

SysErr

Err Function Example

The following example shows a simple utility program which checks whether points P0-P399 exist. If the point does not exist, then a message is printed on the screen to let the user know this point does not exist. The program uses the CX instruction to test each point for whether or not it has been defined. When a point is not defined control is transferred to the error handler and a message is printed on the screen to tell the user which point was undefined.

Function errtest

  Integer i, errnum

  Real x

  OnErr Goto eHandle

  For i = 0 To 399

    x = CX(P(i))

  Next i

  Exit Function

  '

  '

  '*********************************************

  '* Error Handler *

  '*********************************************

eHandle:

  errnum = Err

  ' Check if using undefined point

  If errnum = 78 Then

    Print "Point number P", i, " is undefined!"

  Else

    Print "ERROR: Error number ", errnum, " Occurred."

  EndIf

  EResume Next

Fend


---

# ErrMsg$ Function
**Type:** reference | **Section:** Operator

## Syntax
```
ErrMsg$(errNumber, [ langID ])
```

## Parameters
errNumber	Integer expression containing the error number to get the message for.

langID	Optional.  Integer expression containing the language ID based on the following values.

0 - English

1 - Japanese

2 - German

3 - French

4 - Simplified Chinese

5 - Traditional Chinese

6 - Spanish

If omitted, English is used.

## Description
ErrMsg$ Function

ErrMsg$ Function

See_Also Example

Returns the error message which corresponds to the specified error number for the specified language.

## Examples
```spel
Function ErrHandler 'Error handling routine Integer errTask errTask = Ert Print "Task number at which error occurred is ", errTask If Era(errTask) Then
    Print "Joint which caused error is ", Era(errTask) EndIf Print "The Error code is ", Err(errTask) Print "The Error Message is ", ErrMsg$(Err(errTask)) Print "The line where the error occurred is Line ", Erl(errTask)
Fend
```

## See Also
Error Handling

Error Codes

Era

Erl

Err

Ert

OnErr

ErrMsg$ Function Example

The following example shows a simple program using the Ert function to determine which task the error occurred in along with; Erl: where the error occurred; Err: what error occurred; Era: if an joint caused the error....

Function ErrHandler 'Error handling routine

Integer errTask

  errTask = Ert

  Print "Task number at which error occurred is ", errTask

  If Era(errTask) Then

    Print "Joint which caused error is ", Era(errTask)

  EndIf

  Print "The Error code is ", Err(errTask)

  Print "The Error Message is ", ErrMsg$(Err(errTask))

  Print "The line where the error occurred is Line ", Erl(errTask)

Fend


---

# Error Keyword
**Type:** reference | **Section:** Operator

## Description
Error Keyword

Error Keyword

The Error keyword is used in these contexts:

Error Statement

Trap Statement


---

# Error Statement
**Type:** statement | **Section:** Operator

## Syntax
```
(1) Error taskNumber, errorNumber

(2) Error errorNumber
```

## Parameters
taskNumber	Optional.
		 Integer expression representing a task number from 0 to 32.

0 specifies
		 the current task.

errorNumber	Integer expression
		 representing a valid error number.  User error numbers range
		 is from 8000 to 8999.

## Description
Use the Error statement to generate system or user defined errors.  You can define user error labels and descriptions by using the User Error Editor in the Epson RC+ development environment.

## Examples
```spel
#define ER_VAC 8000

If Sw(vacuum) = Off Then Error ER_VAC
EndIf
```

## See Also
Error Codes

Era

Erl

Err

OnErr

Error Statement Example

#define ER_VAC 8000

If Sw(vacuum) = Off Then

Error ER_VAC

EndIf


---

# Error handling
**Type:** reference | **Section:** Operator

## Description
Error handling

Error Handling

When an error occurs in a SPEL+ function, you can cause execution to be transferred to an error handling routine for processing the error. The routine must be inside a function definition.

The table on the next page shows the program instructions that are used for error handling.

Item	Description

OnErr	Use the OnErr statement to define
		 the location of the error handling routine.

Err	Use Err to retrieve the number for
		 the current error status.

		Use this in the error handling routine to determine which error
		 has occurred.

Error	Generate a user defined error which
		 can be caught by an error handler.

Era	Use Era to retrieve the axis number
		 for which the error occurred.

		This is normally used in the error handling routine.

Erl	Use Erl to retrieve the line number
		 in which the error occurred.

		This is normally used in the error handling routine.

Ert	Use Ert to retrieve the task number
		 in which the error occurred.

		This is normally used in the error handling routine.

ErrMsg$	Use ErrMsg$ to retrieve the error
		 message associated with a specified error number.

Errb	Use Errb to retrieve the robot number
		 in which the error occurred.

		This is normally used in the error handling routine.

User Errors

You can define your own error messages by using the User Error Editor which is available from the Tools Menu. For details refer to 5.12.7 User Error Editor Command (Tools Menu).

## Examples
```spel
Function Main
    String cont$
    Integer i
    OnErr Goto Errhandler
    For i = 1 To 10
    Jump P(i)
    Next i
Exit Function

' *** Error handler ***
Errhandler:
    enum = Err
    Print "Error #", enum, " occurred"
    Print "Continue (Y or N)?"
    Line Input cont$
    Select cont$
      Case "y", "Y"
        EResume Next
      Default
        Quit All
    Send
Fend
```


---

# ErrorOn
**Type:** reference | **Section:** Operator

## Syntax
```
ErrorOn
```

## Description
ErrorOn function is used only for NoEmgAbort task (special task using NoEmgAbort at Xqt) and background task.

## Notes
Forced Flag

This program example uses Forced flag for On/Off command.

Be sure that the I/O outputs change during error, or at Emergency Stop or Safety Door Open when designing the system.

After Error Occurrence

As this program, finish the task promptly after completing the error handling.

Function main

  Xqt ErrorMonitor, NoEmgAbort

   ...

   ...

Fend

Function ErrorMonitor

Wait ErrorOn

  If 4000 < SysErr Then

Print "Motion Error = ", SysErr

    Off 10, Forced

On 12, Forced

Else

Print "Other Error = ", SysErr

Off 11, Forced

On 13, Forced

EndIf

Fend

## See Also
Returns the error status of the controller.

SysErr

Wait

Xqt

ErrorOn Function Example

The following example shows a program that monitors the controller error and switches the I/O On/Off according to the error number when error occurs.


---

# Ert Function
**Type:** reference | **Section:** Operator

## Syntax
```
Ert
```

## Description
Ert is used when an error occurs to determine in which task the error occurs.

Ert returns the number as follows:

No task with error (0), normal task (1 to 32), back ground task (65 to 80), TRAP task (257 to 267).

## Examples
```spel
Function main OnErr Goto eHandler Do
    Call PickPlace Loop Exit Function
eHandler: Print "The Error code is ", Err Print "The Error Message is ", ErrMsg$(Err) errTask = Ert If errTask > 0 Then
    Print "Task number in which error occurred is ", errTask
    Print "The line where the error occurred is Line ", Erl(errTask)
    If Era(errTask) > 0 Then
      Print "Joint which caused error is ", Era(errTask)
    EndIf EndIf
Fend
```

## See Also
Error Handling

Error Codes

Era

Erl

Err

ErrMsg$

OnErr

Trap

Ert Function Example

The following items are returned in the program example below.

In which task the error occurred (Ert function)

Where the error occurred (Erl)

On which joint the error occurred (Era)

Function main

  OnErr Goto eHandler

  Do

    Call PickPlace

  Loop

  Exit Function

eHandler:

  Print "The Error code is ", Err

  Print "The Error Message is ", ErrMsg$(Err)

  errTask = Ert

  If errTask > 0 Then

    Print "Task number in which error occurred is ", errTask

    Print "The line where the error occurred is Line ", Erl(errTask)

    If Era(errTask) > 0 Then

      Print "Joint which caused error is ", Era(errTask)

    EndIf

  EndIf

Fend


---

# Exit Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Exit { Do | For | Function }
```

## Description
The Exit statement syntax has these forms:

Statement	Description

Exit Do	Provides a way to exit a Do...Loop statement. It can be used only inside a Do...Loop statement. Exit Do transfers control to the statement following the Loop statement. When used within nested Do...Loop statements, Exit Do transfers control to the loop that is one nested level above the loop where Exit Do occurs.

Exit For	Provides a way to exit a For loop. It can be used only in a For...Next loop. Exit For transfers control to the statement following the Next statement. When used within nested For loops, Exit For transfers control to the loop that is one nested level above the loop where Exit For occurs.

Exit Function	Immediately exits the Function procedure in which it appears. Execution continues with the statement following the statement that called the Function.

## Examples
```spel
For i = 1 To 10
		  If Sw(1) = On Then

			    Exit For

		  EndIf
		  Jump P(i)
		Next i
```

## See Also
Do...Loop

For...Next

Function...Fend

Exit Statement Example

For i = 1 To 10

		  If Sw(1) = On Then

Exit For

EndIf

		  Jump P(i)

		Next i


---

# FGGet Statement
**Type:** statement | **Section:** Operator

## Description
Acquires a result of a force guide sequence or force guide object.

## Notes
Acquires a specified result.

If a result other than EndStatus is specified while the target force guide sequence or force guide object has not been executed by FGRun, an error will occur.

## Examples
```spel
Function FGGetTest
     Integer iResult
     Motor On
     FGRun Sequence1                    ' Execution of a force guide sequence
     FGGet Sequence1.EndStatus, iResult ' Acquisition of results
     Print iResult
Fend
```

## See Also
FGRun


---

# FGIOPreProcEnabled Property
**Type:** property | **Section:** Operator

## Description
This property sets I/O operations when the force guide object starts.

I/O operations are defined by IOPreprocOutputBit Property and IOPreprocOutputStatus Property.  Use this property when you want to operate the hands or peripherals before the force guide object execution.

Values

True Execute I/O operation at the start.

False I/O operation at the start is not executed.

Default:  False

See Also: IOPreProcEnabled Property

IOCheckEnabled Property

## See Also
Applies To

Sequence, All Objects


---

# FGRun Statement
**Type:** statement | **Section:** Operator

## Description
FGRun Statement

Force Guide

FGRun Statement

## Notes
Executes a specified force guide sequence.  The force guide sequence starts from the position where the FGRun statement was executed.  Execute after moving to the assumed start position by the Go statement, Move statement, or other motion commands.

When the specified force guide sequence ends, the program proceeds to the next statement.

To acquire the results of sequences executed by FGRun, use FGGet.

When path motion is enabled by the CP parameter or CP statement, the program waits until the robot stops and then executes a force guide sequence.

When any of the following conditions is fulfilled at the time of execution start, an error occurs.

- The robot specified in the program differs from the robot specified by the RobotNumber property.  Specify the correct robot by the Robot statement.

- The robot type specified in the program differs from the robot type specified by the RobotType property. Specify the correct robot by the Robot statement.

- The tool number specified in the program differs from the tool number specified by the RobotTool property. Specify the correct tool number by the Tool statement.

- Motor is in OFF state.  Switch to ON state by the Motor statement.

- Force control function is currently being executed.  Stop force control by the FCEnd statement.

- Conveyor tracking is currently being executed.  Stop conveyor tracking by the Cnv_AbortTrack statement.

- Currently in the torque control mode.  Disable the torque control mode by the TC statement.

FGRun, when executed, automatically overwrites the following properties; therefore, it cannot be used together with the following properties:

FM object

- AvgForceClear property

- PeakForceClear property

## Examples
```spel
Function FGRunTest
     Integer iResult
     Motor On
     FGRun Sequence1                    ' Execution of a force guide sequence
     FGGet Sequence1.EndStatus, iResult ' Acquisition of results
     Print iResult
Fend
```

## See Also
FGGet


---

# FG_AbortSeqOnFail Property
**Type:** property | **Section:** Operator

## Description
This property sets operations when force guide object fails.

When specifying True, the program ends force guide sequence and proceeds to the next SPEL statement if force guide object fails.

When specifying False, the program proceeds to the next force guide object without ending the force guide sequence if the force guide object fails.

Use this property when you want to continue the force guide sequence (e.g. the recovery processes are included in the force guide sequence when the force guide object fails.)

Values

True Abort the force guide sequence when the force guide object fails.

False Start the next force guide sequence when the force guide object fails.

Default:  True

See Also: AbortSeqOnFail Property

Enabled Property

## See Also
Applies To

Contact Object, Follow Object, Relax Object


---

# FG_Enabled Property
**Type:** property | **Section:** Operator

## Description
This property sets whether to enable force guide objects.

When specifying True, the force guide object is executed.

When specifying False, execute the next force guide object without executing the force guide object.

Use this property when you want to save the force guide sequence temporary or try with different parameters by copying the force guide object during the force guide sequence creation.

Values

True Enable a force guide object.

False Disable a force guide object.

Default:  True

## See Also
Applies To

All Objects

AbortSeqOnFail Property


---

# FG_IO_CheckEnabled Property
**Type:** property | **Section:** Operator

## Description
This property sets the end conditions of the force guide object related to I/O.

Values

True Enable the end conditions related to I/O.

False Disable the end conditions related to I/O.

Default:  False

See Also: IOCheckEnabled Property

IOCheckInputBit Property

## See Also
Applies To

Sequence, All Objects


---

# FG_IO_CheckInputBit Property
**Type:** property | **Section:** Operator

## Description
This property sets the bit of determination target of the end conditions related to I/O.

It is used when IOCheckEnabled is True.

Values

Minimum value 0

Maximum value 7167

Default:  0

See Also: IOCheckInputBit Property

IOCheckEnabled Property

## See Also
Applies To

Relax Object, FollowMove Object, Press Object


---

# FG_Name Property
**Type:** property | **Section:** Operator

## Description
This property sets a particular name that is assigned to force guide sequences.

You cannot create the force guide sequence with the same name.

You can change the name.  Set up 32 characters at the maximum.  Please use alphanumeric characters and underscore [ _ ].  Note: The initial character cannot be a numeric character..

## See Also
Applies To

Sequences and Objects


---

# Find Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Find [condition]
```

## Parameters
condition	Input status specified as a trigger

[Event] comparative operator ( =, <>, >=, >, <, <=) [Integer expression]

The following functions and variables can be used in the Event:

Functions :  Sw, In, InW, Oport, Out, OutW, MemSw, MemIn, MemInW, Ctr, GetRobotInsideBox, GetRobotInsidePlane, AIO_In, AIO_InW, AIO_Out, AIO_OutW, Hand_On, Hand_Off

Variables :   Byte, Int32, Integer, Long, Short, UByte, UInt32, UShort, global preserve variable, Global variable, module variable

In addition, using the following operators you can specify multiple event conditions.

Operator :   And, Or, Xor

## Description
Find statement can be used by itself or as a modifier of a motion command.

The Find condition must include at least one of the functions above.

When variables are included in the Find condition, their values are computed when setting the Find condition. No use of variable is recommended. Otherwise, the condition may be an unintended condition. Multiple Find statements are permitted. The most recent Find condition remains current.

When parameters are omitted, the current Find definition is displayed.

## Notes
Find setting at Main Power On

At power on, the find condition is:

Find Sw(0)=On ' Input bit 0 is on.

Use of PosFond Function to Verify Find

Use PosFound function to verify if the Find condition has been satisfied after executing a motion command using Find modifier.

Use Variables in Event Condition Expression

Available variables are Integer type (Byte, Int32, Integer, Long, Short, UByte, UInt32, UShort)

Array variables are not available

Local variables are not available

If a variable value cannot satisfy the event condition for more than 0.01 seconds, the system cannot retrieve the change in variables.

Up to 64 can wait for variables in one system (including the ones used in the event condition expressions such as Wait). If it is over 64, an error occurs during the project build.

If you try to transfer a variable waiting for variables as a reference with Byref, an error occurs.

When a variable is included in the right side member of the event condition expression, the value is calculated when starting the motion command. We recommend not using variables in an integer expression to avoid making unintended conditions.

## Examples
```spel
Find Sw(5) = On
```

```spel
Find Sw(5) = On And Sw(6) = Off
```

```spel
Find Sw(5) = On
Go P10 Find
If PosFound Then Go FindPos
Else Print "Cannot find the sensor signal."
EndIf
```

## See Also
FindPos

Go

Jump

PosFound

Find Statement Example

Find Sw(5) = On

Go P10 Find

If PosFound Then

  Go FindPos

Else

  Print "Cannot find the sensor signal."

EndIf


---

# FindPos Function
**Type:** reference | **Section:** Operator

## Syntax
```
FindPos
```

## Description
FindPos Function

FindPos Function

See_Also Example

Returns a robot point stored by Find during a motion command.

## Examples
```spel
Find Sw(5) = On
		Go P10 Find
		If PosFound Then
		  Go FindPos

		Else
		  Print "Cannot find the sensor signal."
		EndIf
```

## See Also
Find

Go

Jump

PosFound

FindPos Function Example

Find Sw(5) = On

		Go P10 Find

		If PosFound Then

		  Go FindPos

Else

		  Print "Cannot find the sensor signal."

		EndIf


---

# Fine Function
**Type:** function | **Section:** Operator

## Syntax
```
Fine(joint)
```

## Parameters
joint	Integer expression representing the joint number for which to retrieve the Fine setting.

The additional S axis is 8 and T axis is 9.

## Description
Fine Function

Fine Function

See_Also Example

Returns Fine setting for a specified joint.

## Examples
```spel
Function finetst
		  Integer a
		  a = Fine(1)
		Fend
```

## See Also
Fine Statement

Fine Function Example

This example uses the Fine function in a program:

Function finetst

		  Integer a

		  a = Fine(1)

		Fend


---

# Fine Keyword
**Type:** reference | **Section:** Operator

## Description
Fine Keyword

Fine Keyword

The Fine keyword is used in these contexts:

Fine Statement

Fine Function


---

# Fine Statement
**Type:** statement | **Section:** Operator

## Syntax
```
(1) Fine axis1, axis2, axis3, axis4, [axis5 , axis6], [axis7], [axis8, axis9]

(2) Fine
```

## Parameters
axis1	Integer expression ranging from (0-65535) which represents the allowable positioning error for the 1st joint.

axis2	Integer expression ranging from (0-65535) which represents the allowable positioning error for the 2nd joint.

axis3	Integer expression ranging from (0-65535) which represents the allowable positioning error for the 3rd joint.

axis4	Integer expression ranging from (0-65535) which represents the allowable positioning error for the 4th joint.

axis5	Optional.  Integer expression ranging from (0-65535) which represents the allowable positioning error for the 5th joint.  Only for the 6-axis robot (including N series).

axis6	Optional.  Integer expression ranging from (0-65535) which represents the allowable positioning error for the 6th joint.  Only for the 6-axis robot (including N series).

axis7	Optional.  Integer expression ranging from (0-65535) which represents the allowable positioning error for the 7th joint. Only for the Joint type 7-axis robot.

axis8	Optional.  Integer expression ranging from (0-65535) which represents the allowable positioning error for the 8th joint. Only for the additional S axis.

axis9	Optional.  Integer expression ranging from (0-65535) which represents the allowable positioning error for the 9th joint. Only for the additional T axis.

* For C8, C12 series Manipulators, the allowable positioning error is from 0 to 131070.

## Description
Fine specifies, for each joint, the allowable positioning error for detecting completion of any given move.

This positioning completion check begins after the CPU has completed sending the target position pulse to the servo system.  Due to servo delay, the robot will not yet have reached the target position.  This check continues to be executed every few milliseconds until each joint has arrived within the specified range setting. Positioning is considered complete when all axes have arrived within the specified ranges.  Once positioning is complete program control is passed to the next statement, however, servo system keeps the control of the robot target position.

When relatively large ranges are used with the Fine instruction, the positioning will be confirmed relatively early in the move, and executes the next statement.

The default Fine settings depend on the robot type.  Refer to your robot manual for details.

## Notes
Cycle Times and the Fine Instruction

The Fine value does not affect the acceleration or deceleration control of the manipulator arm.  However, smaller Fine values can cause the system to run slower because it may take the servo system extra time (a few milliseconds) to get within the acceptable position range.  Once the arm is located within the acceptable position range (defined by the Fine instruction), the CPU executes the next user instruction. (Keep in mind that all activated axes must be in position before the CPU can execute the next user instruction.)

Initialization of Fine (by Motor On, SLock, SFree)

When any of the the following commands is used, the Fine value will be initialized to the default: SLock, SFree, Motor instructions.

Make sure that you reset Fine values after one of the above commands is executed.

Potential Errors

If Fine positioning is not completed within about 2 seconds error 4024 will occur.  This error normally means the servo system balance needs to be adjusted. (Call your distributor for assistance)

## Examples
```spel
Function finetest Fine 5, 5, 5, 5           'reduce precision to +/- 5 Pulse Go P1 Go P2
Fend
```

```spel
> Fine 10, 10, 10, 10
>
> Fine
10, 10, 10, 10
```

## See Also
Robot motion commands

Accel, AccelR, AccelS, Arc, Fine Function, Go, Jump, Move, Speed, SpeedR, SpeedS, Pulse

Fine Statement Example

The examples below show the Fine statement used in a program function, and used from the command window.

Function finetest

  Fine 5, 5, 5, 5           'reduce precision to +/- 5 Pulse

  Go P1

  Go P2

Fend

> Fine 10, 10, 10, 10

>

> Fine

10, 10, 10, 10


---

# Fix Function
**Type:** reference | **Section:** Operator

## Syntax
```
Fix(number)
```

## Parameters
number	Real expression containing number to fix.

## Description
Fix Function

Fix Function

See_Also Example

Returns the integer portion of a real number.

## Examples
```spel
>print
				Fix
			(1.123)
```

```spel
1
```

```spel
>
```

## See Also
Int

Fix Function Example

>print
				Fix
			(1.123)

1

>


---

# For...Next
**Type:** reference | **Section:** Operator

## Syntax
```
For var = initValue To finalValue [Step increment ]

statements

Next [var]
```

## Parameters
var	The counting
		 variable used with the For...Next loop. This variable is normally
		 defined as an integer but may also be defined as a Real variable.

initValue	The initial
		 value for the counter var
		 .

finalValue	The final
		 value of the counter var
		 . Once this value is met, the
		 For...Next loop is complete and execution continues starting with
		 the statement following the Next instruction.

increment	An optional
		 parameter which defines the counting increment for each time the
		 Next statement is executed within the For...Next loop.  This
		 variable may be positive or negative.  However, if the value
		 is negative, the initial value of the variable must be larger
		 than the final value of the variable.  If the increment value
		 is left out the system automatically increments by 1.

statements	Any valid
		 SPEL+ statements can be inserted inside the For...Next loop.

## Description
For...Next executes a set of statements within a loop a specified number of times. The beginning of the loop is the For statement. The end of the loop is the Next statement. A variable is used to count the number of times the statements inside the loop are executed.

The first numeric expression (initValue) is the initial value of the counter. This value may be positive or negative as long as the finalValue variable and Step increment correspond correctly.

The second numeric expression (finalValue) is the final value of the counter. This is the value which once reached causes the For...Next loop to terminate and control of the program is passed on to the next instruction following the Next instruction.

Program statements after the For statement are executed until a Next instruction is reached. The counter variable (var) is then incremented by the Step value defined by the increment parameter. If the Step option is not used, the counter is incremented by 1 (one).

The counter variable (var) is then compared with the final value. If the counter is less than or equal to the final value, the statements following the For instruction are executed again. If the counter variable is greater than the final value, execution branches outside of the For...Next loop and continues with the instruction immediately following the Next instruction.

Note

Negative Step Values:

If the value of the Step increment (increment) is negative, the counter variable (var) is decremented (decreased) each time through the loop and the initial value must be greater than the final value for the loop to work.

Variable Following Next is Not Required:

The variable name following the Next instruction may be omitted. However, for programs that contain nested For...Next loops, it is recommended to include the variable name following the Next instruction to aid in quickly identifying loops.

When a variable comes out of the loop, the value is not a final value.

Function forsample

  Integer i

  For i = 0 To 3

  Next

  Print i ' Displays 4

Fend

When you exit the loop from the nested structure without using Exit For

Error 2020 will occur when you repeatedly execute the program which exits the loop by the command other than the Exit For command (such as GoSub statement, Goto statement, and Call statement.)
  Be sure to use Exit For command to exit the loop.

Avoid endless execution of empty Loop Statements and similar to them, use them with the Wait command instead

Do not use empty For...Next statements and similar commands to avoid effect on the system. The Controllers are detecting endless loop tasks. If the controller determines that the system will be affected, it will stop the program with error 2556 (An excessive loop was detected). When performing operations that require a loop or waiting for I/O, execute a Wait command (Wait 0.1) and more within the loop to avoid occupying the CPU.

## Examples
```spel
Function forsample Integer i For i = 0 To 3 Next Print i ' Displays 4
Fend
```

```spel
Function fornext Integer counter For counter= 1 to 10
    Go Pctr Next counter For counter= 10 to 1 Step -1
    Go Pctr Next counter
Fend
```

## See Also
Do...Loop

For....Next Example

Function fornext

  Integer counter

  For counter= 1 to 10

    Go Pctr

  Next counter

  For counter= 10 to 1 Step -1

    Go Pctr

  Next counter

Fend


---

# ForceCondOK Result
**Type:** result | **Section:** Operator

## Description
It is whether to satisfy the end conditions related to force.


---

# Function and Variable Names
**Type:** reference | **Section:** Operator

## Description
Function and Variable Names

Function and Variable Names (Naming restriction)

The function name can include up to 64 characters. The variable name can include up to 32 alphanumeric, Japanese, or underscore characters. Characters can be upper case or lower case.

The following names are valid:

Function main

Real real_var

Integer IntVar

Function and variable names cannot begin with an underscore.

SPEL+ keywords cannot be used as function or variable names. (Example: Go, On)

String variables must have an additional dollar sign ('$') suffix. An example is shown below.

Function Test

    String modname$

    Print "Enter model name:"

    Line Input modname$

    Print "model is ", modname$

Fend

Restrictions for naming in SPEL+ language

Characters
	 can be alphanumeric, Japanese, or underscore character.

Use
	 alphabets for the first letter.

Characters
	 can be upper case or lower case.

No
	 keywords can be used.

Maximum
	 limits of names are as follows. (For one -byte character)

Name	Max.
		 limit

Point label	32

I/O
		 label	32

User
		 error label	32

Function
		 name	64

Variable
		 name	32

Line
		 label	32

## Examples
```spel
Function main
Real real_var
Integer IntVar
```

```spel
Function Test
    String modname$
    Print "Enter model name:"
    Line Input modname$
    Print "model is ", modname$
Fend
```


---

# Function...Fend Command
**Type:** reference | **Section:** Operator

## Syntax
```
Function
			funcName [(argList)]
			[As
			 type]

statements

Fend
```

## Parameters
funcName	The name which is given to the specific group of statements bound between the Function and Fend instructions. The function name must contain alphanumeric characters and may be up to 64 characters in length. Underscores are also allowed.

argList	Optional. List of variables representing arguments that are passed to the Function procedure when it is called. Multiple variables are separated by commas.

The arglist argument has the following syntax:

[ {ByRef | ByVal} ] varName [( )] As
			type

ByRef	Optional.  Specify ByRef when you refer to the variable to be seen by the calling function.  In this case, the argument change in a function can be reflected to the variable of the calling side.

ByVal	Optional. Specify ByVal when you do not want any changes in the value of the variable to be seen by the calling function.  This is the default.

varName	Required. Name of the variable representing the argument; follows standard variable naming conventions.  If you use an array variable as argument, you should specify ByRef.

type	Required. You must declare the type of argument.

## Description
The Function statement indicates the beginning of a group of SPEL+ statements. To indicate where a function
			ends we use the Fend statement. All statements located between the Function and Fend statements are considered part of the function.

The Function...Fend combination of statements could be thought of as a container where all the statements located between the Function and Fend statements belong to that function. Multiple functions may exist in one program file.

## Examples
```spel
Function main
		  Xqt 2, task2 'Execute task2 in background
		  Xqt 3, task3 'Execute task3 in background
		  '..more statements here

Fend
```

```spel
Function task2
		  Do
		    On 1
		    On 2
		    Off 1
		    Off 2
		  Loop

			Fend
```

```spel
Function task3
		  Do
		    On 10
		    Wait 1
		    Off 10
		  Loop

			Fend
```

## See Also
Function Naming Conventions

Simplest Application

Call

Halt

Quit

Return

Xqt

Function...Fend Example

The following example shows 3 functions which are within a single file. The functions called task2 and task3 are executed as background tasks while the main task called main executes in the foreground.

Function main

		  Xqt 2, task2 'Execute task2 in background

		  Xqt 3, task3 'Execute task3 in background

		  '..more statements here

Fend

Function task2

		  Do

		    On 1

		    On 2

		    Off 1

		    Off 2

		  Loop

Fend

Function task3

		  Do

		    On 10

		    Wait 1

		    Off 10

		  Loop

Fend


---

# GetRobotInsideBox Function
**Type:** reference | **Section:** Operator

## Syntax
```
GetRobotInsideBox(AreaNum)
```

## Parameters
AreaNum	Integer value (1 - 15) representing the approach check area you want to return the status for.

## Description
GetRobotInsideBox Function

GetRobotInsideBox Function

## Examples
```spel
Function WaitNoBox
		Wait GetRobotInsideBox(1) = 0
```

```spel
Function WaitInBoxRobot2
		Wait GetRobotInsideBox(1) = &H2
```

```spel
Function Main
		  Motor On
		  Power High
		  Speed 30; Accel 30,30
```

```spel
Go P1 !D0; Wait GetRobotInsideBox(1) = 1; On 1!
```

```spel
Fend
```

## See Also
Returns a robot which is in the approach check area.

Box

InsideBox

GetRobotInsideBox Function Example

The following program uses the GetRobotInsideBox function.

Wait for the status that no robots are in the approach check area.

Function WaitNoBox

		Wait GetRobotInsideBox(1) = 0

Wait for the status that Robot 2 is only one in the approach check area.

Function WaitInBoxRobot2

		Wait GetRobotInsideBox(1) = &H2

The following program uses the GetRobotInsideBox function in the parallel processing of the motion command.  When a robot is in the specific approach check area while it is running, it turns ON the I/O.  One robot is connected to the controller in this case.

Function Main

		  Motor On

		  Power High

		  Speed 30; Accel 30,30

  Go P1 !D0; Wait GetRobotInsideBox(1) = 1; On 1!

Fend

Note: D0 must be described.


---

# GetRobotInsidePlane Function
**Type:** reference | **Section:** Operator

## Syntax
```
GetRobotInsidePlane(PlaneNum)
```

## Parameters
PlaneNum	Integer value (1 - 15) representing the approach check plane you want to return the status for.

## Description
GetRobotInsidePlane Function

GetRobotInsidePlane Function

## Examples
```spel
Function WaitNoPlane
		Wait GetRobotInsidePlane(1) = 0
```

```spel
Function WaitInPlaneRobot2
		Wait GetRobotInsidePlane(1) = &H2
```

```spel
Function Main
		  Motor On
		  Power High
		  Speed 30; Accel 30,30
```

```spel
Go P1 !D0; Wait GetRobotInsidePlane(1) = 1; On 1!
```

```spel
Fend
```

## See Also
Returns a robot which is in the approach check plane.

Plane

InsidePlane

GetRobotInsidePlane Function Example

The following program uses the GetRobotInsidePlane function.

Wait for the status that no robots are in the approach check plane.

Function WaitNoPlane

		Wait GetRobotInsidePlane(1) = 0

Wait for the status that Robot 2 is only one in the approach check plane.

Function WaitInPlaneRobot2

		Wait GetRobotInsidePlane(1) = &H2

The following program uses the GetRobotInsidePlane function in the parallel processing of the motion command.  When a robot is in the specific approach check plane while it is running, it turns ON the I/O.  One robot is connected to the controller in this case.

Function Main

		  Motor On

		  Power High

		  Speed 30; Accel 30,30

  Go P1 !D0; Wait GetRobotInsidePlane(1) = 1; On 1!

Fend

Note: D0 must be described.


---

# Global Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Global [ Preserve ] dataType varName [( subscripts )] [, varName [( subscripts )] , ...]
```

## Parameters
Preserve	Optional.  If Preserve is specified, then the variable retains it's values.  The values are cleared by project changes.

dataType	Data type including Boolean, Int32, Integer, Long, Real, Short, Double, Byte, String, UByte, UInt32, or UShort.

varName	Variable name. Names may be up to 32 characters in length.

subscripts	Optional.  Dimensions of an array variable; up to 3 dimensions may be declared.  The subscripts syntax is as follows

(ubound1, [ubound2], [ubound3])

ubound1, ubound2, ubound3 each specify the maximum upper bound for the associated dimension.

The elements in each dimension of an array are numbered from 0 to the upper bound value.

The total available number of array elements for global variables is 10000 for strings and 100000 for all other types.

The total available number of array elements for global preserve variables is 400 for strings and 4000 for all other types.

To calculate the total elements used in an array, use the following formula.  (If a dimension is not used, substitute 0 for the ubound value.)

total elements = (ubound1 + 1) * (ubound2 + 1) * (ubound3 + 1)

## Description
Global variables are variables which can be used in more than 1 file within the same project. They are cleared whenever a function is started from the Run window or Operator window unless they are declared with the Preserve option.

Global variables can used in the command window after the project build is complete.

When declared in Preserve option, the variable retains the value at turning off the controller.

Global Preserve variables can also be used with the RC+ Connectivity option.

It is recommended that global variable names begin with a "g_" prefix to make it easy to recognize globals in a program. For example:

Global Long g_PartsCount

## Examples
```spel
Global Long g_PartsCount
```

```spel
Global Integer g_Status
Global Real g_MaxValue

Function Main g_Status = 10 g_MaxValue = 1.1 . .
Fend
```

```spel
Function Test Print "status1 = , g_Status Print "MaxValue = , g_MaxValue . .
Fend
```

## See Also
Data Types Overview

Variable Declarations

Variable Naming Conventions

Boolean

Byte

Double

Int32

Integer

Long

Real

Short

String

UByte

UInt32

UShort

Global Statement Example

The following example shows 2 separate program files. The first program file defines some global variables and initializes them. The second file then also uses these global variables.

FILE1 (Main.prg)

Global Integer g_Status

Global Real g_MaxValue

Function Main

  g_Status = 10

  g_MaxValue = 1.1

  .

  .

Fend

FILE2 (Test.prg)

Function Test

  Print "status1 = , g_Status

  Print "MaxValue = , g_MaxValue

  .

  .

Fend


---

# Go Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Go destination [CP] [LJM [orientationFlag]] [searchExpr] [!...!] [SYNC]
```

## Parameters
destination	The target
		 destination of the motion using a point
		 expression.

CP	Optional.
		 Specifies continuous path motion.

LJM	Optional.
		 Convert the target destination using LJM function.

orientationFlag	Optional.
		 Specifies a parameter that selects an orientation flag for LJM
		 function.

searchExpr	Optional. A Till or Find expression.

Till
		 | Find

Till
		 Sw(expr)
		 = {On | Off}

Find
		 Sw(expr)
		 = {On | Off}

!...!	Optional.
		 Parallel Processing statements
		 can be added to execute I/O and other commands during motion.

SYNC	Reserves a
		 motion command. The robot will not move until SyncRobots is executed.

## Description
Go simultaneously moves all joints of the robot arm using point to point motion.  The destination for the Go instruction can be defined in a variety of ways:
 - Using a specific point to move to. For

## Notes
Difference between Go and Move

The Move instruction and the Go instruction each cause the robot arm to move. However, the primary difference between the 2 instructions is that the Go instruction causes point to point motion where as the Move instruction causes the arm to move in a straight line. The Go instruction is used when the user is primarily concerned with the orientation of the arm when it arrives on point. The Move instruction is used when it is important to control the path of the robot arm while it is moving.

Difference between Go and Jump

The Jump instruction and the Go instruction each cause the robot arm to move in a point to point type fashion. However, the JUMP instruction has 1 additional feature. Jump causes the robot end effector to first move up to the LimZ value, then in a horizontal direction until it is above the target point, and then finally down to the target point. This allows Jump to be used to guarantee object avoidance and more importantly to improve cycle times for pick and place motions.

Proper Speed and Acceleration Instructions with Go

The Speed and Accel instructions are used to specify the speed and acceleration of the manipulator during motion caused by the Go instruction. Pay close attention to the fact that the Speed and Accel instructions apply to point to point type motion (like that for the Go instruction) while linear and circular interpolation motion uses the SpeedS and AccelS instructions.

Using Go with the Optional Till Modifier

The optional Till modifier allows the user to specify a condition to cause the robot to decelerate to a stop at an intermediate position prior to completing the motion caused by the Go instruction. If the Till condition is not satisfied, the robot travels to the target position. The Go with Till modifier can be used in 2 ways as described below:

(1) Go with Till Modifier:

Checks if the current Till condition becomes satisfied. If satisfied, this command completes by decelerating and stopping the robot at an intermediate position prior to completing the motion caused by the Go instruction.

(2) Go with Till Modifier, Sw(Input bit number) Modifier, and Input Condition:

This version of the Go with Till modifier allows the user to specify the Till condition on the same line with the Go instruction rather than using the current definition previously defined for Till. The condition specified is simply a check against one of the H/W inputs. This is accomplished through using the Sw instruction. The user can check if the input is On or Off and cause the arm to stop based on the condition specified. This feature works almost like an interrupt where the motion is interrupted (stopped) once the Input condition is met. If the input condition is never met during the robot motion then the arm successfully arrives on the point specified by destination.

Using Go with the Optional Find Modifier

The optional Find modifier allows the user to specify a condition to cause the robot to record a position during the motion caused by the Go instruction. The Go with Find modifier can be used in 2 ways as described below:

(1) Go with Find Modifier:

Checks if the current Find condition becomes satisfied. If satisfied, the current position is stored in the special point FindPos.

(2) Go with Find Modifier, Sw(Input bit number) Modifier, and Input Condition:

This version of the Go with Find modifier allows the user to specify the Find condition on the same line with the Go instruction rather than using the current definition previously defined for Find. The condition specified is simply a check against one of the H/W inputs. This is accomplished through using the Sw instruction. The user can check if the input is On or Off and cause the current position to be stored in the special point FindPos.

Go Instruction Always Decelerates to a Stop:

The Go instruction always causes the arm to decelerate to a stop prior to reaching the final destination of the move.

Potential

## Examples
```spel
Go LJM (P1, Here,1)
```

```spel
Go P1 LJM 1
```

```spel
Go P1 LJM
```

```spel
Function sample Integer i Home Go P0 Go P1 For i = 1 to 10
    Go P(i) Next i Go P2 Till Sw(2) = On If Sw(2) = On Then
    Print "Input #2 came on during the move and"
    Print "the robot stopped prior to arriving on"
    Print "point P2." Else
    Print "The move to P2 completed successfully."
    Print "Input #2 never came on during the move." EndIf
Fend
```

```spel
>Go Here +X(50) ' Move only in the X direction 50 mm from
' current position
>Go P1 ' Simple example to move to point P1
>Go P1 :U(30) ' Move to P1 but use +30 as the position for
' the U joint to move to
>Go P1 /L ' Move to P1 but make sure the arm ends up
' in lefty position
>Go XY(50, 450, 0, 30) ' Move to position X=50, Y=450, Z=0, U=30
```

```spel
Till Sw(1) = Off And Sw(2) = On ' Specifies Till conditions for
' inputs 1 & 2
Go P1 Till ' Stop if current Till condition
' defined on previous line is met
Go P2 Till Sw(2) = On ' Stop if Input Bit 2 is On
Go P3 Till ' Stop if current Till condition
' defined on previous line is met
```

## See Also
Robot motion commands

!...! Parallel Processing

Accel

Find

Jump

Move

Pass

Point Assignment

Pulse

Speed

Sw

Till

Go Statement Example

The example shown below shows a simple point to point move between points P0 and P10. Later in the program the arm moves in a straight line toward point P2 until H/W input #2 turns on. If H/W input #2 turns On during the Go, then the arm decelerates to a stop prior to arriving on point P2 and the next program instruction is executed.

Function sample

  Integer i

  Home

  Go P0

  Go P1

  For i = 1 to 10

    Go P(i)

  Next i

  Go P2 Till Sw(2) = On

  If Sw(2) = On Then

    Print "Input #2 came on during the move and"

    Print "the robot stopped prior to arriving on"

    Print "point P2."

  Else

    Print "The move to P2 completed successfully."

    Print "Input #2 never came on during the move."

  EndIf

Fend

Some syntax examples from the command window are shown below:

>Go Here +X(50) ' Move only in the X direction 50 mm from

' current position

>Go P1 ' Simple example to move to point P1

>Go P1 :U(30) ' Move to P1 but use +30 as the position for

' the U joint to move to

>Go P1 /L ' Move to P1 but make sure the arm ends up

' in lefty position

>Go XY(50, 450, 0, 30) ' Move to position X=50, Y=450, Z=0, U=30

[Another Coding


---

# GoTo Statement
**Type:** reference | **Section:** Operator

## Syntax
```
GoTo { label }
```

## Parameters
label	Program execution will jump to the line on which the label resides.  The label can be up to 32 characters. However, the first character must be an alphabetic character (not numeric).

## Description
The GoTo instruction causes program control to branch to the user specified statement label.
  The program then executes the statement on that line and continues execution from that line on. GoTo is most commonly used for jumping to an exit label because of an error.

## Notes
Using Too Many GoTo's

Please be careful with the GoTo instruction since using too many GoTo's in a program can make the program difficult to understand.  The general rule is to try to use as few GoTo instructions as possible.  Some GoTo's are almost always necessary.
  However, jumping all over the source code through using too many GoTo statements is an easy way to cause problems.

## Examples
```spel
Function main

If Sw(1) = Off Then

			    GoTo mainAbort
		  EndIf
		  Print "Input 1 was On, continuing cycle"
		  .
		  .
		Exit Function

mainAbort:
		  Print "Input 1 was OFF, cycle aborted!"
		Fend
```

## See Also
Label Definitions

GoSub

OnErr

GoTo Statement Example

The following example shows a simple function which uses a GoTo instruction to branch to a line label.

Function main

If Sw(1) = Off Then

GoTo mainAbort

		  EndIf

		  Print "Input 1 was On, continuing cycle"

		  .

		  .

		Exit Function

mainAbort:

		  Print "Input 1 was OFF, cycle aborted!"

		Fend


---

# Gosub Command
**Type:** reference | **Section:** Operator

## Syntax
```
GoSub {label}

{label
			:}

statements

Return
```

## Parameters
label	When the user specifies a label (rather than a line number) the program execution will jump to the line on which this label resides. The label can be up to 32 characters in length. However, the first character must be an alphabet character (not numeric).

## Description
The GoSub instruction causes program control to branch to the user specified statement label.
  The program then executes the statement on that line and continues execution through subsequent line numbers until a Return instruction is encountered. The Return instruction then causes program control to transfer back to the line which immediately follows the line which initiated the GoSub in the first place. (i.e. the GoSub instruction causes the execution of a subroutine and then execution returns to the statement following the GoSub instruction.) Be sure to always end each subroutine with Return. Doing so directs program execution to return to the line following the GoSub instruction.

Potential Errors

Branching to Non-Existent Statement

If the GoSub instruction attempts to branch control to a non-existent label then an error 3108 will be issued.

Return Found Without GoSub

A Return instruction is used to "return" from a subroutine back to the original program which issued the GoSub instruction. If a Return instruction is encountered without a GoSub having first been issued then an Error 2383 will occur. A stand alone Return instruction has no meaning because the system doesn't know where to Return to.

## Examples
```spel
Function main
		  Integer var1, var2

GoSub checkio 'GoSub using Label
		  On 1
		  On 2
		  Exit Function

checkio: 'Subroutine starts here
		  var1 = In(0)
		  var2 = In(1)
		  If var1 = 1 And var2 = 1 Then
		    On 1
		  Else
		    Off 1
		  EndIf

			  Return 'Subroutine ends here
		Fend
```

## See Also
Label Definitions

GoTo

OnErr

Return

GoSub Statement Example

The following example shows a simple function which uses a GoSub instruction to branch to a label and execute some I/O instructions then return.

Function main

		  Integer var1, var2

GoSub checkio 'GoSub using Label

		  On 1

		  On 2

		  Exit Function

checkio: 'Subroutine starts here

		  var1 = In(0)

		  var2 = In(1)

		  If var1 = 1 And var2 = 1 Then

		    On 1

		  Else

		    Off 1

		  EndIf

Return 'Subroutine ends here

		Fend


---

# Halt Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Halt taskIdentifier
```

## Parameters
taskIdentifier	Task name or integer expression representing
		 the task number.

A task name is the function name used
		 in an Xqt statement or a function started from the Run window
		 or Operator window.  If an
		 integer expression is used, the range is from 1 to 16 for normal
		 tasks and from 257-261 for trap tasks.

## Description
Halt temporarily suspends the task being executed as specified by the task name or number.

To continue the task where it was left off, use Resume. To stop execution of the task completely, use Quit. To display the task status, click the TASK Manager Icon on the Epson RC+ Toolbar to run the TASK manager.

Halt also pauses the task when the specified task is NoPause task or NoEmgAbort task (special task using NoPause or NoEmgAbort at Xqt), trap tasks, or the background tasks. .However, stopping these tasks needs enough consideration. Normally, Halt is not recommended for the special task.

## Examples
```spel
Function main Xqt flicker 'Execute flicker function Do
    Wait 3 'Execute task 2 for 3 seconds
    Halt flicker

    Wait 3 'Halt task 2 for 3 seconds
    Resume flicker Loop
Fend
```

```spel
Function flicker Do
    On 1
    Wait 0.2
    Off 1
    Wait 0.2 Loop
Fend
```

## See Also
Quit

Resume

Xqt

Halt Statement Example

The example below shows a function named "flicker" that is started by Xqt, then is temporarily stopped by Halt and continued again by Resume.

Function main

  Xqt flicker 'Execute flicker function

  Do

    Wait 3 'Execute task 2 for 3 seconds

    Halt flicker

    Wait 3 'Halt task 2 for 3 seconds

    Resume flicker

  Loop

Fend

Function flicker

  Do

    On 1

    Wait 0.2

    Off 1

    Wait 0.2

  Loop

Fend


---

# Hand Function
**Type:** function | **Section:** Operator

## Syntax
```
Hand [(point)]
```

## Parameters
point	Optional.  Point expression.  If point is omitted, then the hand (arm) orientation of the current robot position is returned.

## Description
Hand Function

Hand Function

See_Also  Example

Returns the hand (arm) orientation of a point.

## Examples
```spel
Print Hand(pick)
Print Hand(P1)
Print Hand
Print Hand(P1 + P2)
```

## See Also
Elbow, Wrist, J4Flag, J6Flag, J1Flag, J2Flag

Hand Function Example

Print Hand(pick)

Print Hand(P1)

Print Hand

Print Hand(P1 + P2)


---

# Hand Keyword
**Type:** reference | **Section:** Operator

## Description
Hand Keyword

Hand Keyword

The Hand keyword is used in these contexts:

Hand Statement

Hand Function


---

# Hand Statement
**Type:** statement | **Section:** Operator

## Syntax
```
(1) Hand point, [ Lefty | Righty]

(2) Hand
```

## Parameters
point	Pnumber or P(expr) or point label.

Lefty | Righty	Hand (arm) orientation

## Description
Hand Statement

Hand Statement

## Examples
```spel
Hand P0, Lefty
Hand pick, Righty
Hand P(myPoint), myHand

P1 = -364.474, 120.952, 469.384, 72.414, 1.125, -79.991
```

## See Also
Sets the hand (arm) orientation of a point.

Elbow, Hand Function, J4Flag, J6Flag, Wrist., J1Flag, J2Flag

Hand Statement Example

Hand P0, Lefty

Hand pick, Righty

Hand P(myPoint), myHand

P1 = -364.474, 120.952, 469.384, 72.414, 1.125, -79.991


---

# Hands page: Robot Manager command (Tools menu)
**Type:** reference | **Section:** Operator

## Description
of the hand.

Configure	Select
		 one hand and click this button to display the [Configure Robot
		 Hand: *] window where you can register a new hand and change or
		 delete the registration information.

Clear	When
		 you select a registered hand and press this button, the hand deletion
		 confirmation dialog will be displayed.

		If you select the [Yes] button here, the registered hand information
		 will be deleted.

Select one hand from hands 1 to 15 and press the [Configure...] button to display the [Configure Robot Hand:] screen.

For more details on hand settings, refer to the following manual:

Hand Function Manual


---

# Here Function
**Type:** function | **Section:** Operator

## Syntax
```
Here
```

## Description
Use Here to retrieve the current position of the current manipulator.

## Examples
```spel
P1 =
				Here
```

## See Also
Here Statement

Here Function Example

P1 =
				Here


---

# Here Keyword
**Type:** reference | **Section:** Operator

## Description
Here Keyword

Here Keyword

The Here keyword is used in these contexts:

Here Statement

Here Function


---

# Here Statement
**Type:** statement | **Section:** Operator

## Syntax
```
Here
			point
```

## Parameters
point	P
						number or P(expr) or point label.

Note:

The Here statement and Parallel Processing

You cannot use both of the Here statement and parallel processing in one motion command like this:

Go Here :Z(0) ! D10; MemOn 1 !

Be sure to change the program like this:

P999 = Here

Go P999 Here :Z(0) ! D10; MemOn 1 !

## Description
Here Statement

Here Statement

See_Also Example

Teach a robot point at the current position.

## Examples
```spel
Go Here :Z(0) ! D10; MemOn 1 !
```

```spel
P999 = Here
```

```spel
Go P999 Here :Z(0) ! D10; MemOn 1 !
```

```spel
Here P1

Here
			 pick
```

## See Also
Here Function

Here Statement Example

Here P1

Here
			 pick


---

# Hex$ Function
**Type:** reference | **Section:** Operator

## Syntax
```
Hex$
			(number)
```

## Parameters
number	Integer expression.

## Description
Hex$ returns a string representing the specified number in hexadecimal format. Each character is from 0-9 or A-F. Hex$ is especially useful for examining the results of the Stat function.

## Examples
```spel
> print
				hex$
			(stat(0))
```

```spel
A00000
```

```spel
> print
				hex$
			(255)
```

```spel
FF
```

## See Also
Str$

Stat

Val

Hex$ Function Example

> print
				hex$
			(stat(0))

A00000

> print
				hex$
			(255)

FF


---

# Home Config: Robot Manager Window
**Type:** reference | **Section:** Operator

## Description
Home Config: Robot Manager Window

[Tools]-[Robot Manager]-[Home Config] Page

Home Config allows you to configure the optional user home position.

For more details on the Home Config settings, refer to the following manual:

SPEL+ Language Reference - HomeSet Statement., Hordr Statement

Changing home position

When you select the [Home Config] tab, the current home position is read from the robot controller and displayed in the text boxes. If the home position has never been defined, then the text boxes will be blank.

To define the home position, you can enter an encoder position value for each of the four robot joints in the text boxes. Alternatively, you can select the [Jog & Teach] page to jog the robot to the desired home position, then select the [Home Config] page and click the [Read Current Position] button to read the current encoder position values.

Changing home order

[Home Order] specifies the order in which each joint moves to the home position. More than one joint can be homed in the same step.

Testing home

After making changes to the home position, open the [Robot Manager]-[Jog & Teach]-[Execute Motion] tab, and then click the [Home] button from the motion command.


---

# Homing the robot
**Type:** reference | **Section:** Operator

## Description
Homing the robot

Homing the robot

The Home command moves the robot to a user defined "park" or "idle" position. This command works for all robots. It is mainly used for absolute encoder robots that normally do not need to be mechanically homed. Use the HomeSet command to set the home position and the Hordr command to set the home order.


---

# How to jog
**Type:** reference | **Section:** Operator

## Description
How to jog

How to jog

In the upper left hand corner of the [Jog & Teach] page, you will see a control group called Jogging that contains jog buttons. In the World, Local, Tool, and ECP jog modes, the robot is jogged in the Cartesian coordinate system (X, Y, Z). In the Joint jog mode, each robot joint can be jogged separately.

The jog speed is determined by the Speed setting.

In step mode, each time you click a jog button, the robot moves along the appropriate axis by the amount specified in the [Jog Distance] control group.

If "Continuous" is selected in the [Jog Distance] group, the movement continues using linear interpolation while the jog key is held down. This is called continuous jog operation.

NOTE:  For robots other than the 6-axis robots, the jog motion in step mode is PTP (point to point) motion. It is difficult to predict exact jog motion trajectory in the PTP motion. Therefore, be careful that the robot doesn't collide with peripheral equipment and that the robot arms don't collide with the robot itself during jogging.

For the 6-axis robots, the jog motion is CP (Continuous Path) motion. Note that when jogging near the singularity, if you try to pass through the singularity, a warning dialog below will appear.

Click the [OK] button and click the same Jog button again to jog using PTP motion and pass the singularity. It is difficult to predict exact jog motion trajectory in the PTP motion. Therefore, be careful that the robot doesn't collide with peripheral equipment and that the robot arms don't collide with the robot itself during jogging. Also, if you attempt the other jogs or operations, it cancels the switching to PTP motion. So when jogging near the singularity again, the same warning dialog will appear.

If passing the singularity in the continuous jog motion, the following warning message will appear.

When jogging in continuous mode, if an out of range condition occurs, the robot motors will turn off and an error will be displayed. In this case you must execute a Reset and Motor On from the Control Panel page to continue the jog.

To jog

Select the jog mode: World, Tool, Local, Joint, or ECP.

Select the jog speed: "Low" or "High".

Select the jog distance (Continuous, Long, Medium, or Short) in the [Jog Distance] group.

You can type in the desired jog distance when "Continuous" is not selected.

Click on one of the jog buttons with the mouse button. If you hold the mouse button down, the robot will continue to jog.

When jogging is started, the jog button color changes from yellow to cyan. After jogging is completed, the jog button color returns to yellow.

If you click any jog button during a step jog, the robot will stop.

NOTE:  You can change the orientation of the jog buttons to in the Epson RC+ 8.0 menu-[Setup]-[Preferences]-[Jog & Teach]. This allows you to align the orientation of the jog buttons with the orientation of the robot motion.

NOTE:  As shown in the illustrations below, when the robot reaches to the limit of the motion range during Continuous Jog motion, the robot stops before the limit of the motion range. Use Step Jog if you want to move the robot to the limit of the motion range. The robot motion stops when the following conditions are satisfied.

-   When the robot's current position becomes "approx. 5 mm or less from the limit of the motion range".

-   When the robot operates Continuous Jog motion in the direction reaching to the limit of motion range as shown in the illustrations below.


---

# How to move the arm with ECP motion
**Type:** reference | **Section:** Operator

## Description
How to move the arm with ECP motion

How to move the arm with ECP motion

In the following paragraphs, the process for moving the 6-Axis robot arm with ECP motion is explained as an example.

1. Setting an ECP

The ECP (external control point) is a coordinate system data used for defining the robot position and orientation at a processing point on the tip of the outside fixed tool.

The ECP should be defined based on the robot coordinate system or desired local coordinate system.

For example, when a drawing shows that the ECP is located at X=300, Y=300, Z=300 based on the robot coordinate system, specify it as shown below.

ECPSet 1,XY(300,300,300,0,0,0)   ' Defines ECP No.1

When you have no ECP location data, you can specify it by teaching.

As an example, attach the tool of which you know the data precisely and bring the tip of the tool close to the ECP and then teach its position anywhere as P0.  Then, specify the ECP using P0 coordinate data as shown below.

ECPSet 1,P0 :U(0) :V(0) :W(0)    ' Defines ECP No.1

The orientation data (U, V, W) were set to 0 in the above examples.  In these cases, the orientation in the ECP coordinate system is equal to that in the reference robot coordinate system.

You can specify U, V, and W coordinates in the ECP coordinate system.  However, this data is valid only during the tangential correction mode ON in the Curve statement and ECP jog motion.

2. Teaching

Teach the point data while moving the robot arm holding the actual part.  In this section, the part is assumed to be a rectangular solid and the arm is moved straight so that it touches one side of the part of the ECP specified in the previous section 1. Setting the ECP.

For details on teaching, refer to Jog and Teach.

2-1 Teaching the motion start point

Move the arm to the motion start point and teach it as P1.

2-2 Teaching the motion end point

Move the arm to the motion end point and teach it as P2.

Note:  ECP Jog Mode:

The ECP jog mode is an additional jog mode used for teaching besides the Joint, World, and Tool jog modes.

The ECP jog mode is based on the selected ECP coordinate system.

3. Executing Motion

To move the arm with ECP motion, add the "ECP" parameter to a motion command.

ECP 1 ' Select ECP

Go P1 ' Moves the arm to the motion start point

Move P2 ECP ' Executes ECP motion

Use the Arc3 command to move the arm in an arc trajectory with the fixed tool.  Use the Curve and CVMove commands to move the arm in cubic spline curves.

## Examples
```spel
ECPSet 1,XY(300,300,300,0,0,0)   ' Defines ECP No.1
```

```spel
ECPSet 1,P0 :U(0) :V(0) :W(0)    ' Defines ECP No.1
```

```spel
ECP 1 ' Select ECP
Go P1 ' Moves the arm to the motion start point
Move P2 ECP ' Executes ECP motion
```


---

# How to teach points
**Type:** reference | **Section:** Operator

## Description
How to teach points

How to teach points

To move the robot to the target point, the point data indicating the robot position is necessary.

Follow these steps to teach points from the [Robot Manager]:

Select
	 the point file you are teaching points for from the [Point File] dropdown
	 list box on the [Teach] page.

Select
	 the point number you want to teach in the [Points] box.

Jog
	 the robot to the desired position. Alternatively, free the robot joints
	 in the [Free Joints] tab, and manually move the robot into position.
	 (Direct teaching)

Click
	 the [Teach] button. This will save the robot's current position data.

	In the Epson RC+ 8.0 menu, if the [Setup]-[Preferences]-[Jog &
	 Teach]-[Prompt for new point information] check box is selected, you
	 can enter point labels and comments. Point labels can include up to
	 32 alphanumeric characters and underscores. Only alphabets can be
	 used for the first letter. Characters can be upper case or lower case.

NOTE:  As an alternative to clicking the [Teach] button, on the [Points] tab you can type in the coordinates of the point.


---

# I/O Label Editor
**Type:** reference | **Section:** Operator

## Description
I/O Label Editor

[I/O Label Editor] Command (Tools Menu)
 : Ctrl+L

The I/O label editor lets you define meaningful names for inputs, outputs, and memory I/O for each project. The labels can be used in your programs, from the Command window, or in macros. They are also displayed in the I/O Monitor window.

Open the I/O Label Editor

Open the I/O Label Editor using either of the following methods.

-    Select the Epson RC+ 8.0 menu-[Tools]-[I/O Label Editor]

-    Or

Type Ctrl + L.

-    Or

Click on the  button on the toolbar.

Navigating the grid

Press the [Tab] key to move to the next cell. Press the [Shift] + [Tab] key to move to the previous cell. Press the arrow [↑] or [↓] key to move to the cell above or below.

TIP:  Enter a bit, byte, or word number on the active window to move the cursor to the corresponding row.

Sign	Description

a	Shows
		 the types of I/O. For each type of I/O you can view and edit labels
		 for bits, bytes (8 bits), and words (16 bits).

b	This
		 shows the bit, byte, or word number for the I/O displayed.

c (when
		 Bit is selected)	Shows
		 the types of I/O defined.

Hover the mouse over the icon to show
		 the label in a tool tip.

: Remote I/O

: Hand I/O

d	Sets
		 the label.

		You can type in up to 32 characters for a label. Label characters
		 can be alphanumeric or underscore.

e	Enter
		 a description associated with the label. If you add a description
		 to a comment, then the description will be displayed as a tool
		 tip on the I/O Monitor.

f	Searches
		 for labels, and moves the cursor to the row of the label found.

g	Only
		 shows registered I/O labels.

NOTE:

-  The I/O Label Editor shows all available I/O types on your controller.

-  If the Virtual I/O in [Setup]-[System Configuration]-[Controller]-[Preferences] is enabled, the I/O Label Editor will display all I/Os.

For example, you can edit Fieldbus I/O labels, but you may not have a Fieldbus board installed in the controller.

Important	■	When
		 you specified the string (SPEL+ commands and so on) that has other
		 roles in Epson RC+ 8.0 as a label, it may have unexpected consequences.
		 Specify a unique label name so that it does not duplicate with
		 those strings.

If you set a keyword, the following dialog
		 will be shown.

Split screen

Drag the split bar at the top of the grid down to split each grid into two scroll regions.

To add or edit a label

(1)    Select the type of I/O label. Shows a label in the spreadsheet.

The number of rows in the spreadsheet equals the number of bits, bytes, or words available for the type you have selected.

(2)    Select the row to add or edit, and then enter a label.

Type in the label, which can be up to 32 alphanumeric characters without any spaces.

Optionally, you can type a description for the label in the [Description] field.

(3)    Save the label.

NOTE:  After adding or editing labels, save the changes in the Epson RC+ 8.0 menu by executing [Save] from the [File] menu or by clicking on the [Save all files]  toolbar button.

If any duplicate labels are detected, an error message will be displayed and the save operation will be aborted. You must correct the duplication before you can save the labels successfully.

Cut and paste labels and descriptions

You can cut and paste labels and descriptions by selecting them with the mouse, then executing [Copy], [Cut], and [Paste] from the Epson RC+ 8.0 [Edit] menu.

You can also cut and paste entire rows using the following steps:

(1)      Select one or more rows by using the row selectors.

Execute either the [Cut] or [Copy] command from the Epson RC+ 8.0 [Edit] menu. When selecting multiple rows, hold down the [Shift] or [Ctrl] key while selecting rows with the mouse.

(2)      Select the row where you want to start the paste by clicking the row selector on the left of the row.

(3)      In the Epson RC+ 8.0 menu, select [Edit]-[Paste].


---

# I/O Monitor Command
**Type:** reference | **Section:** Operator

## Description
I/O Monitor Command

[I/O Monitor] Command (Tools Menu)

: Ctrl+I

The I/O Monitor window lets you monitor all controller hardware inputs and outputs and also memory I/O. You can display up to five screens (three screens in standard view, and two screens in user view) side by side.

A custom view can have any combination of input, output, or memory elements you want to monitor.

Labels that have been defined using the [I/O Label Editor] are displayed next to each bit, byte, or word.

After the [I/O Monitor] window has been opened, the input and output status for the current view is constantly updated.

Mouse over any comment entered in the I/O Label Editor to display it as a tooltip.

You can turn outputs on and off by double clicking on the output LED images in the Status column.

Specify byte and word values to change the status of multiple bits at the same time.

Open the I/O  Monitor

Open the I/O Monitor by either of the following methods.

-  Select the Epson RC+ 8.0 menu-[Tools]-[I/O Monitor]

-  Or,

Click on the  button on the toolbar.

-  Or, type the [Ctrl] + [I] keys on the keyboard.

Item	Description

Adds
		 a standard or user view screen.

Searches
		 for labels, and moves the cursor to the row of the label found.

Status
		 (when [Bit] is selected)	To turn
		 an output off or on, double click on the LED image for the desired
		 output.

When Virtual I/O is active, you can turn
		 input and output bits on and off by double clicking on the input
		 LED images in the Status column.

: On  : Off

Value
		 (when [Byte], [Word] are selected)	Displays
		 the status of each bit summarized in bytes and words.

Show
		 labeled only	Only
		 shows I/Os with preset labels.

Hexadecimal
		 Values	To view
		 bytes and words in hexadecimal format, check the [Hexadecimal
		 Values] checkbox.

Edit	Select
		 the [Edit] checkbox to change the value. Only bytes and words
		 can be used.

Read
		 (when [Edit] is selected)	Reads
		 the current I/O status and value.

Write
		 (when [Edit] is selected)	Sets
		 current values after changes have been made.

NOTE:  Enter a bit, byte, or word number on the active window to move the cursor to the corresponding row.

Using the I/O Monitor

Add view screen

The I/O Monitor window can display up to five screens (three screens in standard view, and two screens in custom view) side by side. There are two standard views available by default. To add a view, click the [+] button on the top right of the window.

Split screen

Drag the split bar at the top of the grid down to split each grid into two scroll regions.

Using Custom View

(1)  Click on a [Custom View] tab.

NOTE:  If a Custom View does not appear, click the [+] button on the top right of the window to select it.

Right-click on a custom view tab to rename the tab.

(2)  Click the [Add] button to add a new row to the list.

(3)  Click the Type column, and then select an I/O type.

(4)  Click on the Port column, and then select a port number.

(5)  Add more rows as needed by repeating steps 2 to 4.

[Apply]: Save the changes.

[Delete]: Delete a row.

[Restore]: Cancel changes.

To rename a view

You can rename custom view tabs.

1. Click the [Custom View] tab.

If no custom views appear, click the [+] button on the top right of the window to select it.

2. Right click on the view tab and select [Rename].

(3)   Rename Custom View will be displayed.

Type in a new name, and then click [OK].

Using Monitor of the Safety Board

Select the [Safety Board] tab. I/O status of the safety board will be shown.

NOTE:  To show the monitor of the safety board, connect Epson RC+ to the Controller installed the safety board.

For the setting of safety functions, refer to the following manual.

Robot Controller Safety Function Manual

NOTE:  The following cannot be operated with I/O monitor of the safety board.

-  Output on/off

-  Displaying custom view

-  Renaming the tab name

Signal for the safety board and the status

Signal	State	Notes

Inputs
		 and Outputs	SAFETY_IN1,
		 SAFETY_IN2,

SAFETY_IN3,

SAFETY_IN4,

SAFETY_IN5	Signal level
		 for safety input is

High: turning
		 LED on

Low: turning
		 LED off	Safety input
		 signal is negative logic (Active Low).

SAFETY_OUT1,
		 SAFETY_OUT2,

SAFETY_OUT3	Signal level
		 for safety output is

High: turning
		 LED on

Low: turning
		 LED off	Safety output
		 signal is negative logic (Active Low).

State	SLS_1, SLS_2,
		 SLS_3	Safety Limited
		 Speed is

Enabled: turning
		 LED on

Disabled turning
		 LED off	For the
		 violation of the limited speed, refer to the system history.

SLP_A, SLP_B,
		 SLP_C	Safety Limited
		 Position is

Enabled: turning
		 LED on

Disabled turning
		 LED off	For the
		 violation of the limited position, refer to the system history.

SLP_J	Soft Axis
		 Limiting

Enabled: turning
		 LED on

Disabled turning
		 LED off	Soft axis
		 limiting is always enabled outside of TEACH mode.

FAIL	Fault detection
		 for safety board

Abnormal:
		 turning LED on

Normal: turning
		 LED off	For the
		 information on the fault, refer to the system history.


---

# If...Then...Else...EndIf Statement
**Type:** reference | **Section:** Operator

## Syntax
```
(1) If condition Then

stmtT1

.

.

[ElseIf condition Then]

stmtT1

.

.

[Else]

stmtF1

.

.

EndIf

(2) If condition Then stmtT1 [; stmtT2 ...] [Else stmtF1 [; stmtF2 ...]]
```

## Parameters
condition	Any valid
		 test condition which returns a True (any number besides 0) or
		 False result (returned as a 0). (See sample conditions below)

stmtT1	Executed when
		 the condition is True. (Multiple statements may be put here in
		 a blocked If...Then...Else
		 style.)

stmtF1	Executed when
		 the condition is False. (Multiple statements may be put here in
		 a blocked If...Then...Else
		 style.)

## Description
(1) If...Then...Else executes stmtT1, etc. when the conditional statement is True. If the condition is False then stmtF1, etc. are executed. The Else portion of the If...Then...Else instruction is optional. If you omit the Else statement and the conditional statement is False, the statement following the EndIf statement will be executed. For blocked If...Then...Else statements the EndIf statement is required to close the block regardless of whether an Else is used or not.

(2) If...Then...Else can also be used in a non blocked fashion. This allows all statements for the If...Then...Else to be put on the same line. Please note that when using If...Then...Else in a non blocked fashion, the EndIf statement is not required. If the If condition specified in this line is satisfied (True), the statements between the Then and Else are executed. If the condition is not satisfied (False), the statements following Else are executed. The Else section of the If...Then...Else is not required. If there is no Else keyword then control passes on to the next statement in the program if the If condition is False.

The logical output of the conditional statement is any number excluding 1 when it is True, and 0 when it is false.

## Notes
Sample Conditions:

a = b  :a is equal to b

a < b  :b is larger than a

a >= b  :a is greater than or equal to b

a <> b  :a is not equal to b

a > b  :b is smaller than a

a <= b  :a is less than or equal to b

Logical operations And, Or and Xor may also be used.

True in the Conditions:

Constant True is -1 and the type is Boolean, so you need to be careful when using it in a comparing condition with other type variable.

Function main

  Integer i

  i = 3

  If i = True Then

    Print "i=TRUE"

EndIf

Fend

When you execute the program above, "i=TRUE" is displayed.

The judgement of condition including the Boolean type is done with "0" or "non-0".

If the value of "i" is not "0", it is considered that the condition is established and "i=TRUE" is displayed.

## Examples
```spel
Function main
```

```spel
Integer i
```

```spel
i = 3
```

```spel
If i = True Then
```

```spel
Print "i=TRUE"
```

```spel
EndIf
```

```spel
Fend
```

```spel
Function main Do
    If Sw(0) = 1 Then On 1 Else Off 1 Loop
Fend
```

```spel
If Sw(0) = 1 Then Print "Input0 ON" Else Print "Input0 OFF"
'
If Sw(1) = 1 Then If Sw(2) = 1 Then
    Print "Input1 On and Input2 ON" Else
    Print "Input1 On and Input2 OFF" EndIf Else If Sw(2) = 1 Then
    Print "Input1 Off and Input2 ON" Else
    Print "Input1 Off and Input2 OFF" EndIf
EndIf
```

```spel
If x = 10 And y = 3 Then GoTo 50
If test <= 10 Then Print "Test Failed"
If Sw(0) = 1 Or Sw(1) = 1 Then Print "Everything OK"
```

## See Also
Select...Case

Do...Loop

If...Then...Else Statement Example

[Single Line If...Then...Else]

The following example shows a simple function which checks an input to determine whether to turn a specific output on or off. This task could be a background I/O task which runs continuously.

Function main

  Do

    If Sw(0) = 1 Then On 1 Else Off 1

  Loop

Fend

[Blocked If...Then...Else]

The following example shows a simple function which checks a few inputs and prints the status of these inputs

If Sw(0) = 1 Then Print "Input0 ON" Else Print "Input0 OFF"

'

If Sw(1) = 1 Then

  If Sw(2) = 1 Then

    Print "Input1 On and Input2 ON"

  Else

    Print "Input1 On and Input2 OFF"

  EndIf

  Else

  If Sw(2) = 1 Then

    Print "Input1 Off and Input2 ON"

  Else

    Print "Input1 Off and Input2 OFF"

  EndIf

EndIf

<Other Syntax


---

# In Function
**Type:** reference | **Section:** Operator

## Syntax
```
In(byteportNumber)
```

## Parameters
byteportNumber	Integer number representing one eight bit port (one byte).

## Description
In provides the ability to look at the value of 8 input channels at the same time. The In instruction can be used to store the 8 I/O channels status into a variable or it can be used with the Wait instruction to Wait until a specific condition which involves more than 1 I/O channel is met.

Since 8 channels are checked at a time, the return values range from 0-255. Please review the chart below to see how the integer return values correspond to individual input channels.

Input Channel Result (Using Byte Port #0)

Return Value	7	6	5	4	3	2	1	0

1	Off	Off	Off	Off	Off	Off	Off	On

5	Off	Off	Off	Off	Off	On	Off	On

15	Off	Off	Off	Off	On	On	On	On

255	On	On	On	On	On	On	On	On

Input Channel Result (Using Byte Port #3)

Return Value	31	30	29	28	27	26	25	24

3	Off	Off	Off	Off	Off	Off	On	On

7	Off	Off	Off	Off	Off	On	On	On

32	Off	Off	On	Off	Off	Off	Off	Off

255	On	On	On	On	On	On	On	On

## Examples
```spel
Function main
		  Integer var1
		  var1 = In(2) 'Get 8 input channels status of byte port 2
		  If var1 > 239 Then
		    Go P1
		    Go P2
		    'Execute other motion statements here
		    '.
		    '.
		  Else
		    Print "Error in initialization!"
		    Print "Sensory Inputs not ready for cycle start"
		    Print "Please check inputs 20,21,22 and 23 for"
		    Print "proper state for cycle start and then"
		    Print "start program again"
		  EndIf
		Fend
```

```spel
> print In(0)
		34
		> print In(1)
		128
		> print In(2)

0
		> print In(3)
		64
```

## See Also
InBCD, MemIn, MemOff, MemOn, MemSW, Off, On, OpBCD, Oport, Out, Sw, Wait

In Function Example

For the example below lets assume that input channels 20,21,22 and 23 are all connected to sensory devices such that the application should not start until each of these devices are returning an On signal indicating everything is OK to start. The program example gets the 8 input channels status of byte port 2 and makes sure that channels 20, 21, 22, and 23 are each On before proceeding.  If they are not On (i.e. returning a value of 1) an error message is given to the operator and the task is stopped.

In the program, the variable "var1" is compared against the number 239 because in order for inputs 20, 21, 22 and 23 to all be On, then the result of In(2) will be 240 or larger. (We don't care about Inputs 16, 17, 18, and 19 in this case so any values between 240-255 will allow the program to proceed.)

Function main

		  Integer var1

		  var1 = In(2) 'Get 8 input channels status of byte port 2

		  If var1 > 239 Then

		    Go P1

		    Go P2

		    'Execute other motion statements here

		    '.

		    '.

		  Else

		    Print "Error in initialization!"

		    Print "Sensory Inputs not ready for cycle start"

		    Print "Please check inputs 20,21,22 and 23 for"

		    Print "proper state for cycle start and then"

		    Print "start program again"

		  EndIf

		Fend

We cannot set inputs from the command window but we can check them. For the examples shown below, we will assume that the Input channels 1, 5, 15, and 30 are On. All other inputs are Off.

> print In(0)

		34

		> print In(1)

		128

		> print In(2)

0

		> print In(3)

		64


---

# InBCD Function
**Type:** reference | **Section:** Operator

## Syntax
```
InBCD(
			portNumber
			)
```

## Parameters
portNumber	Integer number between 0-63 representing one of the 64 input groups (each group contains 8 inputs) which make up the 512 inputs available with EPSON RC+ 7.0.

## Description
InBCD simultaneously reads 8 input lines using the BCD format. The 512 user inputs are broken into 64 groups of 8. The portNumber parameter for the InBCD instruction defines which group of 8 inputs to read where portNumber = 0 means inputs 0-7, portNumber = 1 means inputs 8-15, etc.

The resulting value of the 8 inputs is returned in BCD format. The return value may have 1 or 2 digits between 0 and 99. The 1st digit (or 10's digit) corresponds to the upper 4 outputs of the group of 8 outputs selected by portNumber. The 2nd digit (or 1's digit) corresponds to the lower 4 outputs of the group of 8 outputs selected by portNumber.

Since valid entries in BCD format range from 0-9 for each digit, every I/O combination cannot be met. The table below shows some of the possible I/O combinations and their associated return values assuming that portNumber is 0.

Input Settings (Input number)

## Notes
Difference between InBCD and In

The InBCD and In instructions are very similar in the SPEL language. However, there is one major difference between the two. This difference is shown below:

- The InBCD instruction uses the Binary Coded Decimal format for specifying the return value format for the 8 inputs. Since Binary Coded Decimal format precludes the values of &HA, &HB, &HC, &HD, &HE or &HF from being used, all combinations for the 8 inputs cannot be satisfied.

- The In instruction works very similarly to the InBCD instruction except that In allows the return value for all 8 inputs to be used. (i.e. 0-255 vs. 0-99 for InBCD) This allows all possible combinations for the 8 bit input groups to be read.

## Examples
```spel
> Print InBCD(0)
		11
		> Print InBCD(1)
		04
		> Print InBCD(2)
		07

>
```

## See Also
In, MemOff, MemOn, MemOut, MemSW, Off, On, OpBCD, Oport, Out, Sw, Wait

InBCD Function Example

Some simple examples from the Command window are as follows:

Assume that inputs 0, 4, 10, 16, 17, and 18 are all On (The rest of the inputs are Off)

> Print InBCD(0)

		11

		> Print InBCD(1)

		04

		> Print InBCD(2)

		07

>


---

# InStr Function
**Type:** reference | **Section:** Operator

## Syntax
```
InStr(string, searchString)
```

## Parameters
string	String expression to be searched.

searchString	String expression to be searched for within string
						.

## Description
InStr Function

InStr Function

See_Also Example

Returns position of one string within another.

## Examples
```spel
Integer pos

pos = InStr("abc", "b")
```

## See Also
Mid$

Instr Function Example

Integer pos

pos = InStr("abc", "b")


---

# InW Function
**Type:** reference | **Section:** Operator

## Syntax
```
InW(WordPortNum)
```

## Parameters
WordPortNum	Integer expression representing the I/O Input Word.

## Description
InW Function

InW Function

See_Also Example

Returns the status of the specified input word port. Each word port contains 16 input bits.

## Examples
```spel
Long word0

word0 = InW(0)
```

## See Also
In

Out

OutW

InW Function Example

Long word0

word0 = InW(0)


---

# Inertia Function
**Type:** reference | **Section:** Operator

## Syntax
```
Inertia( paramNumber )
```

## Parameters
paramNumber	Integer expression which can have the following values:

0: Causes function to return 1 if robot supports inertia parameters or 0 if not.

1: Causes function to return load inertia in kgm2.

2: Causes function to return eccentricity in mm.

## Description
Inertia Function

Inertia Function

See_Also Example

Returns inertia parameter value.

## Examples
```spel
Real loadInertia, eccentricity
loadInertia = Inertia(1)
eccentricity = Inertia(2)
```

## See Also
Inertia Statement

For details of Hand, refer to the Hand Function Manual.

Inertia Function Example

Real loadInertia, eccentricity

loadInertia = Inertia(1)

eccentricity = Inertia(2)


---

# Inertia Keyword
**Type:** reference | **Section:** Operator

## Description
Inertia Keyword

Inertia Keyword

The Inertia keyword is used in these contexts:

Inertia Statement

Inertia Function


---

# Inertia Page: Robot Manager Window
**Type:** reference | **Section:** Operator

## Description
Inertia Page: Robot Manager Window

[Tools]-[Robot Manager]-[Inertia] Page

This page is for changing the Inertia parameters.

For more details on Inertia settings, refer to the following manual:

SPEL+ Language Reference - Inertia Statement

You can also set by following "Weight, Inertia, and Eccentricity/offset Measurement Utility".

The following section describes the details.

Weight, Inertia, and Eccentricity/offset Measurement Utility

Item	Description

Load
		 inertia	Type
		 in the new load inertia of the payload on the robot in kgxm2.
		 This includes the inertia of end effector plus the part to be
		 carried.

Eccentricity	Type
		 in the new eccentricity value in millimeters. This is the distance
		 from rotational center of joint 4 to the center of gravity of
		 end effector and part.

Apply	Sets
		 the current values.

Restore	Reverts
		 to the previous values.

Defaults	Displays
		 factory default settings.


---

# Inertia Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Inertia [loadInertia [, eccentricity]]

Inertia
```

## Parameters
loadInertia	Optional (It
		 is not possible to omit only loadInertia).  Real expression
		 that specifies total moment of inertia in kgm2 around the center
		 of the end effector joint, including end effector and part.

eccentricity	Optional.
		  Real expression that specifies eccentricity in mm around
		 the center of the end effector joint, including end effector and
		 part.

When [eccentricity] is omitted, the entered [loadInertia] will be set and the default value [eccentricity] will be set.

It is not possible to omit only [loadInertia].

Note: Note that when you specify a value smaller than the actual value to the inertia or eccentricity, excessive acceleration and deceleration values will be set and may damage the manipulator. In addition, it may cause an error or impact. It may cause the function will not work best, the life of the parts be shortened, or the belt be misaligned due to teeth losing.

## Description
Use the Inertia statement to specify the total moment of inertia for the load on the end effector joint.  This allows the system to more accurately compensate acceleration, deceleration, and servo gains for the end effector joint.
  You can also specify the distance from the center of end effector joint to the center of gravity of the end effector and part using the eccentricity parameter.

Robot parameter data is stored in compact flash in controller.  Therefore, writing to command flash occurs when executing this command.  Frequent writing to compact flash affect to lifetime of compact flash.  We recommend to use this command minimally.

You can also set by following "Weight, Inertia, and Eccentricity/offset Measurement Utility".

The following manual describes the details.

Epson RC+ User's Guide 6.18.12 Weight, Inertia, and Eccentricity / Offset Measurement Utility

## Notes
Inertia Values Are Not Changed by Turning Main Power Off

The Inertia values are not changed by turning power off. Once the value is set, the value is memorized in the controller.

When nothing is changed, it will remain at the previously set value.

## Examples
```spel
Inertia 0.02, 1
```

## See Also
Inertia Function

For details of Hand, refer to the Hand Function Manual.

Inertia Statement


---

# Input # Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Input # portNumber, varName [ , varName, varName,... ]
```

## Parameters
portNumber	The ID number that specifies a file, communication port, database, or device. The File number can be specified in ROpen, WOpen, and AOpen statements.

Communication port number can be specified in OpenCom (RS-232C) and OpenNet (TCP/IP) statements.

The database number can be specified in OpenDB statement.

Device ID is:

21 RC+

24 TP (TP1 only)

20 TP3

varName	Variable name to receive the data.

## Description
The Input # instruction receives numeric or string data from the device specified by PortNum, and assigns the data to the variable(s).

## Notes
Rules for Numeric Input

When inputting numeric values and non-numeric data is found in the input other than the delimiter (comma), the Input instruction discards the non-numeric data and all data following that non-numeric data.

Rules for String Input

When inputting strings, numeric and alpha characters are permitted as data.

Maximum data length

This command can handle up to 256 bytes.

However, when the target is the database, it can handle up to 4096 bytes.

Other Rules for the Input Instruction

- When more than one variable is specified in the instruction, the numeric data input intended for each variable has to be separated by a comma (",") character or blank (" ").

- When more than one string variable or both of numeric variable and string variable is specified, the numeric data has to be separated by a comma (",") character or blank (" ").

- Numeric variable names and string variable names are allowed. However, the input data type must match the variable type.

The following programs are examples to exchange the string variable and numeric variable between the controllers using a communication port.

Sending end (Either pattern is OK.)

Print #PortNum, "$Status,", InData, OutData

Print #PortNum, "$Status", ",",InData, OutData

Receiving end

Input #PortNum, Response$, InData, OutData

Potential Errors

Number of variables and input data differ

When the number of the variables specified in the instruction is different from the number of numeric data received from the device, an Error 2505 will occur.

## Examples
```spel
Print #PortNum, "$Status,", InData, OutData
```

```spel
Print #PortNum, "$Status", ",",InData, OutData
```

```spel
Input #PortNum, Response$, InData, OutData
```

```spel
Function GetData Integer A String B$ OpenCom #1 Print #1, "Send" Input #1, A   'Get a numeric value from Port #1 Input #1, B$  'Get a string from Port #1 CloseCom #1
Fend
```

## See Also
Input

Line Input

Line Input #

Print #

Read

ReadBin

Input # Statement Example

This is a simple program example using Input # statement.

Function GetData

  Integer A

  String B$

  OpenCom #1

  Print #1, "Send"

  Input #1, A   'Get a numeric value from Port #1

  Input #1, B$  'Get a string from Port #1

  CloseCom #1

Fend


---

# Input Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Input varName [ , varName, varName,... ]
```

## Parameters
varName	Variable name. Multiple variables can be used with the Input command as long as they are separated by commas.

## Description
Input receives data from the display device and assigns the data to the variable(s) used with the Input instruction.

When executing the Input instruction, a (?) prompt appears at the display device. After inputting data press the return key (Enter) on the keyboard.

## Notes
Rules for Numeric Input

When inputting numeric values and non-numeric data is found in the input other than the delimiter (comma), the Input instruction discards the non-numeric data and all data following that non-numeric data.

Rules for String Input

When inputting strings, numeric and alpha characters are permitted as data.

Other Rules for the Input Instruction

- When more than one variable is specified in the instruction, the numeric data input intended for each variable has to be separated by a comma (",") character.

- Numeric variable names and string variable names are allowed. However, the input data type must match the variable type.

Potential Errors

Number of variables and input data differ

For multiple variables, the number of input data must match the number of Input variable names. When the number of the variables specified in the instruction is different from the number of numeric data received from the keyboard, an Error 2505 will occur.

## Examples
```spel
Function InputNumbers Real A, B, C Print "Please enter 1 number" Input A Print "Please enter 2 numbers separated by a comma" Input B, C Print "A = ", A Print "B = ", B, " C = ", C
Fend
```

```spel
A sample session of the above program running is shown below:
```

```spel
(Use the Run menu or F5 key to start the program)
```

```spel
Please enter 1 number
```

```spel
?-10000
```

```spel
Please enter 2 numbers separated by a comma
```

```spel
?25.1, -10000
```

```spel
A = -10000
```

```spel
B = 25 C = -10000
```

## See Also
Input #

Line Input

Line Input #

Print

String

Input Statement Example

This is a simple program example using Input statement.

Function InputNumbers

  Real A, B, C

  Print "Please enter 1 number"

  Input A

  Print "Please enter 2 numbers separated by a comma"

  Input B, C

  Print "A = ", A

  Print "B = ", B, " C = ", C

Fend

A sample session of the above program running is shown below:

(Use the Run menu or F5 key to start the program)

Please enter 1 number

?-10000

Please enter 2 numbers separated by a comma

?25.1, -10000

A = -10000

B = 25 C = -10000


---

# InsideBox Function
**Type:** reference | **Section:** Operator

## Syntax
```
InsideBox(AreaNum [, robotNumber | All])
```

## Parameters
AreaNum	Integer expression
		 from 1 to 15 representing which approach check area to return
		 status for.

robotNumber	Integer value
		 that contains the robot number you want to search.

If omitted,
		 the current robot will be specified.

If you specify
		 All, True is returned if one robot is in the check area.

## Description
InsideBox Function

InsideBox Function

## Examples
```spel
Function PrintInsideBox If InsideBox(3,1) = True Then
      Print "Inside Box3"
   Else
      Print "Outside Box3"
   EndIf
Fend
```

## See Also
Returns the check status of the approach check area.

Box

BoxClr

BoxDef

GetRobotInsideBox

InsidePlane

InsideBox Function


---

# InsidePlane Function
**Type:** reference | **Section:** Operator

## Syntax
```
InsidePlane(planeNum [, robotNumber | All])
```

## Parameters
planeNum	Integer expression
		 from 1 to 15 representing which approach check plane to return
		 status for.

robotNumber	Integer value
		 that contains the robot number you want to search.

If omitted,
		 the current robot will be specified.

If you specify
		 All, True is returned if one robot is in the check area.

## Description
InsidePlane Function

InsidePlane Function

## Examples
```spel
Function PrintInsidePlane If InsidePlane(3,1) = True Then
     Print "Inside Plane3" Else
     Print "Outside Plane3" EndIf
Fend
```

## See Also
Returns the check status of the approach check plane.

InsideBox

GetRobotInsidePlane

Plane

PlaneClr

PlaneDef

InsidePlane Function


---

# Installing Controller Options
**Type:** reference | **Section:** Operator

## Description
note for each option.

To enable an option on site

1. Copy and paste or write down the Options Key Code. You can view this from the [Setup]-[Controller]-[Options] dialog.

2. Call the supplier of your region to purchase the enable key code for the desired option.

3. You will receive a code to enable the option from the supplier of your region.

4. Select the option to enable, and then click the [Enable] button.

5. Enter in the code you received from the supplier of your region.

NOTE:  The key code is case sensitive.

If the DMB Board or CF card is replaced

If the DMB board or CF card is replaced due to malfunction, all configured options will be disabled. Follow the procedure in To enable an option on site to configure the options again.

*  If the DMB board or CF card is replaced, the previous code for enabling the option cannot be used.


---

# Int Function
**Type:** reference | **Section:** Operator

## Syntax
```
Int
			(number)
```

## Parameters
number	A real number expression.

## Description
Int(number) takes the value of number and returns the largest integer that is less than or equal to number.

Note

For Values Less than 1 (Negative Numbers)

If the parameter number has a value of less than 1 then the return value have a larger absolute value than number. (For example, if number = -1.35 then -2 will be returned.)

## Examples
```spel
> Print Int(5.1)
```

```spel
5
```

```spel
> Print Int(0.2)
```

```spel
0
```

```spel
> Print Int(-5.1)
```

```spel
-6
```

```spel
>
```

## See Also
Abs	Sgn

Atan	Sin

Atan2	Sqr

Cos	Str$

Fix	Tan

Mod	Val

Not

Int Function Example

Some simple examples from the Command window are as follows:

> Print Int(5.1)

5

> Print Int(0.2)

0

> Print Int(-5.1)

-6

>


---

# Int32 Statement
**Type:** statement | **Section:** Operator

## Syntax
```
Int32 varName [( subscripts )] [, varName [( subscripts )]...
```

## Parameters
varName	Variable name which the user wants to declare.

subscripts	Optional.  Dimensions of an array variable; up to 3 dimensions may be declared.  The subscripts syntax is as follows

(ubound1, [ubound2], [ubound3])

ubound1, ubound2, ubound3 each specify the maximum upper bound for the associated dimension.

The elements in each dimension of an array are numbered from 0 and the available number of array elements is the upper bound value + 1.

When specifying the upper bound value, make sure the number of total elements is within the range shown below:

Local variable  2000

Global Preserve variable  4000

Global variable and module variable  100000

## Description
Int32 is used to declare variables as type integer.  Integer variables can contain values from -2147483648 to 2147483647.  Local variables should be declared at the top of a function.  Global and module variables must be declared outside of functions.

## Examples
```spel
Function inttest Int32 A(10) 'Single dimension array of Int32 Int32 B(10, 10) 'Two dimension array of Int32 Int32 C(5, 5, 5) 'Three dimension array of Int32 Int32 var1, arrayvar(10) Integer i Print "Please enter an Integer Number" Input var1 Print "The Integer variable var1 = ", var1 For i = 1 To 5
    Print "Please enter an Integer Number"
    Input arrayvar(i)
    Print "Value Entered was ", arrayvar(i) Next i
Fend
```

## See Also
Boolean

Byte

Data Types Overview

Double

Global

Int64

Integer

Long

Real

Short

String

UByte

UInt32

UShort

Variable Declarations

Variable Naming Conventions

Int32 Statement Example

The following example shows a simple program which declares some variables as Integers using Int32.

Function inttest

  Int32 A(10) 'Single dimension array of Int32

  Int32 B(10, 10) 'Two dimension array of Int32

  Int32 C(5, 5, 5) 'Three dimension array of Int32

  Int32 var1, arrayvar(10)

  Integer i

  Print "Please enter an Integer Number"

  Input var1

  Print "The Integer variable var1 = ", var1

  For i = 1 To 5

    Print "Please enter an Integer Number"

    Input arrayvar(i)

    Print "Value Entered was ", arrayvar(i)
 Next i

Fend


---

# Int64 Statement
**Type:** statement | **Section:** Operator

## Syntax
```
Int64 varName [( subscripts )] [, varName [( subscripts )]...
```

## Parameters
varName	Variable name which the user wants to declare.

subscripts	Optional.  Dimensions of an array variable; up to 3 dimensions may be declared.  The subscripts syntax is as follows

(ubound1, [ubound2], [ubound3])

ubound1, ubound2, ubound3 each specify the maximum upper bound for the associated dimension.

The elements in each dimension of an array are numbered from 0 and the available number of array elements is the upper bound value + 1.

When specifying the upper bound value, make sure the number of total elements is within the range shown below:

Local variable  2000

Global Preserve variable  4000

Global variable and module variable  100000

## Description
Int64 is used to declare variables as type integer.  Integer variables can contain values from -9223372036854775808 to 9223372036854775807.  Local variables should be declared at the top of a function.  Global and module variables must be declared outside of functions.

## Examples
```spel
Function inttest Int64 A(10) 'Single dimension array of Int64 Int64 B(10, 10) 'Two dimension array of Int64 Int64 C(5, 5, 5) 'Three dimension array of Int64 Int64 var1, arrayvar(10) Integer i Print "Please enter an Integer Number" Input var1 Print "The Integer variable var1 = ", var1 For i = 1 To 5
    Print "Please enter an Integer Number"
    Input arrayvar(i)
    Print "Value Entered was ", arrayvar(i) Next i
Fend
```

## See Also
Boolean

Byte

Data Types Overview

Double

Global

Int32

Integer

Long

Real

Short

String

UByte

UInt32

UShort

Variable Declarations

Variable Naming Conventions

Int64 Statement Example

The following example shows a simple program which declares some variables as Integers using Int64.

Function inttest

  Int64 A(10) 'Single dimension array of Int64

  Int64 B(10, 10) 'Two dimension array of Int64

  Int64 C(5, 5, 5) 'Three dimension array of Int64

  Int64 var1, arrayvar(10)

  Integer i

  Print "Please enter an Integer Number"

  Input var1

  Print "The Integer variable var1 = ", var1

  For i = 1 To 5

    Print "Please enter an Integer Number"

    Input arrayvar(i)

    Print "Value Entered was ", arrayvar(i)
 Next i

Fend


---

# Integer Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Integer varName [( subscripts )] [, varName [( subscripts )]...
```

## Parameters
varName	Variable name which the user wants to declare as type Integer.

subscripts	Optional.  Dimensions of an array variable; up to 3 dimensions may be declared.  The subscripts syntax is as follows

(ubound1, [ubound2], [ubound3])

ubound1, ubound2, ubound3 each specify the maximum upper bound for the associated dimension.

The elements in each dimension of an array are numbered from 0 and the available number of array elements is the upper bound value + 1.

When specifying the upper bound value, make sure the number of total elements is within the range shown below:

Local variable   2000

Global Preserve variable   4000

Global variable and module variable   100000

## Description
Integer is used to declare variables as type Integer.  Variables of type Integer can contain whole numbers with values between -32768 to 32767.  Local variables should be declared at the top of a function.  Global and module variables must be declared outside of functions.

## Examples
```spel
Function inttest Integer A(10) 'Single dimension array of integer Integer B(10, 10) 'Two dimension array of integer Integer C(5, 5, 5) 'Three dimension array of integer Integer var1, arrayvar(10) Integer i Print "Please enter an Integer Number" Input var1 Print "The Integer variable var1 = ", var1 For i = 1 To 5
    Print "Please enter an Integer Number"
    Input arrayvar(i)
    Print "Value Entered was ", arrayvar(i) Next i
Fend
```

## See Also
Boolean

Byte

Data Types Overview

Double

Global

Int32

Long

Real

String

UByte

UInt32

UShort

Variable Declarations

Variable Naming Conventions

Integer Statement Example

The following example shows a simple program which declares some variables as Integers using Integer.

Function inttest

  Integer A(10) 'Single dimension array of integer

  Integer B(10, 10) 'Two dimension array of integer

  Integer C(5, 5, 5) 'Three dimension array of integer

  Integer var1, arrayvar(10)

  Integer i

  Print "Please enter an Integer Number"

  Input var1

  Print "The Integer variable var1 = ", var1

  For i = 1 To 5

    Print "Please enter an Integer Number"

    Input arrayvar(i)

    Print "Value Entered was ", arrayvar(i)
 Next i

Fend


---

# J1Flag Function
**Type:** reference | **Section:** Operator

## Syntax
```
J1Flag [(point)]
```

## Parameters
point	Optional.  Point expression.  If point is omitted, then the J1Flag setting of the current robot position is returned.

## Description
J1Flag Function

J1Flag Function

Returns the J1Flag attribute of a point.

## Examples
```spel
Print J1Flag(pick)
		Print J1Flag(P1)
		Print J1Flag

		Print J1Flag(Pallet(1, 1))
```

## See Also
Hand, J1Flag Statement, J2Flag

J1Flag Function Example

Print J1Flag(pick)

		Print J1Flag(P1)

		Print J1Flag

Print J1Flag(Pallet(1, 1))


---

# J1Flag Statement
**Type:** statement | **Section:** Operator

## Syntax
```
(1) J1Flag point, [value ]

(2) J1Flag
```

## Parameters
point	Pnumber
		 or P(expr) or point label.

value	Optional.
		  Integer expression.

		For RS series Manipulator:

		0 (/J1F0) J1 range is -90 to +270 degrees

1 (/J1F1) J1
		 range is from -270 to -90 or +270 to +450 degrees

		For C8, C12 series Manipulator:

0 (/J1F0) J1
		 range is -180 to +180 degrees

		1 (/J1F1) J1 range is -240 to -180 or +180 to +240 degrees

## Description
J1Flag Statement

J1Flag Statement

## Examples
```spel
J1Flag P0, 1
J1Flag P(mypoint), 0
```

## See Also
Specifies the J1Flag attribute of a point.

Hand, J1Flag Function, J2Flag

J1Flag Statement


---

# J2Flag Function
**Type:** reference | **Section:** Operator

## Syntax
```
J2Flag [(point)]
```

## Parameters
point	Optional.  Point expression.  If point is omitted, then the J2Flag setting of the current robot position is returned.

## Description
J2Flag Function

J2Flag Function

Returns the J2Flag attribute of a point.

## Examples
```spel
Print J2Flag(pick)
		Print J2Flag(P1)
		Print J2Flag

		Print J2Flag(Pallet(1, 1))
```

## See Also
Hand, J2Flag Statement, J1Flag

J2Flag Function Example

Print J2Flag(pick)

		Print J2Flag(P1)

		Print J2Flag

Print J2Flag(Pallet(1, 1))


---

# J2Flag Statement
**Type:** statement | **Section:** Operator

## Syntax
```
(1) J2Flag
			point, [value ]

(2) J2Flag
```

## Parameters
point	P
						number or P(expr) or point label.

value	Optional.  Integer expression.

0 (/J2F0) J2 range is -180 to +180 degrees

1 (/J2F1) J2 range is from -360 to -180 or +180 to +360 degrees

## Description
J2Flag Statement

J2Flag Statement

## Examples
```spel
J2Flag P0, 1

			J2Flag P(mypoint), 0
```

## See Also
Hand, J2Flag Function, J1Flag

J2Flag Statement Example

J2Flag P0, 1

J2Flag P(mypoint), 0


---

# J4Flag Function
**Type:** reference | **Section:** Operator

## Syntax
```
J4Flag [(point)]
```

## Parameters
point	Optional.  Point expression.  If point is omitted, then the J4Flag setting of the current robot position is returned.

## Description
J4Flag Function

J4Flag Function

Returns the J4Flag attribute of a point.

## Examples
```spel
Print J4Flag(pick)

Print J4Flag(P1)

Print J4Flag

Print J4Flag(Pallet(1, 1))
```

## See Also
Elbow, Hand, Wrist, J4Flag Statement, J6Flag

J4Flag Function Example

Print J4Flag(pick)

Print J4Flag(P1)

Print J4Flag

Print J4Flag(Pallet(1, 1))


---

# J4Flag Keyword
**Type:** reference | **Section:** Operator

## Description
J4Flag Keyword

J4Flag Keyword

The J4Flag is used in these contexts:

J4Flag Statement

J4Flag Function


---

# J4Flag Statement
**Type:** statement | **Section:** Operator

## Syntax
```
(1) J4Flag
			point, [value ]

(2) J4Flag
```

## Parameters
point	Pnumber or P(expr) or point label.

value	Optional.  Integer expression.

0 (/J4F0) J4 range is -180 to +180 degrees

1 (/J4F1) J4 range is from -360 to -180 or +180 to +360 degrees

## Description
J4Flag Statement

J4Flag Statement

## Examples
```spel
J4Flag P0, 1

			J4Flag P(mypoint), 0
```

## See Also
Elbow, Hand, J4Flag Function, J6Flag, Wrist

J4Flag Statement Example

J4Flag P0, 1

J4Flag P(mypoint), 0


---

# J6Flag Function
**Type:** reference | **Section:** Operator

## Syntax
```
J6Flag [(point)]
```

## Parameters
point	Optional.  Point expression.  If point is omitted, then the J6Flag setting of the current robot position is returned.

## Description
J6Flag Function

J6Flag Function

Returns the J6Flag attribute of a point.

## Examples
```spel
Print J6Flag(pick)

Print J6Flag(P1)

Print J6Flag

Print J6Flag(P1 + P2)
```

## See Also
Elbow, Hand, Wrist, J4Flag, J6Flag Statement

J6Flag Function Example

Print J6Flag(pick)

Print J6Flag(P1)

Print J6Flag

Print J6Flag(P1 + P2)


---

# J6Flag Keyword
**Type:** reference | **Section:** Operator

## Description
J6Flag Keyword

J6Flag Keyword

The J6Flag is used in these contexts:

J6Flag Statement

J6Flag Function


---

# J6Flag Statement
**Type:** statement | **Section:** Operator

## Syntax
```
(1) J6Flag point, [value ]

(2) J6Flag
```

## Parameters
point	P
		 number or P(expr) or point label.

value	Integer expression.
		  Range is 0 - 127 (/J6F0 - /J6F127).  J6 range for the
		 specified point is as follows:

( -180 * (value+1)
		  < J6 <= -180 * value ) and ( 180 * value < J6 <=
		 180 * (value+1) )

## Description
J6Flag Statement

J6Flag Statement

## Examples
```spel
J6Flag P0, 1
J6Flag P(mypoint), 0
```

## See Also
Sets the J6Flag attribute of a point.

Elbow, Hand, J4Flag, J6Flag Function, Wrist

J6Flag Statement


---

# JA Function
**Type:** reference | **Section:** Operator

## Syntax
```
JA( j1, j2, j3, j4,[ j5, j6 ] , [ j7 ], [ j8, j9 ] )
```

## Parameters
j1 - j9	Real expressions representing joint angles.

For for linear joints, specifies in units of mm.

j5 and j6 are for the 6-axis robot (including N series) and Joint type 6-axis robot.

j7 is for the Joint type 7-axis robot.

j8 and j9 are for the additional ST axis.

Note

If the angle exceeding the motion range is specified, an out of range error occurs.

## Description
Use JA to specify a robot point using joint angles.

When the points returned from JA function specify a singularity of the robot, the joint angles of the robot do not always agree with the joint angles supplied to the JA function as arguments during the execution of a motion command for the points.  To operate the robot using the joint angles specified for the JA function, avoid a singularity of the robot.

For example:

> go ja(0,0,0,90,0,-90)

> where

WORLD:  X:    0.000 mm  Y:  655.000 mm  Z:  675.000 mm  U:    0.000 deg V:  -90.000 deg W:  -90.000 deg

JOINT:  1:    0.000 deg 2:    0.000 deg 3:    0.000 deg 4:    0.000 deg 5:    0.000 deg 6:    0.000 deg

PULSE:  1:        0 pls 2:        0 pls 3:        0 pls 4:        0 pls 5:        0 pls 6:        0 pls

> go ja(0,0,0,90,0.001,-90)

> where

WORLD:  X:   -0.004 mm  Y:  655.000 mm  Z:  675.000 mm  U:    0.000 deg V:  -90.000 deg W:  -89.999 deg

JOINT:  1:    0.000 deg 2:    0.000 deg 3:    0.000 deg 4:   90.000 deg 5:    0.001 deg 6:  -90.000 deg

PULSE:  1:        0 pls 2:        0 pls 3:        0 pls 4:  2621440 pls 5:       29 pls 6: -1638400 pls

## Examples
```spel
> go ja(0,0,0,90,0,-90)
```

```spel
> where
```

```spel
WORLD:  X:    0.000 mm  Y:  655.000 mm  Z:  675.000 mm  U:    0.000 deg V:  -90.000 deg W:  -90.000 deg
```

```spel
JOINT:  1:    0.000 deg 2:    0.000 deg 3:    0.000 deg 4:    0.000 deg 5:    0.000 deg 6:    0.000 deg
```

```spel
PULSE:  1:        0 pls 2:        0 pls 3:        0 pls 4:        0 pls 5:        0 pls 6:        0 pls
```

```spel
> go ja(0,0,0,90,0.001,-90)
```

```spel
> where
```

```spel
WORLD:  X:   -0.004 mm  Y:  655.000 mm  Z:  675.000 mm  U:    0.000 deg V:  -90.000 deg W:  -89.999 deg
```

```spel
JOINT:  1:    0.000 deg 2:    0.000 deg 3:    0.000 deg 4:   90.000 deg 5:    0.001 deg 6:  -90.000 deg
```

```spel
PULSE:  1:        0 pls 2:        0 pls 3:        0 pls 4:  2621440 pls 5:       29 pls 6: -1638400 pls
```

```spel
P10 = JA(60, 30, -50, 45)
Go JA(135, 90, -50, 90)
P3 = JA(0, 0, 0, 0, 0, 0)
```

## See Also
AglToPls

XY

Ja Function Example

P10 = JA(60, 30, -50, 45)

Go JA(135, 90, -50, 90)

P3 = JA(0, 0, 0, 0, 0, 0)


---

# JRange Function
**Type:** function | **Section:** Operator

## Syntax
```
JRange(jointNumber, paramNumber)
```

## Parameters
jointNumber	Specifies reference joint number (integer from 1 - 9) by an expression or numeric value.

The additional S axis is 8 and T axis is 9.

paramNumber	Integer expression containing one of two values:
 1: Specifies lower limit value.
 2: Specifies upper limit value.

## Description
JRange Function

JRange Function

See_Also Example

Returns the permissible working range of the specified joint in pulses.

## Examples
```spel
Long i, oldRanges(3, 1)

For i = 0 To 3
		  oldRanges(i, 0) = JRange(i + 1, 1)
		  oldRanges(i, 1) = JRange(i + 1, 2)
		Next i
```

## See Also
Range Statement

JRange Statement

JRange Function Example

Long i, oldRanges(3, 1)

For i = 0 To 3

		  oldRanges(i, 0) = JRange(i + 1, 1)

		  oldRanges(i, 1) = JRange(i + 1, 2)

		Next i


---

# JRange Keyword
**Type:** reference | **Section:** Operator

## Description
JRange Keyword

JRange Keyword

The JRange keyword is used in these contexts:

JRange Statement

JRange Function


---

# JRange Statement
**Type:** statement | **Section:** Operator

## Syntax
```
JRange jointNumber, lowerLimit, upperLmit
```

## Parameters
jointNumber	Integer expression between 1-9 representing the joint for which JRange will be specified.

The additional S axis is 8 and T axis is 9.

lowerLmit	Long integer expression representing the encoder pulse count position for the lower limit range of the specified joint.

upperLmit	Long Integer expression representing the encoder pulse count position for the upper limit range of the specified joint.

## Description
Defines the permissible working range for the specified joint with upper and lower limits in encoder pulse counts. JRange is similar to the Range command.  However, the Range command requires that all joint range limits be set while the JRange command can be used to set each joint working limits individually thus reducing the number of parameters required.  To confirm the defined working range, use the Range command.

Robot parameter data is stored in compact flash in controller.  Therefore, writing to command flash occurs when executing this command.  Frequent writing to compact flash affect to lifetime of compact flash.  We recommend to use this command minimally.

## Notes
Lower Limits Must Not Exceed Upper Limits:

The Lower limit defined in the JRange command must not exceed the Upper limit.  A lower limit in excess of the Upper limit will cause an error, making it impossible to execute a motion command.

Factors Which can Change JRange:

Once JRange values are set they remain in place until the user modifies the values either by the Range or JRange commands.  Turning controller power off will not change the JRange joint limit values.

Maximum and Minimum Working Ranges:

Refer to the specifications in the Robot manual for maximum working ranges for each robot model since these vary from model to model.

## Examples
```spel
> JRange 2, -6000, 7000  'Define the 2nd joint range
```

```spel
> JRange 1, 0, 7000  'Define the 1st joint range
```

## See Also
JRange Function

Range

JRange Statement Example

The following examples are done from the Command window:

> JRange 2, -6000, 7000  'Define the 2nd joint range

> JRange 1, 0, 7000  'Define the 1st joint range


---

# JS Function
**Type:** reference | **Section:** Operator

## Syntax
```
JS
```

## Description
JS is used in conjunction with the Jump and Sense instructions.  The purpose of the JS instruction is to provide a status result as to whether an input condition (as defined by the Sense instruction) is met during motion caused by the Jump instruction or not.  When the input condition is met, JS returns True.  When the input condition is not met and the arm reaches the target position, JS returns False.

JS is simply a status check instruction and does not cause motion or specify which Input to check during motion.  The Jump instruction is used to initiate motion and the Sense instruction is used to specify which Input (if any) to check during Jump initiated motion.

Note

JS Works only with the Most Recent Jump, Jump3, JumpTLZ, Jump3CP Instruction

JS can only be used to check the most recent Jump instruction's input check (which is initiated by the Sense instruction.) Once a 2nd Jump instruction is initiated, the JS instruction can only return the status for the 2nd Jump instruction. The JS status for the first Jump is gone forever. So be sure to always do any JS status check for Jump instructions immediately following the Jump instruction to be checked.

## Examples
```spel
Function SearchSensor As Boolean Sense Sw(5) = On Jump P0 Jump P1 Sense If JS = TRUE Then
    Print "Sensor was found"
    SearchSensor = TRUE EndIf
Fend
```

## See Also
JT

Jump

Jump3

Jump3CP

JumpTLZ

Sense

JS Function Example

Function SearchSensor As Boolean

  Sense Sw(5) = On

  Jump P0

  Jump P1 Sense

  If JS = TRUE Then

    Print "Sensor was found"

    SearchSensor = TRUE

  EndIf

Fend


---

# JT Function
**Type:** reference | **Section:** Operator

## Syntax
```
JT
```

## Description
Use JT to determine the status of the most recent Jump command that was stopped before completion by Sense, Till, abort, etc.

## Examples
```spel
Function SearchTill As Boolean Till Sw(5) = On Jump P0 Jump P1 Till If JT And 4 Then Print "Motion stopped during descent"
    SearchTill = TRUE EndIf
Fend
```

## See Also
JS

Jump

Jump3

Jump3CP

JumpTLZ

Sense

Till

JT Function Example

Function SearchTill As Boolean

  Till Sw(5) = On

  Jump P0

  Jump P1 Till

  If JT And 4 Then

  Print "Motion stopped during descent"

    SearchTill = TRUE

  EndIf

Fend


---

# JTran Statement
**Type:** reference | **Section:** Operator

## Syntax
```
JTran
			jointNumber, distance
```

## Parameters
jointNumber	Integer expression representing which joint to move.

The additional S axis is 8 and T axis is 9.

distance	Real expression representing the distance to move in degrees for rotational joints or millimeters for linear joints.

## Description
Use JTran to move one joint a specified distance from the current position.

## Examples
```spel
JTran 1, 20
```

## See Also
Go

Jump

Move

PTran

JTran Statement Example

JTran 1, 20


---

# Jogging in Teach Mode
**Type:** reference | **Section:** Operator

## Description
Jogging in Teach Mode

Jogging in Teach Mode

You can jog and move the robot at slow speed with the safeguard open by using the Teach Pendant. For more details, refer to the following manual:

Robot Controller option Teach Pendant TP1 manual.

Robot Controller option Teach Pendant TP2 manual.

Robot Controller option Teach Pendant TP3 manual.

Robot Controller option Teach Pendant TP4 manual.


---

# Joint Statement
**Type:** statement | **Section:** Operator

## Syntax
```
Joint
```

## Description
Joint Statement

Joint Statement

## Examples
```spel
>joint
```

```spel
JOINT:  1:
   -6.905 deg 2:   23.437 deg 3:   -1.999 mm  4:  -16.529 deg
```

```spel
>
```

## See Also
Displays the current position for the robot in joint coordinates.

Pulse

Where

Joint Statement Example

>joint

JOINT:  1:
   -6.905 deg 2:   23.437 deg 3:   -1.999 mm  4:  -16.529 deg

>


---

# Joint motion
**Type:** reference | **Section:** Operator

## Description
Joint motion

Joint motion

JTran	The JTran command can be used to move one joint of the robot a relative distance from the current position in degrees or millimeters, depending on the joint type.  The speed and acceleration are the same as for point to point motion commands.

PTran	The PTran command can be used to move one joint of the robot a relative distance from the current position in pulses.
  The speed and acceleration are the same as for point to point motion commands.

Pulse	The Pulse command can be used to move all joints of the robot to absolute encoder pulse positions.  The speed and acceleration are the same as for point to point motion commands.

PG_Scan	The PG_Scan command can be used to rotate a pulse generator axis of a
Joint-type single axis PG robot continuously in CW/CCW directions. (To
rotate it continuously, you need to enable the continuous rotation
parameter.) The speed and acceleration are the same as for point to point
motion commands -- i.e., specified with Speed or Accel commands.


---

# Jump Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Jump destination [C archNumber] [LimZ zLimit ] [CP] [searchExpr] [!...!] [SYNC]
```

## Parameters
destination	The target destination of the motion using a point expression.

archNumber	Optional. The arch number (archNumber) specifies which Arch Table entry to use for the Arch type motion caused by the Jump instruction. archNumber can be an expression, and must always be proceeded by the letter C. (Valid entries are C0-C7.)

zLimit	Optional. This is a Z limit value which represents the maximum position the Z joint will travel to during the Jump motion. This can be thought of as the Z Height Ceiling for the Jump instruction. Any valid Z joint Coordinate value is acceptable.

CP	Optional.  Specifies continuous path motion.

searchExpr	Optional. A Sense, Till or Find expression.

Sense | Till | Find

Sense Sw(expr) = {On | Off}

Till Sw(expr) = {On | Off}

Find Sw(expr) = {On | Off}

!...!	Optional. Parallel Processing statements can be added to the Jump instruction to cause I/O and other commands to execute during motion.

SYNC	Reserves a motion command. The robot will not move until SyncRobots is executed.

## Description
Jump moves the arm from the current position to destination using what is called Arch Motion. Jump can be thought of as 3 motions in 1. For example, when the Arch table entry defined by archNumber is 7, the following 3 motions will occur.

1) The move begins with only Z-joint motion until it reaches the Z joint height calculated by the Arch number used for the Jump command.

2) Next the arm moves horizontally (while still moving upward in Z) towards the target point position until the upper Z Limit (defined by LimZ) is reached. Then the arm begins to move downward in the Z direction (while continuing X, Y and U joint motion) until the final X, and Y and U joint positions are reached.

3) The Jump instruction is then completed by moving the arm down with only Z-joint motion until the target Z-joint position is reached.

The coordinates of destination (the target position for the move) must be taught previously before executing the Jump instruction. The coordinates cannot be specified in the Jump instruction itself. Acceleration and deceleration for the Jump is controlled by the Accel instruction. Speed for the move is controlled by the Speed instruction.

archNumber Details

The Arch for the Jump instruction can be modified based on the archNumber value optionally specified with the Jump instruction. This allows the user to define how much Z to move before beginning the X, Y, and U joint motion. (This allows the user to move the arm up and out of the way of parts, feeders and other objects before beginning horizontal motion.) Valid archNumber entries for the Jump instruction are between C0-C7. The Arch table entries for C0-C6 are user definable with the Arch instruction. However, C7 is a special Arch entry which always defines what is called Gate Motion. Gate Motion means that the robot first moves Z all the way to the coordinate defined by LimZ before beginning any X, Y, or U joint motion. Once the LimZ Z limit is reached, X, Y and U joint motion begins. After the X, Y, and U joints each reaches its final destination position, then the Z joint can begin moving downward towards the final Z joint coordinate position as defined by destination (the target point). Gate Motion looks as follows:

LimZ Details

LimZ zLimit specifies the upper Z coordinate value for the horizontal movement plane in the current local coordinate system.  The definition of archnum can cause the X, Y, and U joints to begin movement before reaching LimZ, but LimZ is always the maximum Z height for the move.  When the LimZ optional parameter is omitted, the previous value specified by the LimZ instruction is used for the horizontal movement plane definition.

It is important to note that the LimZ zLimit height limit specification is the Z value for the local robot coordinate system.  It is not the Z value for Arm or Tool.  Therefore take the necessary precautions when using tools or hands with different operating heights.

Sense Details

The Sense optional parameter allows the user to check for an input condition or memory I/O condition before beginning the final Z motion downward.  If satisfied, this command completes with the robot stopped above the target position where only Z motion is required to reach the target position.  It is important to note that the robot arm does not stop immediately upon sensing the Sense input modifier.

The Js or Stat commands can then be used to verify whether the Sense condition was satisfied and the robot stopped prior to its target position or that the Sense condition was not satisfied and the robot continued until stopping at its target position.

Till Details

The optional Till qualifier allows the user to specify a condition to cause the robot to decelerate to a stop prior to completing the Jump.  The condition specified is simply a check against one of the I/O inputs or one of the memory I/O.  This is accomplished through using either the Sw or MemSw function.  The user can check if the input is On or Off and cause the arm to decelerate and stop based on the condition specified.

The Stat function can be used to verify whether the Till condition has been satisfied and this command has been completed, or the Till condition has not been satisfied and the robot stopped at the target position.

## Notes
Jump cannot be executed for 6-axis robots

Use Jump3 or Jump3CP for 6-axis robots.

Caution for Arch motion

Jump motion trajectory is comprised of vertical motion and horizontal motion. It is not a continuous path trajectory. The actual Jump trajectory of arch motion is not determined by Arch parameters alone. It also depends on motion and speed.

Always use care when optimizing Jump trajectory in your applications.  Execute Jump with the desired motion and speed to verify the actual trajectory.

When speed is lower, the trajectory will be lower.  If Jump is executed with high speed to verify an arch motion trajectory, the end effector may crash into an obstacle with lower speed.

In a Jump trajectory, the depart distance increases and the approach distance decreases when the motion speed is set high. When the fall distance of the trajectory is shorter than the expected, lower the speed and/or the deceleration, or change the fall distance to be larger.

Even if Jump commands with the same distance and speed are executed, the trajectory is affected by motion of the robot arms.  As a general example, for a SCARA robot the vertical upward distance increases and the vertical downward distance decreases when the movement of the first arm is large.  When the vertical fall distance decreases and the trajectory is shorter than the expected, lower the speed and/or the deceleration, or change the fall distance to be larger.

Omitting archNumber Parameter

If the archNumber optional parameter is omitted, the default Arch entry for use with the Jump instruction is C7. This will cause Gate Motion, as described above.

Difference between Jump and Jump3, Jump3CP

The Jump3 and Jump3CP instructions can be used for 6-axis robots.  On the other hand the Jump instruction cannot be used for 6-axis robots.  For SCARA robots (including DHS type), using the Jump instruction shortens the joint motion time for depart and approach motion.  The depart and approach motions in Jump3 can be executed along the Z axis and in other directions.

Difference between Jump and Go

The Go instruction is similar to Jump in that they both cause Point to Point type motion, however there are many differences. The most important difference is that the Go instruction simply causes Point to Point motion where all joints start and stop at the same time (they are synchronized). Jump is different since it causes vertical Z movement at the beginning and end of the move. Jump is ideal for pick and place type applications.

Decelerating to a Stop With the Jump Instruction

The Jump instruction always causes the arm to decelerate to a stop prior to reaching the destination point.

Proper Speed and Acceleration Instructions with Jump:

The Speed and Accel instructions are used to specify the speed and acceleration of the robot during Jump motion. Pay close attention to the fact that Speed and Accel apply to point to point type motion (Go, Jump, Etc.). while linear and circular interpolated motion instructions such as Move or Arc use the SpeedS and AccelS instructions. For the Jump instruction, it is possible to separately specify speeds and accelerations for Z joint upward motion, horizontal travel including U joint rotation, and Z joint downward motion.

Pass Function of Jump

When the CP parameter is specified for Jump with 0 downward motion, the Jump horizontal travel does not decelerate to a stop but goes on smoothly to the next PTP motion.

When the CP parameter is specified for a PTP motion command right before a Jump with 0 upward motion, the PTP motion does not decelerate to a stop but connects smoothly with the Jump horizontal travel.

This is useful when you want to replace the horizontal travel of Jump (a PTP motion) with several PTP motions.

(Example)

    Go P1

    Jump P2 :Z(-50) C0 LimZ -50 CP

    Go P3 :Z(0) CP

    Jump P4 C0 LimZ 0

Potential Errors

LimZ Value Not High Enough

When the current arm position of the Z joint is higher than the value set for LimZ and a Jump instruction is attempted, an Error 4005 will occur.

## Examples
```spel
Function jumptest Home Go P0 Go P1 Sense Sw(4) = On Jump P0 LimZ -10 Jump P1 LimZ -10 Sense 'Check input #4 If Js(0) = 1 Then
    Print "Input #4 came on during the move and"
    Print "the robot stopped prior to arriving on"
    Print "point P1." Else
    Print "The move to P1 completed successfully."
    Print "Input #4 never came on during the move." EndIf
Fend
```

```spel
> Jump P10+X50 C0 LimZ-20 Sense !D50;On 0;D80;On 1!
```

## See Also
Robot motion commands

!....! Parallel Processing

Accel

Arc

Arch

Go

Js

Jt

JTran

LimZ

Point Expression

Pulse

Sense

Speed

Stat

Till

Jump Statement Example

The example shown below shows a simple point to point move between points P0 and P1 and then moves back to P0 using the Jump instruction. Later in the program the arm moves using the Jump instruction. If input #4 never goes high then the arm starts the approach motion and moves to P1. If input #4 goes high then the arm does not execute the approach motion.

Function jumptest

  Home

  Go P0

  Go P1

  Sense Sw(4) = On

  Jump P0 LimZ -10

  Jump P1 LimZ -10 Sense 'Check input #4

  If Js(0) = 1 Then

    Print "Input #4 came on during the move and"

    Print "the robot stopped prior to arriving on"

    Print "point P1."

  Else

    Print "The move to P1 completed successfully."

    Print "Input #4 never came on during the move."

  EndIf

Fend

> Jump P10+X50 C0 LimZ-20 Sense !D50;On 0;D80;On 1!


---

# Jump3, Jump3CP Statements
**Type:** reference | **Section:** Operator

## Syntax
```
(1) Jump3  depart, approach, destination  [C archNumber] [CP] [LJM [orientationFlag]] [searchExpr] [!...!] [SYNC]

(2) Jump3CP  depart, approach, destination  [ROT] [C archNumber] [CP] [LJM [orientationFlag]] [searchExpr] [!...!] [SYNC]
```

## Parameters
depart	The departure point above the current position using a point expression.

approach	The approach point above the destination position a point expression.

destination	The target destination of the motion using a point expression.

ROT	Optional.  :Decides the speed/acceleration/deceleration in favor of tool rotation.

archNumber	Optional.  The arch number (archNumber) specifies which Arch Table entry to use for the Arch type motion caused by the Jump instruction. archNumber must always be proceeded by the letter C. (Valid entries are C0-C7.)

CP	Optional.  Specifies continuous path motion.

LJM	Optional.  Convert the target destination using LJM function.

orientationFlag	Optional.  Specifies a parameter that selects an orientation flag for LJM function.

searchExpr	Optional.  A Sense, Till or Find expression.

Sense | Till | Find

Sense Sw(expr) = {On | Off}

Till Sw(expr) = {On | Off}

Find Sw(expr) = {On | Off}

!...!	Optional.  Parallel Processing statements can be added to the Jump instruction to cause I/O and other commands to execute during motion.

SYNC	Reserves a motion command. The robot will not move until SyncRobots is executed.

## Description
Moves the arm from the current position to the destination point with 3D gate motion.  3D gate motion consists of depart motion, span motion, and approach motion.  The depart motion form the current position to the depart point is always CP motion.  The span motion from the depart point to the start approach point is PTP motion in Jump3, and the CP motion in Jump3CP.

The approach motion from the starting approach point to the target point is always CP motion.

Arch motion is achieved by specifying the arch number.  The arch motion for Jump3, Jump3CP is as shown in the figure below.  For arch motion to occur, the Depart distance must be greateer than the arch upward distance and the Approach distance must be greater than the arch downward distance.

Jump3CP uses the SpeedS speed value and AccelS acceleration and deceleration values. Refer to Using Jump3, Jump3CP with CP below on the relation between the speed/acceleration and the acceleration/deceleration.  If, however, the ROT modifier parameter is used, Jump3CP uses the SpeedR speed value and AccelR acceleration and deceleration values.  In this case SpeedS speed value and AccelS acceleration and deceleration value  have no effect.

Usually, when the move distance is 0 and only the tool orientation is changed, an error will occur. However, by using the ROT parameter and giving priority to the acceleration and the deceleration of the tool rotation, it is possible to move without an error. When there is not an orientational change with the ROT modifier parameter and movement distance is not 0, an error will occur.

Also, when the tool rotation is large as compared to move distance, and when the rotation speed exceeds the specified speed of the manipulator, an error will occur. In this case, please reduce the speed or append the ROT modifier parameter to give priority to the rotational speed/acceleration/deceleration.

## Notes
Jump3 span motion is PTP (point to point)

It is difficult to predict Jump3 span motion trajectory.  Therefore, be careful that the robot doesn't collide with peripheral equipment and that robot arms don't collide with the robot.

Jump3 Motion trajectory changes depending on motion and speed

Jump3 motion trajectory is comprised of depart, span, and approach motions.  It is not a continuous path trajectory.  The actual Jump3 trajectory of arch motion is not determined by Arch parameters alone.  It also depends on motion and speed.

Always use care when optimizing Jump3 trajectory in your applications.  Execute Jump3 with the desired motion and speed to verify the actual trajectory.

When speed is lower, the trajectory will be lower.  If Jump3 is executed with high speed to verify an arch motion trajectory, the end effector may crash into an obstacle with lower speed.

In a Jump3 trajectory, the depart distance increases and the approach distance decreases when the motion speed is set high. When the approach distance of the trajectory is shorter than the expected, lower the speed and/or the deceleration, or change the approach distance to be larger.

Even if Jump commands with the same distance and speed are executed, the trajectory is affected by motion of the robot arms.  As a general example, for a SCARA robot the depart distance increases and the approach distance decreases when the movement of the first arm is large.  When the approach distance decreases and the trajectory is shorter than the expected, lower the speed and/or the deceleration, or change the approach distance to be larger.

LimZ does not affect Jump3 and Jump3CP

LimZ has no affect on Jump3 or Jump3CP since the span motion is not necessarily perpendicular to the Z axis of the coordinate system.

Potential acceleration errors

An acceleration error may occur during an arch motion execution by the Jump3 andJump3CP commands.  This error is issued frequently when the majority of the motion during depart or approach uses the same joint as the span motion.  To avoid this error, reduce the acceleration/deceleration speed of the span motion using Accel command for Jump3 or using Accels command for Jump3CP.  Depending on the motion and orientation of the robot, it may also help to reduce the acceleration and deceleration of the depart motion (approach motion) using the Accels command.

Using Jump3, Jump3CP with CP

The CP parameter causes the arm to move to destination without decelerating or stopping at the point defined by destination.  This is done to allow the user to string a series of motion instructions together to cause the arm to move along a continuous path while maintaining a specified speed throughout all the motion.  The Jump3CP instruction without CP always causes the arm to decelerate to a stop prior to reaching the point destination.

Pass Function of Jump3

When the CP parameter is specified for Jump3 with 0 approach motion, the Jump3 span motion does not decelerate to a stop but goes on smoothly to the next PTP motion.

When the CP parameter is specified for a PTP motion command right before Jump3 with 0 depart motion, the PTP motion does not decelerate to a stop but connects smoothly with the Jump3 span motion.

This is useful when you want to replace the span motion of Jump3 (a PTP motion) with several PTP motions.

Pass Function of Jump3CP

When the CP parameter is specified for Jump3CP with 0 approach motion, the Jump3CP span motion does not decelerate to a stop but goes on smoothly to the next CP motion.

When the CP parameter is specified for a CP motion command right before Jump3CP with 0 depart motion, the CP motion does not decelerate to a stop but connects smoothly with the Jump3CP span motion.

This is useful when you want to replace the span motion of Jump3CP (a CP motion) with several CP motions.

(Example 1)

Jump3 P1,P2,P2 CP

Go P3,P4 CP

Jump3 P4,P5,P5+tlz(50)

(Example 2)

Jump3CP P1,P2,P2 CP

Move P3,P4 CP

Jump3CP P4,P5,P5+tlz(50)

Use Jump3, Jump3CP with LJM

With LJM parameter, the program using LJM function can be more simple.

For example, the following four-line program

P11 = LJM(P1, Here, 2)

P12 = LJM(P2, P11, 2)

P13 = LJM(P3, P12, 2)

Jump3 P11, P12, P13

can be... the one-line program.

Jump3 P1, P2, P3 LJM 2

LJM parameter is available for 6-axis (including N series) and RS series robots.

Jump3CP span motion is straight line (CP) motion and it cannot switch the wrist orientation along the way. Therefore, do not use the orientationFlag (LJM 1) of LJM function which is able to switch the wrist orientation.

## Examples
```spel
P11 = LJM(P1, Here, 2)
```

```spel
P12 = LJM(P2, P11, 2)
```

```spel
P13 = LJM(P3, P12, 2)
```

```spel
Jump3 P11, P12, P13
```

```spel
Jump3 P1, P2, P3 LJM 2
```

```spel
' 6 axis robot motion which works like Jump of SCARA robot
Jump3  Here :Z(100), P3:Z(100), P3
' Depart and approach use Z tool coordinates
Jump3  Here -TLZ(100), P3-TLZ(100), P3
' Depart uses base Z and approach uses tool Z
Jump3  Here P*+Z(100), P3-TLZ(100), P3
```

```spel
Arch 0,20,20
Tool 1
Go P1
P2 = P1 -TLZ(100)
Tool 2
Jump3 P2, P3-TLZ(100), P3 C0
```

## See Also
Accel, Arc, Arc3, Arch, Go, JS, JT, Point Expression, Pulse, Sense, Speed, Stat, Till

Jump3 Statement Example

' 6 axis robot motion which works like Jump of SCARA robot

Jump3  Here :Z(100), P3:Z(100), P3

' Depart and approach use Z tool coordinates

Jump3  Here -TLZ(100), P3-TLZ(100), P3

' Depart uses base Z and approach uses tool Z

Jump3  Here P*+Z(100), P3-TLZ(100), P3

Example for the depart motion from P1 in Tool 1 and the approach motion to P3 in Tool 2

Arch 0,20,20

Tool 1

Go P1

P2 = P1 -TLZ(100)

Tool 2

Jump3 P2, P3-TLZ(100), P3 C0


---

# JumpTLZ
**Type:** reference | **Section:** Operator

## Syntax
```
JumpTLZ  destination, TLZ movement, [CarchNumber] [CP] [LJM [orientationFlag]] [searchExpr] [!...!] [SYNC]
```

## Parameters
destination	The target destination of the motion using a point expression.

TLZ movement	The amount of movement in Z direction in Tool coordinate system.  The is unit is [mm].

The Tool coordinate system for the currently used Tool number is used.

archNumber	Optional.  The arch number (archNumber) specifies which Arch Table entry to use for the Arch type motion caused by the Jump instruction. archNumber must always be proceeded by the letter C. (Valid entries are C0-C7.)

CP	Optional.  Specifies continuous path motion.

LJM	Optional.  Convert the target destination using LJM function.

orientationFlag	Optional.  Specifies a parameter that selects an orientation flag for LJM function.

searchExpr	Optional.  A Sense, Till or Find expression.

Sense | Till | Find

Sense Sw(expr) = {On | Off}

Till Sw(expr) = {On | Off}

Find Sw(expr) = {On | Off}

!...!	Optional.  Parallel Processing statements can be added to the Jump instruction to cause I/O and other commands to execute during motion.

SYNC	Reserves a motion command. The robot will not move until SyncRobots is executed.

## Description
Moves the arm from the current position to the destination point with 3D gate motion.  3D gate motion consists of depart motion, span motion, and approach motion.  The depart motion form the current position to the depart point is always CP motion.  The span motion from the depart point to the start approach point is PTP motion.

The depart point is a point moved from the current position with TLZ amount in the Z direction.

The robot posture at the depart point is same as the current position.  (Posture may change if the robot passes the singularity or singularity neighborhood.)

The approach point is a point moved from the depart point in X and Y direction of the Tool coordinate system with move amount to approach to the destination point.  The U, V, and W coordinates and the robot posture at the depart point and are the same as the current position.    (Posture may change if the robot passes the singularity or singularity neighborhood)

Arch motion is achieved by specifying the arch number.  For arch motion to occur, the Depart distance must be greateer than the arch upward distance and the Approach distance must be greater than the arch downward distance.

## Notes
LimZ does not affect JumpTLZ

LimZ has no affect on JumpTLZ since the span motion is not necessarily perpendicular to the Z axis of the coordinate system.

JumpTLZ span motion is PTP (point to point)

It is difficult to predict JumpTLZ span motion trajectory.  Therefore, be careful that the robot doesn't collide with peripheral equipment and that robot arms don't collide with the robot.

Difference between JumpTLZ and Jump3

JumpTLZ and Jump3 are different in the following points.

JumpTLZ:

  The depart point must be in the Z direction from the current position.

  The approach point must be in the Z direction from the distimation point.  Also, the approach distance cannot be specified.

  Different Tool coordinate systems cannot be selected for the depart, approach, and distination points.

  (It is not possible to execute the depart motion in Tool1, and execute the approach motion in Tool2.)

Jump3:

  The depart point can be anywhere.

  The approach point can be anywhere.

  Different Tool coordinate systems can be selected for the depart, approach, and distination points.

  (It is possible to execute the depart motion in Tool1, and execute the approach motion in Tool2.)

Applicable manipulators

  JumpTLZ is only available for N series.

Caution for Arch motion

Jump3 motion trajectory is comprised of depart, span, and approach motions.  It is not a continuous path trajectory.  The actual Jump3 trajectory of arch motion is not determined by Arch parameters alone.  It also depends on motion and speed.

Always use care when optimizing Jump3 trajectory in your applications.  Execute Jump3 with the desired motion and speed to verify the actual trajectory.

When speed is lower, the trajectory will be lower.  If Jump3 is executed with high speed to verify an arch motion trajectory, the end effector may crash into an obstacle with lower speed.

In a Jump3 trajectory, the depart distance increases and the approach distance decreases when the motion speed is set high. When the approach distance of the trajectory is shorter than the expected, lower the speed and/or the deceleration, or change the approach distance to be larger.

Even if Jump commands with the same distance and speed are executed, the trajectory is affected by motion of the robot arms.

Potential acceleration errors

An acceleration error may occur during an arch motion execution by the Jump3 andJump3CP commands.  This error is issued frequently when the majority of the motion during depart or approach uses the same joint as the span motion.  To avoid this error, reduce the acceleration/deceleration speed of the span motion using Accel command for Jump3 or using Accels command for Jump3CP.  Depending on the motion and orientation of the robot, it may also help to reduce the acceleration and deceleration of the depart motion (approach motion) using the Accels command.

## Examples
```spel
JumpTLZ  P0, -100
```

## See Also
Accel, Arc, Arc3, Arch, Go, JS, JT, Point Expression, Pulse, Sense, Speed, Stat, Till

JumpTLZ Example

Move 100 mm upward from the current point in Z direction of the Tool coordinate sytem.  Then, move to the target point (P0):

JumpTLZ  P0, -100


---

# LJM Function
**Type:** reference | **Section:** Operator

## Syntax
```
(1) LJM (Point, [ refPoint, [orientationFlag] ])
```

## Parameters
Point	Specifies point data.

refPoint	Specifies the reference point data. When this is omitted, the reference point is the current position (Here).

orientationFlag

6-axis robot	1: Converts the wrist orientation (Wrist Flag), J4Flag, J6Flag or J1Flag so that Joint #4 will be the shortest movement.  This is the default setting when "orientationFlag" is omitted.

2: Converts the J4Flag or J6Flag.

3: Converts the wrist orientation (Wrist Flag), J4Flag, J6Flag or J1Flag so that Joint #5 will be the shortest movement.

4: Converts the wrist orientation (Wrist Flag), J4Flag, J6Flag or J1Flag so that Joint #6 will be the shortest movement.

RS series	1:Converts the hand orientation (Hand Flag), J1Flag or J2Flag.  This is the default setting when "orientationFlag" is omitted.

2:Converts the hand orientation (Hand Flag), J1Flag or J2Flag.  Prevents the U axis from moving out of motion range at flag convert.

N2 series	1: Converts to the posture with minimum joint movement in priority order of Joint #1 and Joint #5.  The target postures are hand orientation (Hand Flag), elbow orientation (Elbow Flag), wrist orientation (Wrist Flag), J4Flag, and J6Flag.  The elbow orientation (Elbow Flag) is always above elbow  orientation.  This is the default setting when "orientationFlag" is omitted.

2: Converts to the posture with minimum joint movement in priority order of Joint #1 and Joint #4.  The target postures are hand orientation (Hand Flag), elbow orientation (Elbow Flag), wrist orientation (Wrist Flag), J4Flag, and J6Flag.  The elbow orientation (Elbow Flag) is always above elbow  orientation.

3: Converts the wrist orientation (Wrist Flag), J4Flag, and J6Flag so that Joint #4 will be the shortest movement.

4: Converts the J4Flag and J6Flag.

5: Change the hand orientation specified by "refPoint" to different hand orientation (Hand Flag).  Converts the wrist orientation (Wrist Flag), J4Flag, J6Flag or J1Flag so that Joint #5 will be the shortest movement.  The target postures are hand orientation (Hand Flag), elbow orientation (Elbow Flag), wrist orientation (Wrist Flag), J4Flag, and J6Flag.  The elbow orientation (Elbow Flag) is always above elbow orientation.

6: Change the hand orientation specified by "refPoint" to different hand orientation (Hand Flag).  Converts the wrist orientation (Wrist Flag), J4Flag, J6Flag or J1Flag so that Joint #4 will be the shortest movement.  The target postures are hand orientation (Hand Flag), elbow orientation (Elbow Flag), wrist orientation (Wrist Flag), J4Flag, and J6Flag.  The elbow orientation (Elbow Flag) is always above elbow orientation.

7: Change the elbow orientation to the below elbow orientation (Elbow Flag).  To be the shortest movement, converts the wrist orientation (Wrist Flag), J4Flag, and J6Flag in priority order of Joint #1 and Joint #5.  The target postures are hand orientation (Hand Flag), elbow orientation (Elbow Flag), wrist orientation (Wrist Flag), J4Flag, and J6Flag.

8: Change the elbow orientation to the below elbow orientation (Elbow Flag).  To be the shortest movement, converts the wrist orientation (Wrist Flag), J4Flag, and J6Flag in priority order of Joint #1 and Joint #4.   The target postures are hand orientation (Hand Flag), elbow orientation (Elbow Flag), wrist orientation (Wrist Flag), J4Flag, and J6Flag.

*1: Above elbow orientation

*2: Hand orientation is different from the orientation specified by "refPoint".

*3: Below elbow orientation

N6 series

1: Converts the wrist orientation (Wrist Flag), J4Flag, and J6Flag so that Joint #4 will be the shortest movement.  This is the default setting when "orientationFlag" is omitted.

2: Converts the J4Flag and J6Flag.

3: Converts the wrist orientation (Wrist Flag), J4Flag, J6Flag or J1Flag so that Joint #5 will be the shortest movement.

4. Converts the wrist orientation (Wrist Flag), J4Flag, J6Flag or J1Flag so that Joint #6 will be the shortest movement.

## Description
When the 6-axis robot moves to a point calculated by such as pallet or relative offsets, the wrist part may rotate to an unintended direction. The point calculation above does not depend on robot models and results in motion without converting the required point flag. LJM function can be used to convert the point flag to prevent the unintended wrist rotation.

In the same way, when the RS series robot moves to a point calculated by such as pallet or relative offsets, Arm #1 may rotate to an unintended direction. LJM function can be used to convert the point flag to prevent the unintended rotation of Arm #1.

In addition, the U axis of an RS series robot may go out of motion range when the orientation flag is converted, which will cause an error. To prevent this error, the LJM function adjusts the U axis target angle so that it is inside the motion range. This is available when "2" is selected for orientationFlag.

Returns the specified point for robots other than 6-axis and RS series.

Note: The reference point omission and Parallel Processing

You cannot use both of the parallel point omission and parallel processing in one motion command like this:

Go LJM(P10) ! D10; MemOn 1 !

Be sure to change the program like this:

P999 = Here

Go LJM(P10,P999) ! D10; MemOn 1 !

Note: orientationFlag for N2 series

orientationFlag 1, 2:

To shorten the cycle time, select orientationFlag 1 or 2.

Since the posture has minimum Joint #1 movement, the cycle time can be shortest in most motion.

To reduce the Joint #5 movement, select orientationFlag 1.

To reduce the Joint #4 movement, select orientationFlag 2.

orientationFlag 3, 4:

Use these flags if you do not want to change the reference orientation, hand orientation, and elbow orientation.

Use these flages if you want to use them in a same manner as the flags for verticxal 6-axis robots.

orientationFlag 3 is same as orientationFlag 1 of the vertical 6-axis robots.

orientationFlag 4 is same as orientationFlag 2 of the vertical 6-axis robots.

orientationFlag 5, 6:

If the hand collides with peripheral walls during the operation, select orientationFlag 5 or 6.

Since the hand passes the neigbhorhood of the robot's origin point, the robot can move with less possibility to collide with the obstacles.

To reduce the Joint #5 movement, select orientationFlag 5.

To reduce the Joint #4 movement, select orientationFlag 6.

orientationFlag 7, 8:

To have a below elbow orientation, select orientationFlag 7 or 8.

Depending on motion, the robot passes the neighborhood of the origin like orientationFlag 5 and orientationFlag 6.  Therefore, the robot can move with less possibility to collide with the obstacles, if these are located around the robot.

To reduce the Joint #5 movement, select orientationFlag 7.

To reduce the Joint #4 movement, select orientationFlag 8.

localNumber

Local numbers of the points returned by LJM function are the same as that of "Point Expression".

## Examples
```spel
Go LJM(P10) ! D10; MemOn 1 !
```

```spel
P999 = Here
```

```spel
Go LJM(P10,P999) ! D10; MemOn 1 !
```

```spel
Function main Integer i, j P0 = XY(300, 300, 300, 90, 0, 180) P1 = XY(400, 0, 150, 90, 0, 180) P2 = XY(400, 500, 150, 90, 0, 180) P3 = XY(-400, 0, 150, 90, 0, 180) Pallet 1, P1, P2, P3, 10, 10 Motor On Power High Speed 50; Accel 50, 50 SpeedS 1000; AccelS 5000 Go P0 P11 = P0 - TLZ(50)
    For i = 1 To 10
      For j = 1 To 10
      'Specify points
         P10 = P11               'Depart point
         P12 = Pallet(1, i, j)   'Target point
         P11 = P12 -TLZ(50)      'Start approach point
         ' Converting each point to LJM
         P10 = LJM(P10)
         P11 = LJM(P11, P10)
         P12 = LJM(P12, P11)
         'Execute motion
         Jump3 P10, P11, P12 C0
       Next
      Next
Fend
Function main2 P0 = XY(300, 300, 300, 90, 0, 180) P1 = XY(400, 0, 150, 90, 0, 180) P2 = XY(400, 500, 150, 90, 0, 180) P3 = XY(-400, 0, 150, 90, 0, 180) Pallet 1, P1, P2, P3, 10, 10 Motor On Power High Speed 50; Accel 50, 50 SpeedS 1000; AccelS 5000 Go P0 Do
    ' Specify points
    P10 = Here -TLZ(50)                                'Depart point
    P12 = Pallet(1, Int(Rnd(9)) + 1, Int(Rnd(9)) + 1)   'Target point
    P11 = P12 -TLZ(50)                                  'Start approach point
    If TargetOK(P11) And TargetOK(P12) Then             'Point check
    ' Converting each point to LJM
    P10 = LJM(P10)
    P11 = LJM(P11, P10)
    P12 = LJM(P12, P11)
    ' Execute motion
      Jump3 P10, P11, P12 C0
    EndIf Loop
Fend
```

## See Also
Returns the point data with the orientation flags converted to enable least joint motion when moving to a specified point based on the reference point.

Pallet

LJM Function Example

Function main

  Integer i, j

  P0 = XY(300, 300, 300, 90, 0, 180)

  P1 = XY(400, 0, 150, 90, 0, 180)

  P2 = XY(400, 500, 150, 90, 0, 180)

  P3 = XY(-400, 0, 150, 90, 0, 180)

  Pallet 1, P1, P2, P3, 10, 10

  Motor On

  Power High

  Speed 50; Accel 50, 50

  SpeedS 1000; AccelS 5000

  Go P0

  P11 = P0 - TLZ(50)

    For i = 1 To 10

      For j = 1 To 10

      'Specify points

         P10 = P11               'Depart point

         P12 = Pallet(1, i, j)   'Target point

         P11 = P12 -TLZ(50)      'Start approach point

         ' Converting each point to LJM

         P10 = LJM(P10)

         P11 = LJM(P11, P10)

         P12 = LJM(P12, P11)

         'Execute motion

         Jump3 P10, P11, P12 C0

       Next

      Next

Fend

Function main2

  P0 = XY(300, 300, 300, 90, 0, 180)

  P1 = XY(400, 0, 150, 90, 0, 180)

  P2 = XY(400, 500, 150, 90, 0, 180)

  P3 = XY(-400, 0, 150, 90, 0, 180)

  Pallet 1, P1, P2, P3, 10, 10

  Motor On

  Power High

  Speed 50; Accel 50, 50

  SpeedS 1000; AccelS 5000

  Go P0

  Do

    ' Specify points

    P10 = Here -TLZ(50)                                'Depart point

    P12 = Pallet(1, Int(Rnd(9)) + 1, Int(Rnd(9)) + 1)   'Target point

    P11 = P12 -TLZ(50)                                  'Start approach point

    If TargetOK(P11) And TargetOK(P12) Then             'Point check

    ' Converting each point to LJM

    P10 = LJM(P10)

    P11 = LJM(P11, P10)

    P12 = LJM(P12, P11)

    ' Execute motion

      Jump3 P10, P11, P12 C0

    EndIf

  Loop

Fend


---

# LSet$ Function
**Type:** reference | **Section:** Operator

## Syntax
```
LSet$
			(string, length)
```

## Parameters
string	String expression.

length	Integer expression for the total length of the string returned.

## Description
LSet$ Function

LSet$ Function

## Examples
```spel
temp$ = "123"
		temp$ = LSet$(temp$, 10)  ' temp$ = "123       "
```

## See Also
Returns the specified string with trailing spaces appended up to the specified length.

Space$

RSet$

LSet$ Function Example

temp$ = "123"

		temp$ = LSet$(temp$, 10)  ' temp$ = "123       "


---

# LShift Function
**Type:** reference | **Section:** Operator

## Syntax
```
LShift (number, shiftBits)
```

## Parameters
number	Integer expression to be shifted.

shiftBits	The number of bits (integer from 0 to 31) to shift number to the left.

## Description
LShift shifts the specified numeric data (number) to the left (toward a higher order digit) by the specified number of bits (shiftBits).  The low order bits shifted are replaced by 0.

The simplest explanation for LShift is that it simply returns the result of number * 2shiftBits.

Note

Numeric Data Type:

The numeric data (number) may be any valid numeric data type. LShift works with data types: Byte, Double, Int32, Integer, Long, Real, Short, UByte, UInt32, and UShort.

## Examples
```spel
Function lshiftst Integer i Integer num, snum num = 1 For i = 1 to 10
    Print "i =", i
    snum = LShift(num, i)
    Print "The shifted num is ", snum Next i
Fend
```

```spel
> Print LShift (2,2)
```

```spel
8
```

```spel
> Print LShift (5,1)
```

```spel
10
```

```spel
> Print LShift (3,2)
```

```spel
12
```

```spel
>
```

## See Also
And

Not

Or

RShift

Xor

LShift Function Example

Function lshiftst

  Integer i

  Integer num, snum

  num = 1

  For i = 1 to 10

    Print "i =", i

    snum = LShift(num, i)

    Print "The shifted num is ", snum

  Next i

Fend

Some other example results from the LShift instruction from the command window.

> Print LShift (2,2)

8

> Print LShift (5,1)

10

> Print LShift (3,2)

12

>


---

# Left$ Function
**Type:** reference | **Section:** Operator

## Syntax
```
Left$
			(string, count)
```

## Parameters
string	String expression from which the leftmost characters are copied.

count	The number of characters to copy from string
 starting with the leftmost character.

## Description
Left$ returns the leftmost number characters of a string specified by the user. Left$ can return up to as many characters as are in the character string.

## Examples
```spel
Function ParsePartData(DataIn$ As String, ByRef PartNum$ As String, ByRef PartName$ As String, ByRef PartCount As Integer)
```

```spel
Integer pos
		  String temp$

pos = Instr(DataIn$, ",")
		  PartNum$ = Left$(DataIn$, pos - 1)

DataIn$ = Right$(datain$, Len(DataIn$) - pos)
		  pos = Instr(DataIn$, ",")

PartName$ = Left$(DataIn$, pos - 1)

PartCount = Val(Right$(datain$, Len(DataIn$) - pos))

		Fend
```

```spel
> Print
				Left$
			("ABCDEFG", 2)
```

```spel
AB
```

```spel
> Print
				Left$
			("ABC", 3)
```

```spel
ABC
```

## See Also
Asc

Chr$

InStr

Len

Mid$

Right$

Space$

Str$

Val

Left$ Function Example

The example shown below shows a program which takes a part data string as its input and parses out the part number, part name, and part count.

Function ParsePartData(DataIn$ As String, ByRef PartNum$ As String, ByRef PartName$ As String, ByRef PartCount As Integer)

  Integer pos

		  String temp$

pos = Instr(DataIn$, ",")

		  PartNum$ = Left$(DataIn$, pos - 1)

DataIn$ = Right$(datain$, Len(DataIn$) - pos)

		  pos = Instr(DataIn$, ",")

PartName$ = Left$(DataIn$, pos - 1)

PartCount = Val(Right$(datain$, Len(DataIn$) - pos))

Fend

Some other example results from the Left$ instruction from the Command window.

> Print
				Left$
			("ABCDEFG", 2)

AB

> Print
				Left$
			("ABC", 3)

ABC


---

# Len Function
**Type:** reference | **Section:** Operator

## Syntax
```
Len
			(string)
```

## Parameters
string	String expression.

## Description
Len returns an integer number representing the number of characters in a string specified by the user.  Len will return values between 0-255 (since a string can contain between 0-255 characters).

## Examples
```spel
Function ParsePartData(DataIn$ As String, ByRef PartNum$ As String, ByRef PartName$ As String, ByRef PartCount As Integer)

Integer pos
			  String temp$

pos = Instr(DataIn$, ",")
			  PartNum$ = Left$(DataIn$, pos - 1)

DataIn$ = Right$(datain$, Len(DataIn$) - pos)

			  pos = Instr(DataIn$, ",")

PartName$ = Left$(DataIn$, pos - 1)

		  PartCount = Val(Right$(datain$, Len(DataIn$) - pos))
		Fend
```

```spel
> ? len("ABCDEFG")

7

> ? len("ABC")

3

> ? len("")

0

>
```

## See Also
Asc

Chr$

InStr

Left$

Mid$

Right$

Space$

Str$

Val

Len Function Example

The example shown below shows a program which takes a part data string as its input and parses out the part number, part name, and part count.

Function ParsePartData(DataIn$ As String, ByRef PartNum$ As String, ByRef PartName$ As String, ByRef PartCount As Integer)

Integer pos

			  String temp$

pos = Instr(DataIn$, ",")

			  PartNum$ = Left$(DataIn$, pos - 1)

DataIn$ = Right$(datain$, Len(DataIn$) - pos)

pos = Instr(DataIn$, ",")

PartName$ = Left$(DataIn$, pos - 1)

PartCount = Val(Right$(datain$, Len(DataIn$) - pos))

		Fend

Some other example results from the Len instruction from the command window.

> ? len("ABCDEFG")

7

> ? len("ABC")

3

> ? len("")

0

>


---

# LimZ Function
**Type:** function | **Section:** Operator

## Syntax
```
LimZ
```

## Description
LimZ Function

LimZ Function

See_Also Example

Returns the current LimZ setting.

## Examples
```spel
Real savLimz

savLimz = LimZ

LimZ -25

Go pick

LimZ savLimZ
```

## See Also
LimZ Statement

LimZ Function Example

Real savLimz

savLimz = LimZ

LimZ -25

Go pick

LimZ savLimZ


---

# LimZ Keyword
**Type:** reference | **Section:** Operator

## Description
LimZ Keyword

LimZ Keyword

The LimZ keyword is used in these contexts:

LimZ Statement

LimZ Function


---

# LimZ Statement
**Type:** statement | **Section:** Operator

## Syntax
```
(1) LimZ
			zLimit

(2) LimZ
```

## Parameters
zLimit	A coordinate value within the movable range of the Z joint.

## Description
LimZ determines the maximum Z joint height which the arm move to when using the Jump instruction, wherein the robot arm raises on the Z joint, moves in the X-Y plane, then lowers on the Z joint.  LimZ is simply a default Z joint value used to define the Z joint ceiling position for use during motion caused by the Jump instruction.  When a specific LimZ value is not specified in the Jump instruction, the last LimZ setting is used for the Jump instruction.

Note

Resetting LimZ to 0

Restarting the controller, or executing the SFree, SLock, or Motor On commands will initialize LimZ to 0.

LimZ Value is Not Valid for Arm, Tool, or Local Coordinates:

LimZ Z joint height limit specification is the Z joint value for the robot coordinate system.  It is not the Z joint value for Arm, Tool, or Local coordinates.  Therefore take the necessary precautions when using tools or end effectors with different operating heights.

LimZ does not affect Jump3 and Jump3CP

LimZ has no affect on Jump3 or Jump3CP since the span motion is not necessarily perpendicular to the Z axis of the coordinate system.

## Examples
```spel
Function main

			  LimZ -10            'Set the default LimZ value
		  Jump P1             'Move up to Z=-10 position for Jump
		  Jump P2 LimZ -20    'Move up to Z=-20 position for Jump
		  Jump P3             'Move up to Z=-10 position for Jump
		Fend
```

## See Also
LimZ Function

Jump

LimZ Statement Example

The example below shows the use of LimZ in Jump operations.

Function main

LimZ -10            'Set the default LimZ value

		  Jump P1             'Move up to Z=-10 position for Jump

		  Jump P2 LimZ -20    'Move up to Z=-20 position for Jump

		  Jump P3             'Move up to Z=-10 position for Jump

		Fend


---

# LimitTorque Function
**Type:** function | **Section:** Operator

## Syntax
```
LimitTorque(jointNumber)
```

## Parameters
jointNumber	Integer expression ranging from 1 to 9.

Additional S axis is 8, and T axis is 9.

## Description
LimitTorque Function

LimitTorque Function

## Examples
```spel
Print LimitTorque(1) 'Displays the LimitTorque value of Joint #1.
```

## See Also
Returns the setting value of LimitTorque command.

LimitTorque Statement

LimitTorque Function Example

Print LimitTorque(1) 'Displays the LimitTorque value of Joint #1.


---

# LimitTorque Statement
**Type:** statement | **Section:** Operator

## Syntax
```
(1) LimitTorque AllMax

(2) LimitTorque j1Max, j2Max, j3Max, j4Max

(3) LimitTorque j1Max, j2Max, j3Max, j4Max, j5Max, j6Max

(4) LimitTorque
```

## Parameters
AllMax	specify the percentage of high power torque upper limit value for all axes to the maximum momentary torque of each axis by an integer number

j #n Max	specify the percentage of high power torque upper limit  value for axis #n to the maximum momentary torque of axis #n by an integer number

## Description
Sets the upper limit value of torque in high power mode.  Normally, the maximum torque is set and there is no need to change this setting value.  This statement is useful to restrict the torque not to exceed which is necessary for the specific motion in order to reduce damage to the manipulator and equipment caused by collision with peripherals.

The upper limit value is a peak torque in specific motion measured by PTRQ with allowance considering the variation added (approximately 10%).

The torque lower than the upper limit for Low power mode cannot be set by this command.  The smallest values vary for models and joints.  Display the setting value and confirm the actual upper limit value after setting the value.

Note

Too low LimitTorque setting

LimitTorque limits the torque for the specific motion as the upper limit value to operate the manipulator with the set acceleration/deceleration regardless of the torque size necessary for the motion.  As a result of this, if the motion requires larger torque than the set upper limit value, the roobt may not be able to operate properly and cause vibrational motion, noise, or position deviation and overrun.  Make sure to measure PTRQ before using the torque control.  If the above problems occur, set the upper limit value larger and adjust the value so that the manipulator can operate properly.

## Examples
```spel
Function main Motor On Power high Speed 100; Accel 100, 100 LimitTorque 80,100,100,100   ' Restricts the maximum torque of Joint #1 to 80% Jump P1  ' Executes the Jump motion
Fend
```

## See Also
Sets / returns the upper torque value in High power mode.

LimitTorque Function

Power

PTrq

RealTorque

LimitTorque Statement Example

Following is the example which operates the manipulator with the maximum torque of Joint #1 at 80 %.

Function main
 Motor On
 Power high
 Speed 100; Accel 100, 100
 LimitTorque 80,100,100,100   ' Restricts the maximum torque of Joint #1 to 80%
 Jump P1  ' Executes the Jump motion

Fend


---

# Line Input # Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Line Input # portNumber, stringVar$
```

## Parameters
portNumber	The communications handle or the device ID.  Communication handles can be specified in OpenCom (RS-232C) and OpenNet (TCP/IP) statements.

Device ID integers are as follows.

21 RC+

23 OP

24 TP (TP1 only)

20 TP3

stringVar$	A string variable. (string variables must end with a $ character.)

## Description
Line Input # reads string data of one line from the device specified with the handle parameter, and assigns the data to the string variable stringVar$.

## Examples
```spel
Function lintest String a$ Print #1, "Please input string to be sent to robot" Line Input #1, a$ Print "Value entered = ", a$
Fend
```

## See Also
Input

Input #

Line Input

Line Input # Statement Example

This example receives the string data from the communication port number 1, and assigns the data to the string variable A$.

Function lintest

  String a$

  Print #1, "Please input string to be sent to robot"

  Line Input #1, a$

  Print "Value entered = ", a$

Fend


---

# Line Input Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Line Input stringVar$
```

## Parameters
stringVar$	A string variable
		 name. (the string variable must end with the $ character.)

## Description
Line Input reads input data of one line from the display device and assigns the data to the string variable used in the Line Input instruction.  When the Line Input instruction is ready to receive data from the user, it causes a "?" prompt to be displayed on the display device.  The input data line after the prompt is then received as the value for the string variable.  After inputting the line of data press the [ENTER] key.

## Examples
```spel
Function Main String A$ Line Input A$ 'Read one line input data into A$ Print A$
Fend
```

```spel
Run the program above using the F5 key or Run menu from Epson RC+ main screen. A resulting run session may be as follows:
```

```spel
?A, B, C
```

```spel
A, B, C
```

## See Also
Input

Input #

Line Input#

Line Input Statement


---

# Linear Motion
**Type:** reference | **Section:** Operator

## Description
Linear Motion

Linear motion

Linear motion commands move the tool center point of robot from its current position to a specified point in a straight line. Liner motion is a CP (Continuous Path) motion.

To set velocity (speed) for straight motion, use the SpeedS command. To set acceleration and deceleration, use the AccelS command.

Command	Description

Move	Move in a
		 straight line to the specified point.

TMove	Move in a
		 straight line to the specified point in a tool coordinate system.

Jump3CP	Jump to a
		 point in 3 dimensions using CP motion. Move in a straight line
		 until the recede point. The motion between the recede points is
		 also a straight line motion.

BMove	Move in a
		 straight line to the relative specified point in Base / Local
		 coordinate system


---

# Local Function
**Type:** function | **Section:** Operator

## Syntax
```
Local(localNumber)
```

## Parameters
localNumber	Local coordinate system number (integer from 1 to 15) using an expression or numeric value.

## Description
Local Function

Local Function

See_Also Example

Returns the specified local coordinate system data as a point.

## Examples
```spel
P1 = Local (1)
```

## See Also
Local Statement

Local Function Example

P1 = Local (1)


---

# Local Keyword
**Type:** reference | **Section:** Operator

## Description
Local Keyword

Local Keyword

The Local keyword is used in these contexts:

Local Statement

Local Function


---

# Local Statement
**Type:** statement | **Section:** Operator

## Syntax
```
(1) Local localNumber , ( pLocal1 : pBase1 ) , ( pLocal2 : pBase2 ), [ { L | R } ], [ BaseU ]

(2) Local localNumber, pCoordinateData

(3) Local localNumber, pOrigin,  [pXaxis], [pYaxis], [ { X | Y } ]

(4) Local localNumber
```

## Parameters
localNumber	The local coordinate system number. A total of 15 local coordinate systems (of the integer value from 1 to 15) may be defined.

pLocal1, pLocal2	Point variables with point data in the local coordinate system.

pBase1, pBase2	Point variables with point data in the base coordinate system.

L | R	Optional. Align local origin to left (first) or right (second) base points.

BaseU	Optional. When supplied, U axis coordinates are in the base coordinate system. When omitted, U axis coordinates are in the local coordinate system.

X	Local coordinate system X axis origin.

Y	Local coordinate system Y axis origin.

Z	Local coordinate system Z axis origin.

U	Local coordinate system rotation angle about the Z axis.

V	Optional.  Local coordinate system rotation angle about the Y axis.

W	Optional.  Local coordinate system rotation angle about the X axis.

pCoordinateData	Point data representing the coordinate data of the origin and direction.

When it's SCARA Robots (include RS series), specify V coordinate and W coordinate to "0".

pOrigin	Integer expression representing the origin point using robot coordinate system.

pXaxis	Optional. Integer expression representing a point along the X axis using robot coordinate system if X alignment is specified.

pYaxis	Optional. Integer expression representing a point along the Y axis using robot coordinate system if Y alignment is specified.

X | Y	Optional.  If X alignment is specified, then pXaxis is on the X axis of the local and only the Z coordinate of pYaxis is used.  If Y alignment is specified, then pYaxis is on the Y axis of the local and only the Z coordinate of pXaxis is used.  If ommitted, X alignment is assumed.

## Description
(1) Local defines a local coordinate system by specifying 2 points, pLocal1 and pLocal2, contained in it that coincide with two points, pBase1 and pBase2, contained in the base coordinate system.

## Examples
```spel
Local 1, (P1:P11), (P2:P12)
```

```spel
Local 1, XY(x, y, z, u)
Local 1, XY(x, y, z, u, v, w)
Local 1, P1
```

```spel
Local 1, P1, P2, P3
Local 1, P1, P2, P3, X
Local 1, P1, P2, P3, Y
```

```spel
> p1 = 0, 0, 0, 0/1
```

```spel
> p2 = 100, 0, 0, 0/1
```

```spel
> p11 = 150, 150, 0, 0
```

```spel
> p12 = 300, 150, 0, 0
```

```spel
> local 1, (P1:P11), (P2:P12), L
```

```spel
> p21 = 50, 0, 0, 0/1
```

```spel
> go p21
```

```spel
Local defined with only the origin point:
```

```spel
> local 1, 100, 200, -20, 0
```

```spel
Local defined with only the origin point rotated 45 degrees about the X axis:
```

```spel
> local 2, 50, 200, 0, 0, 45, 0
```

```spel
3D Local with p2 aligned with the X axis of the local:
```

```spel
> local 3, p1, p2, p3, x
```

```spel
3D Local with p3 aligned with the Y axis of the local:
```

```spel
> local 4, p1, p2, p3, y
```

## See Also
Armset

Base

LocalClr

TLSet

Where

Local Statement Example

Here are some examples from the command window:

Left aligned local:

> p1 = 0, 0, 0, 0/1

> p2 = 100, 0, 0, 0/1

> p11 = 150, 150, 0, 0

> p12 = 300, 150, 0, 0

> local 1, (P1:P11), (P2:P12), L

> p21 = 50, 0, 0, 0/1

> go p21

Local defined with only the origin point:

> local 1, 100, 200, -20, 0

Local defined with only the origin point rotated 45 degrees about the X axis:

> local 2, 50, 200, 0, 0, 45, 0

3D Local with p2 aligned with the X axis of the local:

> local 3, p1, p2, p3, x

3D Local with p3 aligned with the Y axis of the local:

> local 4, p1, p2, p3, y


---

# LocalClr Statement
**Type:** statement | **Section:** Operator

## Syntax
```
LocalClr localNumber
```

## Parameters
localNumber	Integer expression representing which of 15 locals (integer from 1 to 15) to clear (undefine).

## Description
Robot parameter data is stored in compact flash in controller.  Therefore, writing to command flash occurs when executing this command.  Frequent writing to compact flash affect to lifetime of compact flash.  We recommend to use this command minimally.

## Examples
```spel
LocalClr 1
```

## See Also
Clears (undefines) a local coordinate system.

Arm

Armset

Local

Tool

TLClr

TLSet

LocalClr Example

LocalClr 1


---

# Locals page, Robot Manager Window
**Type:** reference | **Section:** Operator

## Description
Locals page, Robot Manager Window

[Tools]-[Robot Manager]-[Locals] Page

This page allows you to define local coordinate systems for a robot. When the tab is selected, the values of all local tools you can define are displayed. A grid is used to display all of the values for the locals you can define. Local "0" is the base coordinate system and cannot be changed from this page.

To change the base coordinate system, use the Base command from the command window.

For more details, refer to the following manual:

SPEL+ Language Reference

When a local is undefined, then all fields for that local will be blank. When you enter a value in any of the fields for an undefined local, then the remaining fields will be set to zero.

Click the [Apply] button to define the local coordinate system.

For more details on local settings, refer to the following manual:

SPEL+ Language Reference - Local Statement

Navigating the grid

Press the [Tab] key to move to the next cell. Press the [Shift] + [Tab] key to move to the previous cell. Press the arrow [↑] or [↓] key to move to the cell above or below.

Item	Description

Local
		 Wizard	Click
		 this button to start the Local Wizard.

		Follow the instructions for each step to define a local. See details
		 in the next section.

X	The X
		 coordinate of the local origin in the base coordinate system.

Y	The Y
		 coordinate of the local origin in the base coordinate system.

Z	The Z
		 coordinate of the local origin in the base coordinate system.

Item	Description

U	Rotation
		 angle of the local about the base Z axis. (roll)

V	Rotation
		 angle of the local about the base Y axis. (pitch)

W	Rotation
		 angle of the local about the base X axis. (yaw)

Apply	Sets
		 the current values.

Restore	Reverts
		 to the previous values.

Clear	Clears
		 all selected values.

Using the Local Wizard

A wizard is provided for defining a local coordinate system. You can define a local using a single point or three points, as described in the following sections. This section describes the procedure used when selecting [Manually define the local using jog & teach]. For details of the Local setting, refer to 7. Vision Calibration in the Vision Guide 8.0 Software manual.

Using the Local Wizard to teach a single point local

(1)    Open the [Robot Manager] and click on [Locals] to show the [Locals] page.

(2)    Select [Manually define the local using jog & teach], and then click the [Local Wizard] button. The following dialog appears.

(3)    Select the local number you want to define.

For [How many points will be used], select [1 - Origin]. Since this is a single point local, you will just teach the origin of the new coordinate system. If you want to use the U, V, or W axes for the orientation of the coordinate system, check the [Use U, V, W tool coordinates for local rotation] checkbox. If this checkbox is unchecked, the new coordinate system is offset from local 0 in X and Y, but is not rotated about any axis.

Click the [Next] button.

(4)    Teach the local origin point.

Click the [Teach] button to open the [Local Wizard Teach Point] dialog box.

(5)    Jog the robot until the end effector is aligned with the local origin point.

Click the [Teach] button.

(6)    The new local definition is displayed as shown below.

Click the [Finish] button to accept the new definition.

Using the Local Wizard to teach a three point local

(1)    Open the [Robot Manager] and click on [Locals] to show the [Locals] page.

(2)    Select [Manually define the local using jog & teach], and then click the [Local Wizard] button. The following dialog appears.

(3)          Select the local number you want to define.

For [How many points will be used], select [3 - Origin, X, Y]. Since this is a three point local, you will teach the origin of the new coordinate system, and then teach one point anywhere along the X axis and one point anywhere along the Y axis. Select which axis will be used to align the coordinate system. For example, if you select X, then the new coordinate system X axis will be aligned to the X axis point that you will teach in a later step. The Y axis point will be used to determine tilt. Click the [Next] button.

(4)    Teach the local origin point.

Click the [Teach] button to open the [Local Wizard: Teach Point] dialog box.

(5)    Jog the robot until the end effector is aligned with the origin point.

Click the [Teach] button. The following dialog will appear.

(6)    Teach a point on the local X axis.

Click the [Teach] button and jog the robot until the end effector is aligned with a point anywhere along the X axis of the new coordinate system. Click the [Teach] button on the [Teach Point] dialog box to continue.

(7)    Teach a point on the local Y axis.

Click the [Teach] button and jog the robot until the end effector is aligned with a point anywhere along the Y axis of the new coordinate system. Click the [Teach] button on the [Local Wizard Teach Point] dialog box to continue.

(8)    The new local definition is displayed as shown below.

Click the [Finish] button to accept the new definition.


---

# Long Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Long varName [( subscripts )] [, varName [( subscripts )]...
```

## Parameters
varName	Variable name which the user wants to declare as type Long.

subscripts	Optional.  Dimensions of an array variable; up to 3 dimensions may be declared.  The subscripts syntax is as follows

(ubound1, [ubound2], [ubound3])

ubound1, ubound2, ubound3 each specify the maximum upper bound for the associated dimension.

The elements in each dimension of an array are numbered from 0 and the available number of array elements is the upper bound value + 1.

When specifying the upper bound value, make sure the number of total elements is within the range shown below:

Local variable  2000

Global Preserve variable  4000

Global variable and module variable  100000

## Description
Long is used to declare variables as type Long.  Variables of type Long can contain whole numbers with values between -2,147,483,648 to 2,147,483,647.  Local variables should be declared at the top of a function.  Global and module variables must be declared outside of functions.

## Examples
```spel
Function longtest Long A(10) 'Single dimension array of long Long B(10, 10) 'Two dimension array of long Long C(5, 5, 5) 'Three dimension array of long Long var1, arrayVar(10) Long i Print "Please enter an Long Number" Input var1 Print "The Long variable var1 = ", var1 For i = 1 To 5
    Print "Please enter an Long Number"
    Input arrayVar(i)
    Print "Value Entered was ", arrayVar(i) Next i
```

```spel
Fend
```

## See Also
Boolean

Data Types Overview

Variable Declarations

Variable Naming Conventions

Byte

Double

Global

Int32

Integer

Real

Short

String

UByte

UInt32

UShort

Long Statement Example

The following example shows a simple program which declares some variables as Longs using Long.

Function longtest

  Long A(10) 'Single dimension array of long

  Long B(10, 10) 'Two dimension array of long

  Long C(5, 5, 5) 'Three dimension array of long

  Long var1, arrayVar(10)

  Long i

  Print "Please enter an Long Number"

  Input var1

  Print "The Long variable var1 = ", var1

  For i = 1 To 5

    Print "Please enter an Long Number"

    Input arrayVar(i)

    Print "Value Entered was ", arrayVar(i)

  Next i

Fend


---

# MemIn Function
**Type:** function | **Section:** Operator

## Syntax
```
MemIn ( portNumber )
```

## Parameters
portNumber	Integer expression representing the memory I/O byte number.

## Description
Returns an integer value between 0 and 255.  The return value is 8 bits, with each bit corresponding to 1 memory I/O bit.

MemIn provides the ability to look at the value of 8 memory I/O bits at the same time.  The MemIn instruction can be used to store the 8 memory I/O bit status into a variable or it can be used with the Wait instruction to Wait until a specific condition which involves more than 1 memory I/O bit is met.

Since 8 bits are retrieved at a time, the return value ranges from 0 and 255.  Please review the chart below to see how the integer return values correspond to individual memory I/O bits.

Memory I/O Bit Result (Using Port #0)

## Notes
Difference Between MemIn and MemSw

The MemSw instruction allows the user to read the value of 1 memory I/O bit.  The return value from MemSw is either a 1 or a 0 which indicates that the memory I/O bit is either On or Off.  MemSw can check each of the memory I/O bits individually.  The MemIn instruction is very similar to the MemSw instruction in that it also is used to check the status of the memory I/O bits.  However there is 1 distinct difference.  The MemIn instruction checks 8 memory I/O bits at a time vs. the single bit checking functionality of the MemSw instruction. MemIn returns a value between 0 and 255 which tells the user which of the 8 I/O bits are On and which are Off.

## Examples
```spel
Function main Integer var1 var1 = MemIn(0)  'Get the 1st 8 memory I/O bit values If var1 = 0 Then
    Go P1
    Go P2 Else
    Print "Error in initialization!"
    Print "First 8 memory I/O bits were not all set to 0" EndIf
Fend
```

```spel
> memout 0, 1
```

```spel
> print MemIn(0)
```

```spel
1
```

```spel
> memon 1
```

```spel
> print MemIn(0)
```

```spel
3
```

```spel
> memout 31,3
```

```spel
> print MemIn(31)
```

```spel
3
```

```spel
> memoff 249
```

```spel
> print MemIn(31)
```

```spel
1
```

```spel
>
```

## See Also
In, InBCD, Off, MemOff, On, MemOn, OpBCD, Oport, Out, Sw, MemSw, Wait

MemIn Function Example

The program example below gets the current value of the first 8 memory I/O bits and then makes sure that all 8 I/O are currently set to 0 before proceeding.  If they are not 0 an error message is given to the operator and the task is stopped.

Function main

  Integer var1

  var1 = MemIn(0)  'Get the 1st 8 memory I/O bit values

  If var1 = 0 Then

    Go P1

    Go P2

  Else

    Print "Error in initialization!"

    Print "First 8 memory I/O bits were not all set to 0"

  EndIf

Fend

Other simple examples from the command window are as follows:

> memout 0, 1

> print MemIn(0)

1

> memon 1

> print MemIn(0)

3

> memout 31,3

> print MemIn(31)

3

> memoff 249

> print MemIn(31)

1

>


---

# MemOff Statement
**Type:** reference | **Section:** Operator

## Syntax
```
MemOff { bitNumber | memIOLabel }
```

## Parameters
bitNumber	Integer expression
		 representing the memory I/O bit number.

memIOLabel	Memory I/O label.

## Description
MemOff turns Off the specified bit of the robot memory I/O.  The 256 memory I/O bits are typically excellent choices for use as status bits for uses such as On/Off, True/False, Done/Not Done, etc.  The MemOn instruction turns the memory bit On, the MemOff instruction turns it Off, and the MemSw instruction is used to check the current state of the specified memory bit.  The Wait instruction can also be used with the memory I/O bit to cause the system to wait until a specified memory I/O status is set.

Note:  All memory I/O bits are turned off when the controller is restarted.  They are not turned off by Emergency stop, safeguard open, program end, Reset command, or Epson RC+ restart.

## Examples
```spel
Function main Integer i MemOff 1 Xqt 2, task2 For i = 1 to 100
    Wait MemSw(1) = Off
    Go P(i)
    MemOn 1 Next i
Fend
```

```spel
Function task2 Integer i For i = 101 to 200
    Wait MemSw(1) = On
    Go P(i)
    MemOff 1 Next i
Fend
```

```spel
> MemOn 1  'Switch memory I/O bit #1 on
```

```spel
> Print MemSw(1)
```

```spel
1
```

```spel
> MemOff 1 'Switch memory I/O bit #1 off
```

```spel
> Print MemSw(1)
```

```spel
0
```

## See Also
Turns Off the specified bit of the memory I/O.

In, MemIn, InBCD, Off, On, MemOn, OpBCD, Oport, Out, MemOut, Sw, MemSW, Wait

MemOff Example

The example shown below shows 2 tasks each with the ability to initiate motion instructions. However, a locking mechanism is used between the 2 tasks to ensure that each task gains control of the robot motion instructions only after the other task is finished using them. This allows 2 tasks to each execute motion statements as required and in an orderly predictable fashion. MemSw is used in combination with the Wait instruction to wait until the memory I/O #1 is the proper value before it is safe to move again. MemOn and MemOff are used to turn On and turn Off the memory I/O for proper synchronization.

Function main

  Integer i

  MemOff 1

  Xqt 2, task2

  For i = 1 to 100

    Wait MemSw(1) = Off

    Go P(i)

    MemOn 1

  Next i

Fend

Function task2

  Integer i

  For i = 101 to 200

    Wait MemSw(1) = On

    Go P(i)

    MemOff 1

  Next i

Fend

Other simple examples from the command window are as follows:

> MemOn 1  'Switch memory I/O bit #1 on

> Print MemSw(1)

1

> MemOff 1 'Switch memory I/O bit #1 off

> Print MemSw(1)

0


---

# MemOn Statement
**Type:** reference | **Section:** Operator

## Syntax
```
MemOn { bitNumber | memIOLabel }
```

## Parameters
bitNumber	Integer expression
		 representing the memory I/O bit number.

memIOLabel	Memory I/O
		 label.

## Description
MemOn turns on the specified bit of the robot memory I/O.  The 256 memory I/O bits are typically used as task communication status bits.  The MemOn instruction turns the memory bit On, the MemOff instruction turns it Off, and the MemSw instruction is used to check the current state of the specified memory bit.  The Wait instruction can also be used with the memory bit to cause the system to wait until a specified status is set.

Note:  All memory I/O bits are turned off when the controller is restarted.  They are not turned off by Emergency stop, safeguard open, program end, Reset command, or Epson RC+ restart.

## Examples
```spel
Function main Integer i MemOff 1 Xqt 2, task2 For i = 1 to 100
    Wait MemSw(1) = Off
    Go P(i)

    MemOn 1 Next i
Fend
```

```spel
Function task2 Integer i For i = 101 to 200
    Wait MemSw(1) = On
    Go P(i)
    MemOff 1 Next i
Fend
```

```spel
> memon 1
```

```spel
> print memsw(1)
```

```spel
1
```

```spel
> memoff $1
```

```spel
> print sw(1)
```

```spel
0
```

## See Also
Turns On the specified bit of the memory I/O.

In, MemIn, InBCD, Off, MemOff, On, OpBCD, Oport, Out, MemOut, Sw, MemSW, Wait

MemOn Statement Example

The example shown below shows 2 tasks each with the ability to initiate motion instructions.  However, a locking mechanism is used between the 2 tasks to ensure that each task gains control of the robot motion instructions only after the other task is finished using them.  This allows 2 tasks to each execute motion statements as required and in an orderly predictable fashion.  MemSw is used in combination with the Wait instruction to wait until the memory I/O #1 is the proper value before it is safe to move again.  MemOn and MemOff are used to turn on and turn off the memory I/O for proper synchronization.

Function main

  Integer i

  MemOff 1

  Xqt 2, task2

  For i = 1 to 100

    Wait MemSw(1) = Off

    Go P(i)

MemOn 1

  Next i

Fend

Function task2

  Integer i

  For i = 101 to 200

    Wait MemSw(1) = On

    Go P(i)

    MemOff 1

  Next i

Fend

Other simple examples from the command window are as follows:

> memon 1

> print memsw(1)

1

> memoff $1

> print sw(1)

0


---

# MemOut Statement
**Type:** reference | **Section:** Operator

## Syntax
```
MemOut portNumber, outData
```

## Parameters
Portnum	Outputs

0	0-7

1	8-15

.	.

.

outData	Integer expression between 0 and 255 representing the output pattern for the output group selected by portNumber.  If represented in hexadecimal form the range is from &H0 to &HFF.  The lower digit represents the least significant digits (or the 1st 4 outputs) and the upper digit represents the most significant digits (or the 2nd 4 outputs).

## Description
MemOut simultaneously sets 8 memory I/O bits using the combination of the portNumber and outData values specified by the user to determine which outputs will be set.  The portNumber parameter specifies which group of 8 outputs to use where portNumber = 0 means outputs 0 to 7, portNumber = 1 means outputs 8 to 15, etc.

Once a portNumber is selected (i.e. a group of 8 outputs has be selected), a specific output pattern must be defined. This is done using the outData parameter.  The outData parameter may have a value between 0 and 255 and may be represented in hexadecimal or integer format.  (i.e.  &H0 to &HFF    or    0 to 255)

The table below shows some of the possible I/O combinations and their associated outData values assuming that portNumber is 0, and 1 accordingly.

Output Settings When portNumber=0  (Output number)

OutData Value	7	6	5	4	3	2	1	0

01	Off	Off	Off	Off	Off	Off	Off	On

02	Off	Off	Off	Off	Off	Off	On	Off

03	Off	Off	Off	Off	Off	Off	On	On

08	Off	Off	Off	Off	On	Off	Off	Off

09	Off	Off	Off	Off	On	Off	Off	On

10	Off	Off	Off	On	Off	Off	Off	Off

11	Off	Off	Off	On	Off	Off	Off	On

99	Off	On	On	Off	Off	Off	On	On

255	On	On	On	On	On	On	On	On

Output Settings When portNumber=1  (Output number)

OutData Value	15	14	13	12	11	10	9	8

01	Off	Off	Off	Off	Off	Off	Off	On

02	Off	Off	Off	Off	Off	Off	On	Off

03	Off	Off	Off	Off	Off	Off	On	On

08	Off	Off	Off	Off	On	Off	Off	Off

09	Off	Off	Off	Off	On	Off	Off	On

10	Off	Off	Off	On	Off	Off	Off	Off

11	Off	Off	Off	On	Off	Off	Off	On

99	Off	On	On	Off	Off	Off	On	On

255	On	On	On	On	On	On	On	On

## Notes
Difference between Out and MemOut

It is very important for the user to understand the difference between the Out and MemOut instructions.  This difference is shown below:

- The MemOut instruction works with internal memory I/O and does not affect hardware I/O in any way.

- The Out instruction works with the hardware output ports located on the rear of the controller. These hardware ports are discrete Outputs which interact with devices external to the robot.

## Examples
```spel
Function main Xqt 2, iotask Go P1 . .
Fend
Function iotask Do
    MemOut 0, &HF
    Wait 1
    MemOut 0, &H0
    Wait 1 Loop
Fend
```

```spel
> MemOut 1,6   'Turns on memory I/O bits 9 & 10
```

```spel
> MemOut 2,1   'Turns on memory I/O bits 8
```

```spel
> MemOut 3,91  'Turns on memory I/O bits 24, 25, 27, 28, and 30
```

## See Also
In, MemIn, InBCD, MemOff, MemOn, MemSW, Off, On, OpBCD, Oport, Out, Sw, Wait

MemOut Example

The example below shows main task starting a background task called iotask.  The iotask is a simple task to toggle memory I/O bits from 0 to 3 On and Off.  The MemOut instruction makes this possible using only 1 command rather than turning each memory I/O bit on and off individually.

Function main

  Xqt 2, iotask

  Go P1

  .

  .

Fend

Function iotask

  Do

    MemOut 0, &HF

    Wait 1

    MemOut 0, &H0

    Wait 1

  Loop

Fend

Other simple examples from the command window are as follows:

> MemOut 1,6   'Turns on memory I/O bits 9 & 10

> MemOut 2,1   'Turns on memory I/O bits 8

> MemOut 3,91  'Turns on memory I/O bits 24, 25, 27, 28, and 30


---

# MemSw Function
**Type:** reference | **Section:** Operator

## Syntax
```
MemSw(bitNumber)
```

## Parameters
bitNumber	Integer expression representing memory I/O bit number.

## Description
MemSw returns the status of one memory I/O bit.  Valid entries for MemSw range from bit 0 to bit 511.  MemOn turns the specified bit on and MemOff turns the specified bit Off.

## Examples
```spel
Function main
		  Integer i
		  MemOff 1
		  Xqt 2, task2
		  For i = 1 to 100
		    Wait MemSw(1) = Off
		    Go P(i)
		    MemOn 1
		  Next i
		Fend
```

```spel
Function task2
		  Integer i
		  For i = 101 to 200
		    Wait MemSw(1) = On
		    Go P(i)
		    MemOff 1
		  Next i
		Fend
```

```spel
> memon 1
```

```spel
> print memsw(1)
```

```spel
1
```

```spel
> memoff 1
```

```spel
> print memsw(1)
```

```spel
0
```

## See Also
In, MemIn, InBCD, Off, MemOff, MemOn, MemOut, On, OpBCD, Oport, Out, Sw, Wait

MemSw Example

The example shown below shows 2 tasks each with the ability to initiate motion instructions.  However, a locking mechanism is used between the 2 tasks to ensure that each task gains control of the robot motion instructions only after the other task is finished using them.  This allows 2 tasks to each execute motion statements as required and in an orderly predictable fashion.  MemSw is used in combination with the Wait instruction to wait until the memory I/O bit 1 is the proper value before it is safe to move again.

Function main

		  Integer i

		  MemOff 1

		  Xqt 2, task2

		  For i = 1 to 100

		    Wait MemSw(1) = Off

		    Go P(i)

		    MemOn 1

		  Next i

		Fend

Function task2

		  Integer i

		  For i = 101 to 200

		    Wait MemSw(1) = On

		    Go P(i)

		    MemOff 1

		  Next i

		Fend

Other simple examples from the Command window are as follows:

> memon 1

> print memsw(1)

1

> memoff 1

> print memsw(1)

0


---

# Mid$ Function
**Type:** reference | **Section:** Operator

## Syntax
```
Mid$
			(string, position, [count])
```

## Parameters
string	Source string expression.

position	The starting position in the character string for copying count

						characters.

count	Optional.  The number of characters to copy from string starting with the character defined by position.
  If ommitted, then all characters from position to the end of the string are returned.

## Description
Mid$ returns a substring of as many as count characters starting with the position character in string.

## Examples
```spel
Function midtest
		  String basestr$, m1$, m2$
		  basestr$ = "ABCDEFGHIJ"
		  m1$ = Mid$(basestr$, (Len(basestr$) / 2), 2)
		  Print "The middle 2 characters are: ", m1$
		  m2$ = Mid$(basestr$, 5)
		  Print "The string starting at 5 is: ", m2$
		Fend
```

## See Also
Asc, Chr$, InStr, Left$, Len, Right$, Space$, Str$, Val

Mid$ Function Example

The example shown below shows a program that extracts the middle 2 characters from the string "ABCDEFGHIJ" and the remainder of the string starting at position 5.

Function midtest

		  String basestr$, m1$, m2$

		  basestr$ = "ABCDEFGHIJ"

		  m1$ = Mid$(basestr$, (Len(basestr$) / 2), 2)

		  Print "The middle 2 characters are: ", m1$

		  m2$ = Mid$(basestr$, 5)

		  Print "The string starting at 5 is: ", m2$

		Fend


---

# Mod Operator
**Type:** reference | **Section:** Operator

## Syntax
```
number
			Mod
 divisor
```

## Parameters
number	The number being divided. (the dividend)

divisor	The number which number is divided by.

## Description
Mod is used to get the remainder after dividing 2 numbers.  The remainder is a whole number. One clever use of the Mod instruction is to determine if a number is odd or even.  The method in which the Mod instruction works is as follows: number is divided by divisor.  The remainder left over after this division is then the return value for the Mod instruction.

## Examples
```spel
Function modtest
		  Integer var1, result

Print "Enter an integer number:"
		  Input var1
		  result = var1 Mod 2
		  Print "Result = ", result
		  If result = 0 Then
		    Print "Result = ", result
		    Print "The number is EVEN"
		  Else
		    Print "Result = ", result
		    Print "The number is ODD"
		  EndIf
		Fend
```

```spel
> Print 36 Mod 6
```

```spel
> 0
```

```spel
> Print 25 Mod 10
```

```spel
> 5
```

```spel
>
```

## See Also
Abs	Sgn

Atan	Sin

Atan2	Sqr

Cos	Str$

Int	Tan

Not	Val

Mod Operator Example

The example shown below determines if a number (var1) is even or odd.  When the number is even the result of the Mod instruction will return a 0.
  When the number is odd, the result of the Mod instruction will return a 1.

Function modtest

		  Integer var1, result

Print "Enter an integer number:"

		  Input var1

		  result = var1 Mod 2

		  Print "Result = ", result

		  If result = 0 Then

		    Print "Result = ", result

		    Print "The number is EVEN"

		  Else

		    Print "Result = ", result

		    Print "The number is ODD"

		  EndIf

		Fend

Some other example results from the Mod instruction from the Command window.

> Print 36 Mod 6

> 0

> Print 25 Mod 10

> 5

>


---

# Motor Function
**Type:** function | **Section:** Operator

## Syntax
```
Motor
```

## Description
Motor Function

Motor Function

See_Also Example

Returns status of motor power for the current robot.

## Examples
```spel
If Motor = Off Then
		  Motor On
		EndIf
```

## See Also
Motor Statement

Motor Function Example

If Motor = Off Then

		  Motor On

		EndIf


---

# Motor Keyword
**Type:** reference | **Section:** Operator

## Description
Motor Keyword

Motor Keyword

The Motor keyword is used in these contexts:

Motor Statement

Motor Function


---

# Motor Statement
**Type:** statement | **Section:** Operator

## Syntax
```
Motor ON | OFF
```

## Parameters
ON | OFF	The keyword ON is used to turn the Motor Power on. The keyword OFF is used to turn Motor Power Off.

## Description
The Motor On command is used to turn Motor Power On and release the brakes for all axes. Motor Off is used to turn Motor Power Off and set the brakes.

In order to move the robot, motor power must be turned on.

After an emergency stop, or after an error has occurred that requires resetting with the Reset command, execute Reset, and then execute Motor On.

Motor On sets the robot control parameter as below:

Speed, SpeedR, SpeedS	Default values

Accel, AccelR, AccelS	Default values

QPDecelR, QPDecelS	Default values

LimZ	0

CP	Off

SoftCP	Off

Fine	Default values

Power Low	Low

PTPBoost	Default values

TCLim, TCSpeed	Default values

PgLSpeed	Default values

PerformMode	Standard mode

## Examples
```spel
> Motor On

> Motor Off
```

## See Also
Motor Function

Power

Reset

SFree

SLock

Motor Statement Example

The following examples are done from the command window:

> Motor On

> Motor Off


---

# Move Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Move destination [ROT] [ECP] [CP] [searchExpr] [!...!] [SYNC]
```

## Parameters
destination	The target destination of the motion using a point expression.

ROT	Optional.  Decides the speed/acceleration/deceleration in favor of tool rotation.

ECP	Optional.  External control point motion.  This parameter is valid when the ECP option is enabled.

CP	Optional.  Specifies continuous path motion.

searchExpr	Optional. A Till or Find expression.

Till | Find

Till Sw(expr) = {On | Off}

Find Sw(expr) = {On | Off}

!...!	Optional. Parallel Processing statements can be added to execute I/O and other commands during motion.

SYNC	Reserves a motion command. The robot will not move until SyncRobots is executed.

## Description
Move moves the arm from the current position to destination in a straight line. Move coordinates all axes to start and stop at the same time.  The coordinates of destination must be taught previously before executing the Move instruction.  Acceleration and deceleration for the Move is controlled by the AccelS instruction.  Speed for the move is controlled by the SpeedS instruction. If the SpeedS speed value exceeds the allowable speed for any joint, power to all four joint motors will be turned off, and the robot will stop.

Move uses the SpeedS speed value and AccelS acceleration and deceleration values. Refer to Using Move with CP below on the relation between the speed/acceleration and the acceleration/deceleration.  If, however, the ROT modifier parameter is used, Move uses the SpeedR speed value and AccelR acceleration and deceleration values.  In this case SpeedS speed value and AccelS acceleration and deceleration value  have no effect.

Usually, when the move distance is 0 and only the tool orientation is changed, an error will occur. However, by using the ROT parameter and giving priority to the acceleration and the deceleration of the tool rotation, it is possible to move without an error. When there is not an orientational change with the ROT modifier parameter and movement distance is not 0, an error will occur.

Also, when the tool rotation is large as compared to move distance, and when the rotation speed exceeds the specified speed of the manipulator, an error will occur. In this case, please reduce the speed or append the ROT modifier parameter to give priority to the rotational speed/acceleration/deceleration.

When ECP is used, the trajectory of the external control point coresponding to the ECP number specified by ECP instruction moves straight with respect to the tool coordinate system. In this case, the trajectory of tool center point does not follow a straight line.

The optional Till qualifier allows the user to specify a condition to cause the robot to decelerate to a stop prior to completing the Move.  The condition specified is simply a check against one of the inputs.  This is accomplished through using the Sw instruction.  The user can check if the input is On or Off and cause the arm to stop based on the condition specified.  This feature works almost like an interrupt where the Move is interrupted (stopped) once the Input condition is met.  If the input condition is never met during the Move then the arm successfully arrives on the point specified by destination.  For more information about the Till qualifier see the Till command (Till).

## Notes
Move Cannot

Move cannot execute range verification of the trajectory prior to starting the move itself.  Therefore, even for target positions that are within an allowable range, it is possible for the system to find a prohibited position along the way to a target point. In this case, the arm may abruptly stop which may cause shock and a servo out condition of the arm.  To prevent this, be sure to perform range verifications at low speed prior to using Move at high speeds.  In summary, even though the target position is within the range of the arm, there are some Moves which will not work because the arm cannot physically make it to some of the intermediate positions required during the Move.

Using Move with CP

The CP parameter causes the arm to move to destination without decelerating or stopping at the point defined by destination.  This is done to allow the user to string a series of motion instructions together to cause the arm to move along a continuous path while maintaining a specific speed throughout all the motion.  The Move instruction without CP always causes the arm to decelerate to a stop prior to reaching the point destination destination.

Move with CP is equivalent to CMove on the SRC 3xx controllers.

Proper Speed and Acceleration Instructions with Move

The SpeedS and AccelS instructions are used to specify the speed and acceleration of the robot during Move motion.  Pay close attention to the fact that SpeedS and AccelS apply to linear and circular interpolated motion while point to point motion uses the Speed and Accel instructions.

Potential Errors

Attempt to Change Only Tool Orientation

Changing only tool orientation during the move is impossible.  If this is attempted, an error will occur.  In this case, use the ROT parameter.

Joint Overspeed Errors

When the motion requested results in the speed of one of the joints to exceed its maximum allowable speed an overspeed error occurs.  In the case of a motor overspeed error, the robot arm is brought to a stop and servo power is turned off.

No Motion Instruction Following Move CP Instruction

If, following Move CP, there are not any motion instructions to smoothly move the arm (since the arm has not yet decelerated) damage may occur to the arm due to excessive shock. In this case an error will occur, the arm will stop and servo power will be removed. (A Pause input during continuous path motion may cause an error also due to the fact that it tries to instantaneously stop the robot.)

## Examples
```spel
Function movetest Home Go P0 Go P1 Move P0 Move P2 Till Sw(2) = On If Sw(2) = On Then
    Print "Input #2 came on during the move and"
    Print "the robot stopped prior to arriving on"
    Print "point P2." Else
    Print "The move to P2 completed successfully."
    Print "Input #2 never came on during the move." Endif
Fend
```

```spel
Function CornerArc Go P100 Move P101 CP 'Do not stop at P101 Arc P102, P103 CP 'Do not stop at P103 Move P104 'Decelerate to stop at P104
Fend
```

## See Also
Robot motion commands

!...! Parallel Processing

AccelS

Arc

CP

Go

Jump

Jump3

Jump3CP

Point Expression

SpeedS

Sw

Till

Move Statement Example

The example shown below shows a simple point to point move between points P0 and P1 and then moves back to P0 in a straight line. Later in the program the arm moves in a straight line toward point P2 until input #2 turns on. If input #2 turns On during the Move, then the arm decelerates to a stop prior to arriving on point P2 and the next program instruction is executed.

Function movetest

  Home

  Go P0

  Go P1

  Move P0

  Move P2 Till Sw(2) = On

  If Sw(2) = On Then

    Print "Input #2 came on during the move and"

    Print "the robot stopped prior to arriving on"

    Print "point P2."

  Else

    Print "The move to P2 completed successfully."

    Print "Input #2 never came on during the move."

  Endif

Fend

This example uses Move with CP. The diagram below shows arc motion which originated at the point P100 and then moves in a straight line through P101, at which time the arm begins to form an arc. The arc is then continued through P102 and on to P103. Next the arm moves in a straight line to P104 where it finally decelerates to a stop. Note that the arm doesn't decelerate between each point until its final destination of P104. The following function would generate such a motion.

Function CornerArc

  Go P100

  Move P101 CP 'Do not stop at P101

  Arc P102, P103 CP 'Do not stop at P103

  Move P104 'Decelerate to stop at P104

Fend


---

# Multi-tasking
**Type:** reference | **Section:** Operator

## Description
Multi-tasking

Multi-tasking

For some applications, you may want to control other equipment besides the robot, such as conveyors, pick and place units, etc.  By using multi-tasking, you can control this other equipment with their own tasks.

SPEL+ supports up to 32 normal tasks and 16 background tasks (48 tasks in total) running simultaneously. A task is a function that has been started by the system or by the Xqt statement.

Use the Xqt statement to start another task from within a function. You can optionally specify a task number from 1 to 32 in the Xqt statement.

A task started from a background task is started as a background task. You can execute up to 16 background tasks simultaneously.

The table below shows the program instructions that are used for multitasking.

Statement	Description

Xqt	Starts a function as a task.

Halt	Temporarily suspends execution of
		 a task.

Resume	Resumes a task that has been halted.

Quit	Stops a task.

Signal	Sends a signal to one or more tasks
		 that are waiting for the signal using WaitSig.

SyncLock	Locks a resource for use by the current
		 task and blocks other tasks from using the resource until SyncUnlock
		 is executed.

WaitSig	Waits for a signal from another task.

Pause	Pause all tasks.

One example for starting another task is to run a conveyor system for the robot work cell.

Program: MAINTASK.PRG

Function Main

   Xqt Conveyor        ' Start the conveyor task

    Do

        ...

        ...

    Loop

Fend

Program: CONVTASK.PRG

Function Conveyor

  Do

    Select True

        Case Sw(10) = On

            Off convCtrl

        Case Sw(11) = On

            On convCtrl

    Send

  Loop

Fend

## Examples
```spel
Function Main
   Xqt Conveyor        ' Start the conveyor task
    Do
        ...
        ...
    Loop
Fend
```

```spel
Function Conveyor Do
    Select True
        Case Sw(10) = On
            Off convCtrl
        Case Sw(11) = On
            On convCtrl
    Send Loop
```

```spel
Fend
```


---

# New command (Project menu)
**Type:** reference | **Section:** Operator

## Description
New command (Project menu)

New Command (Project Menu)
 : Ctrl+Shift+N

The New command is used to create a new Epson RC+ 8.0 project.

Item	Description

New Project
		 Name	Type
		 in a new name for the project.

The name can include alphanumeric characters
		 along with underscores.

For a project name, Japanese characters
		 are not allowed. Be careful when you set the alternative models.

Template	Select
		 a project template.

		The new project will be a copy of the template project.

Project
		 save destination	Select
		 the folder to save the new project to.

When specifying a new destination, click
		 the [...] button to set the save destination. Set the destination
		 in advance in the Epson RC+ menu, [Setup]-[Preferences]-[Workspace]-[Project
		 Save Destination].

Select
		 Project Folder	This
		 is a list of folders and projects on the selected save destination.
		 If you click on a name of projects in this list, the name appear
		 in the [New Project Name] text box and can be edited. You can
		 then edit the name, or you can create a new project with the same
		 name as one that has already been created. In the later case,
		 you will be prompted to overwrite the old project if it is in
		 the same folder.

New Folder	Creates
		 a new folder in the currently selected folder.

OK	Creates
		 the new project.

Cancel	Cancels
		 the operation and closes the dialog.


---

# Not Operator
**Type:** reference | **Section:** Operator

## Syntax
```
Not operand
```

## Parameters
operand	Integer, Long, or Boolean expression.

## Description
Not is a unary operator (has one operand).  For Boolean expressions, Not returns True or False.  For number expressions, Not returns the bitwise complement on the value of the operand.  Each bit of the result is the complement of the corresponding bit in the operand, effectively changing 0 bits to 1, and 1 bits to 0.

## Examples
```spel
>print not 1
```

```spel
-2
```

```spel
>
```

```spel
Function main
		  Boolean result

result = False

If Not result Then
		    Print "result was true"
		  EndIf
		Fend
```

## See Also
Abs	RShift

And	Sgn

Atan	Sin

Atan2	Sqr

Cos	Str$

Int	Tan

LShift	Val

Mod	Xor

Or

Not Operator Example

>print not 1

-2

>

Function main

		  Boolean result

result = False

If Not result Then

		    Print "result was true"

		  EndIf

		Fend


---

# Off Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Off { bitNumber | outputLabel } [, time [, parallel ] [,Forced]
```

## Parameters
bitNumber	Integer expression
		 representing which Output to turn Off.

outputLabel	Output label.

time	Optional.
		 Specifies a time interval in seconds for the output to remain
		 Off. After the time interval expires, the Output is turned back
		 on.  The minimum time interval is 0.01 seconds and maximum
		 time interval is 10 seconds.

parallel	Optional. When a timer is set, the parallel
		 parameter may be used to specify when the next command executes:

0 - immediately after the output is turned
		 off

1 - after the
		 specified time interval elapses. (default value)

Forced	Optional. Usually omitted.

## Description
Off turns off (sets to 0) the specified output.

If the time interval parameter is specified, the output bit specified by outnum is switched off, and then switched back on after the time interval elapses. If prior to executing Off, the Output bit was already off, then it is switched On after the time interval elapses.

The parallel parameter settings are applicable when the time interval is specified as follows:

1: Switches the output off, switches it back on after specified interval elapses, then executes the next command. (This is also the default value for the parallel parameter.  If this parameter is omitted, this is the same as setting the parameter to 1.)

0: Switches the output off, and simultaneously executes the next command.

## Notes
Output bits Configured as Remote Control output

If an output bit which was set up as a system output is specified, an error will occur.  Remote control output bits are turned on or off automatically according to system status.

Outputs and When an Emergency Stop Occurs:

Epson RC+ has a feature which causes all outputs to go off when an E-Stop occurs.  This feature is set or disabled from Setup | System Configuration | Preferences.

Forced Flag

This flag is used to turn Off the I/O output at Emergency Stop and Safety Door Open from NoPause task or NoEmgAbort task (special task using NoPause or NoEmgAbort at Xqt). Be sure that the I/O outputs change by Emergency Stop and Safety Door Open when designing the system.

## Examples
```spel
Function main Xqt 2, iotask Go P1 ' ' More commands here '
Fend
```

```spel
Function iotask Do
    On 1
    On 2
    Off 1
    Off 2
    Wait 10 Loop
Fend
```

```spel
> on 1
> off 1, 10 ' Turn Output 1 off, wait 10 secs, turn on again
> on 2
> off 2
```

## See Also
In, InBCD, MemOn, MemOff, MemOut, MemSW, OpBCD, Oport, Out, Wait

Off Statement Example

The example shown below shows main task start a background task called iotask.  The iotask is a simple task to turn discrete output bits 1 and 2 on and then off, Wait 10 seconds and then do it again.

Function main

  Xqt 2, iotask

  Go P1

  '

  ' More commands here

  '

Fend

Function iotask

  Do

    On 1

    On 2

    Off 1

    Off 2

    Wait 10

  Loop

Fend

Other simple examples from the Command window are as follows:

> on 1

> off 1, 10 ' Turn Output 1 off, wait 10 secs, turn on again

> on 2

> off 2


---

# On Statement
**Type:** reference | **Section:** Operator

## Syntax
```
On { bitNumber | outputLabel } [, time [, parallel ] [, Forced ]]
```

## Parameters
bitNumber	Integer expression
		 representing which Output to turn On.

outputLabel	Output label.

time	Optional.
		 Specifies a time interval in seconds for the output to remain
		 On.  After the time interval expires, the Output is turned
		 back off. (Minimum time interval is 0.01 seconds)

parallel	Optional.  When a timer is set,
		 the parallel parameter may be used to specify when the next command
		 executes:

0 - immediately after the output is turned
		 on

1 - after the
		 specified time interval elapses. (default value)

Forced	Optional.   Usually omitted.

## Description
On turns On (sets to 1) the specified output bit.

If the time interval parameter is specified, the output bit specified by bitNumber is switched On, and then switched back Off after the time interval elapses.

The parallel parameter settings are applicable when the time interval is specified as follows:

1: Switches the output On, switches it back Off after specified interval elapses, then executes the next command. (This is also the default value for the parallel parameter.  If this parameter is omitted, this is the same as setting the parameter to 1.)

0: Switches the output On, and simultaneously executes the next command.

Note

Output bits Configured as remote

If an output bit which was set up as remote is specified, an error will occur.  Remote output bits are turned ON or OFF automatically according to system status.  For more information regarding remote, refer to Epson RC+ User's Guide.  The individual bits for the remote connector can be set as remote or I/O from [Setup]-[System Configuration]-[Controller]-[Remote Control] panel.

Outputs and When an Emergency Stop Occurs

The Controller has a feature which causes all outputs to go off when an E-Stop occurs.  If you want to keep the settings even in case of the emergency stop, this feature can be reconfigured from the [Outputs Off during emergency stop] checkbox in [Setup]-[System Configuration]-[Controller]-[Preferences].

Forced Flag

This flag is used to turn On the I/O output at Emergency Stop and Safety Door Open from NoPause task, NoEmgAbort task (special task using NoPause or NoEmgAbort at Xqt), or background tasks.

Be sure that the I/O outputs change by Emergency Stop and Safety Door Open when designing the system.

## Examples
```spel
Function main Xqt iotask Go P1 ' ' More commands here '
Fend
```

```spel
Function iotask Do
    On 1
    On 2
    Off 1
    Off 2
    Wait 10 Loop
Fend
```

```spel
> On 1
> Off 1, 10 'Turn Output 1 off, wait 10 secs, turn on again
> On 2
> Off 2
```

## See Also
In, InBCD, MemOn, MemOff, MemOut, MemSW, Off, OpBCD, Oport, Out, Wait

On Statement Example

The example shown below shows main task start a background task called iotask.  The iotask is a simple task to turn discrete output bits 1 and 2 on and then off, Wait 10 seconds and then do it again.

Function main

  Xqt iotask

  Go P1

  '

  ' More commands here

  '

Fend

Function iotask

  Do

    On 1

    On 2

    Off 1

    Off 2

    Wait 10

  Loop

Fend

Other simple examples from the command window are as follows:

> On 1

> Off 1, 10 'Turn Output 1 off, wait 10 secs, turn on again

> On 2

> Off 2


---

# OnErr command
**Type:** reference | **Section:** Operator

## Syntax
```
OnErr GoTo {label | 0}
```

## Parameters
label	Statement label to jump to when an error occurs.

0	Parameter used to clear OnErr setting.

## Description
OnErr enables user error handling. When an error occurs without OnErr being used, the task is terminated and the error is displayed.  However, when OnErr is used it allows the user to "catch" the error and go to an error handler to automatically recover from the error.  Upon receiving an error, OnErr branches control to the designated label specified in the OnErr instruction.  In this way the task is not terminated and the user is given the capability to automatically handle the error.  This makes workcells run much smoother since potential problems are always handled and recovered from in the same fashion.

When the OnErr command is specified with the 0 parameter, the current OnErr setting is cleared. (i.e. After executing OnErr 0, if an error occurs program execution will stop.)

## Examples
```spel
Function errDemo
		  Integer i, errNum, temp

OnErr GoTo
			 errHandler

For i = 0 To 399
		    temp = CX(P(i))
		  Next i
		  Exit Function
		  '
		  '
		  '*********************************************
		  '* Error Handler *
		  '*********************************************
		errHandler:
		  errNum = Err
		  ' Check if using undefined point
		  If errNum = 7007 Then
		    Print "Point number P", i, " is undefined!"
		  Else
		    Print "ERROR: Error number ", errNum, " occurred while"
		    Print " trying to process point P", i, " !"
		  EndIf
		  EResume Next
		Fend
```

## See Also
Error Handling

Error Codes

Err

OnErr Example

The following example shows a simple utility program which checks whether points P0-P399 exist. If the point does not exist, then a message is printed on the screen to let the user know this point does not exist. The program uses the CX instruction to test each point for whether or not it has been defined. When a point is not defined control is transferred to the error handler and a message is printed on the screen to tell the user which point was undefined.

Function errDemo

		  Integer i, errNum, temp

OnErr GoTo
			 errHandler

For i = 0 To 399

		    temp = CX(P(i))

		  Next i

		  Exit Function

		  '

		  '

		  '*********************************************

		  '* Error Handler *

		  '*********************************************

		errHandler:

		  errNum = Err

		  ' Check if using undefined point

		  If errNum = 7007 Then

		    Print "Point number P", i, " is undefined!"

		  Else

		    Print "ERROR: Error number ", errNum, " occurred while"

		    Print " trying to process point P", i, " !"

		  EndIf

		  EResume Next

		Fend


---

# OpBCD Statement
**Type:** reference | **Section:** Operator

## Syntax
```
OpBCD portNumber, outData [, Forced ]
```

## Parameters
PortNumber	Outputs

0	0-7

1	8-15

2	16-23

3	24-31

...	...

...

outData	Integer expression
		 between 0-99 representing the output pattern for the output group
		 selected by portNumber.
		 The 2nd digit (called the 1's digit) represents the lower 4 outputs
		 in the selected group and the 1st digit (called the 10's digit)
		 represents the upper 4 outputs in the selected group.

Forced	Optional.
		 Usually omitted.

## Description
OpBCD simultaneously sets 8 output lines using the BCD format. The standard and expansion user outputs are broken into groups of 8. The portNumber parameter for the OpBCD instruction defines which group of 8 outputs to use where portNumber = 0 means outputs 0-7, portNumber = 1 means outputs 8-15, etc..

Once a port number is selected (i.e. a group of 8 outputs has be selected), a specific output pattern must be defined. This is done in Binary Coded Decimal format using the outdata parameter. The outdata parameter may have 1 or 2 digits. (Valid entries range from 0 to 99.) The 1st digit (or 10's digit) corresponds to the upper 4 outputs of the group of 8 outputs selected by portNumber. The 2nd digit (or 1's digit) corresponds to the lower 4 outputs of the group of 8 outputs selected by portNumber.

Since valid entries in BCD format range from 0-9 for each digit, every I/O combination cannot be met. The table below shows some of the possible I/O combinations and their associated outnum values assuming that portNumber is 0.

Output Settings (Output number)

Outnum
		 Value	7	6	5	4	3	2	1	0

01	Off	Off	Off	Off	Off	Off	Off	On

02	Off	Off	Off	Off	Off	Off	On	Off

03	Off	Off	Off	Off	Off	Off	On	On

08	Off	Off	Off	Off	On	Off	Off	Off

09	Off	Off	Off	Off	On	Off	Off	On

10	Off	Off	Off	On	Off	Off	Off	Off

11	Off	Off	Off	On	Off	Off	Off	On

99	On	Off	Off	On	On	Off	Off	On

Notice that the Binary Coded Decimal format only allows decimal values to be specified. This means that through using Binary Coded Decimal format it is impossible to turn on all outputs with the OpBCD instruction. Please note that the maximum value for either digit for outnum is 9. This means that the largest value possible to use with OpBCD is 99. In the table above it is easy to see that 99 does not turn all Outputs on. Instead it turns outputs 0, 3, 4, and 7 On and all the others off.

## Notes
Difference between OpBCD and Out

The OpBCD and Out instructions are very similar in the SPEL language. However, there is one major difference between the two. This difference is shown below:
 - The OpBCD instruction uses the Binary Coded Decimal format for specifying an 8 bit value to use for turning the outputs on or off. Since Binary Coded Decimal format precludes the values of &HA, &HB, &HC, &HD, &HE or &HF from being used, all combinations for setting the 8 output group cannot be satisfied.
 - The Out instruction works very similarly to the OpBCD instruction except that Out allows the range for the 8 bit value to use for turning outputs on or off to be between 0-255 (vs. 0-99 for OpBCD). This allows all possible combinations for the 8 bit output groups to be initiated according to the users specifications.

Output bits Configured as remote:

If an output bit which was set up as remote is specified to be turned on by OpBCD, an error will occur. Remote output bits are turned On or Off automatically according to system status.  For more information regarding remote, refer to Epson RC+ User's Guide.  The individual bits for the remote connector can be set as remote or I/O from [Setup]-[System Configuration]-[Controller]-[Remote Control] panel.

Outputs and When an Emergency Stop Occurs:

The controller has a feature which causes all outputs to go off when an E-Stop occurs. This feature is set or disabled from one of the Option Switches. To configure this go to Setup | System Configuration | Preferences.

Forced Flag

This flag is used to turn On the I/O output at Emergency Stop and Safety Door Open from NoPause task or NoEmgAbort task (special task using NoPause or NoEmgAbort at Xqt). Be sure that the I/O outputs change by Emergency Stop and Safety Door Open when designing the system.

## Examples
```spel
Function main Xqt 2, iotask Go P1 . . .
Fend
```

```spel
Function iotask Do
    OpBCD 0, 6
    OpBCD 0, 9
    Wait 10 Loop
Fend
```

```spel
> OpBCD 1,6  'Turns on Outputs 1 and 2
> OpBCD 2,1  'Turns on Output 8
> OpBCD 3, 91 'Turns on Output 24, 28, and 31
```

## See Also
In, InBCD, MemOn, MemOff, MemOut, MemSW, Off, Oport, Out, Wait

OpBCD Statement


---

# OpenCom Statement
**Type:** reference | **Section:** Operator

## Syntax
```
OpenCom #portNumber
```

## Parameters
portNumber	Integer expression
		 for RS-232C port number to open.

The range of
		 port number is:

Real Part1 ~
		 8

Windows Part1001
		 to 1008

## Description
You need to connect the specified RS-232C port to the controller.

To use the SPEL+ real part ports, option I/O board must be installed to the Controller.

To use Windows part ports, RC+ setting must be done.  For details, refer to the description about RC-232C in the Epson RC+ User's Guide 5.13 [Setup] Menu.

## Examples
```spel
Integer PortNo
PortNo = 1001
```

```spel
OpenCom #PortNo
Print #PortNo, "Data from COM1"
CloseCom #PortNo
```

## See Also
ChkCom, CloseCom, SetCom

OpenCom Statement


---

# OpenNet Statement
**Type:** reference | **Section:** Operator

## Syntax
```
OpenNet #portNumber
			As { Client | Server }
```

## Parameters
portNumber	Integer expression for TCP/IP port number to open. Range is 201 - 216.

## Description
OpenNet opens a TCP/IP port for communication with another computer on the network.

One system should open as Server and the other as Client. It does not matter which one executes first.

## Examples
```spel
Function tcpip1

			  OpenNet #201 As Server
		  WaitNet #201
		  Print #201, "Data from host 1"
		  CloseNet #201
		Fend
```

```spel
Function tcpip2
		  String data$

			  OpenNet #201 As Client
		  WaitNet #201
		  Input #201, data$
		  Print "received '", data$, "' from host 1"
		Fend
```

## See Also
ChkNet

CloseNet

SetNet

OpenNet Statement Example

For this example, two controllers have their TCP/IP settings configured as follows:

Controller #1:

Port: #201

Host Name: 192.168.0.2

TCP/IP Port: 1000

Function tcpip1

OpenNet #201 As Server

		  WaitNet #201

		  Print #201, "Data from host 1"

		  CloseNet #201

		Fend

Controller #2:

Port: #201

Host Name: 192.168.0.1

TCP/IP Port: 1000

Function tcpip2

		  String data$

OpenNet #201 As Client

		  WaitNet #201

		  Input #201, data$

		  Print "received '", data$, "' from host 1"

		Fend


---

# Oport Function
**Type:** reference | **Section:** Operator

## Syntax
```
Oport(
			bitNumber
			)
```

## Parameters
bitNumber	Integer expression representing I/O output bits.

## Description
Oport provides a status check for the hardware outputs which EPSON RC+ 7.0 supports. It functions much in the same way as the Sw instruction does for hardware inputs. Oport is most commonly used to check the status of one of the hardware outputs which could be connected to a feeder, conveyor, gripper solenoid, or a host of other devices which works via discrete I/O. Obviously the output checked with the Oport instruction has 2 states (1 or 0). These indicate whether the specified output is On or Off.

## Notes
Difference between Oport and Sw:

It is very important for the user to understand the difference between the Oport and Sw instructions. Both instructions are used to get the status of I/O. However, the type of I/O is different between the two. The Sw instruction works with memory bits and hardware inputs. The Oport instruction works with the standard and expansion hardware outputs. These hardware ports are discrete outputs which interact with devices external to the controller.

## Examples
```spel
Function main
		  TMOut 10
		  OnErr errchk
		  Integer errnum
		  On 5 'Turn on output 5
		  Wait Oport(5)
		  Call mkpart1
		  Exit Function

errchk:
		  errnum = Err(0)
		  If errnum = 94 Then
		    Print "TIME Out Error Occurred during period"
		    Print "waiting for Oport to come on. Check"
		    Print "Output #5 for proper operation. Then"
		    Print "restart this program."
		  Else
		    Print "ERROR number ", errnum, "Occurred"
		    Print "Program stopped due to errors!"
		  EndIf
		  Exit Function
		Fend
```

```spel
> On 1
		> Print Oport(1)

1
		> Off 1
		> Print Oport(1)

0

>
```

## See Also
In, InBCD, MemIn, MemOn, MemOff, MemOut, Off, On, OpBCD, Out, Sw, Wait

Oport Function Example

The example shown below turns on output 5, then checks to make sure it is on before continuing.

Function main

		  TMOut 10

		  OnErr errchk

		  Integer errnum

		  On 5 'Turn on output 5

		  Wait Oport(5)

		  Call mkpart1

		  Exit Function

errchk:

		  errnum = Err(0)

		  If errnum = 94 Then

		    Print "TIME Out Error Occurred during period"

		    Print "waiting for Oport to come on. Check"

		    Print "Output #5 for proper operation. Then"

		    Print "restart this program."

		  Else

		    Print "ERROR number ", errnum, "Occurred"

		    Print "Program stopped due to errors!"

		  EndIf

		  Exit Function

		Fend

Other simple examples are as follows from the command window:

> On 1

		> Print Oport(1)

1

		> Off 1

		> Print Oport(1)

0

>


---

# Options Command (Setup Menu)
**Type:** reference | **Section:** Operator

## Description
Options Command (Setup Menu)

[Options] Command (Setup Menu)

This dialog allows you to view and enable options in the controller.

Epson RC+ 8.0 uses a key that is stored in the Spel controller board to enable options on the system.

If an option is not enabled, you can purchase it from the supplier of your region. Please contact the supplier. When you call to purchase, you must give the Options Key Code to the operator. You will then be given a code to enable the option for the current software options key.

After receiving the code, click the [Enable] button and enter the code. The option you purchased should now be enabled.

For details on enabling options, refer to Installing Controller Options.


---

# Or Operator
**Type:** reference | **Section:** Operator

## Syntax
```
expr1
			Or
			expr2
```

## Parameters
expr1, expr2	Integer or Boolean expressions.

## Description
For integer expressions, the Or operator performs the bitwise OR operation on the values of the operands. Each bit of the result is 1 if one or both of the corresponding bits of the two operands is 1.  For Boolean expressions, the result is True if either of the expressions evaluates to True.

## Examples
```spel
>print 1 or 2

			3

			>
```

```spel
If a = 1 Or b = 2 Then
		  c = 3
		EndIf
```

## See Also
And

LShift

Mod

Not

RShift

Xor

Or Operator Example

Here is an example of a bitwise OR.

>print 1 or 2

3

>

Here is an example of a logical OR.

If a = 1 Or b = 2 Then

		  c = 3

		EndIf


---

# Out Function
**Type:** function | **Section:** Operator

## Syntax
```
Out(
			portNumber
			)
```

## Parameters
Portnum	Outputs

0	0-7

1	8-15

8-15

## Description
Out Function

Out Function

See_Also Example

Returns the status of one byte of outputs.

## Examples
```spel
Print Out(0)
```

## See Also
Out Statement

Out Function Example

Print Out(0)


---

# Out Keyword
**Type:** reference | **Section:** Operator

## Description
Out Keyword

Out Keyword

The Out keyword is used in these contexts:

Out Statement

Out Function


---

# Out Statement
**Type:** statement | **Section:** Operator

## Syntax
```
Out portNumber, outData [, Forced]
```

## Parameters
Portnum	Outputs

0	0-7

1	8-15

2	16-23

3	24-31

...	...

...

outData	Integer number between 0-255 representing the output pattern for the output group selected by portNumber. If represented in hexadecimal form the range is from &H0 to &HFF. The lower digit represents the least significant digits (or the 1st 4 outputs) and the upper digit represents the most significant digits (or the 2nd 4 outputs).

Forced	Optional. Usually omitted.

## Description
Out simultaneously sets 8 output bits using the combination of the portNumber and outdata values specified by the user to determine which outputs will be set.  The portNumber parameter defines which group of 8 outputs to use where portNumber = 0 means outputs 0-7, portNumber = 1 means outputs 8-15, etc..

Once a portnum is selected (i.e. a group of 8 outputs has be selected), a specific output pattern must be defined.  This is done using the outData parameter.  The outData parameter may have a value between 0-255 and may be represented in Hexadecimal or Integer format. (i.e. &H0-&HFF or 0-255)

The table below shows some of the possible I/O combinations and their associated outData values assuming that portNumber is 0, and 1 accordingly.

Output Settings When portNumber = 0 (Output number)

outData Value	7	6	5	4	3	2	1	0

01	Off	Off	Off	Off	Off	Off	Off	On

02	Off	Off	Off	Off	Off	Off	On	Off

03	Off	Off	Off	Off	Off	Off	On	On

08	Off	Off	Off	Off	On	Off	Off	Off

09	Off	Off	Off	Off	On	Off	Off	On

10	Off	Off	Off	On	Off	Off	Off	Off

11	Off	Off	Off	On	Off	Off	Off	On

99	Off	On	On	Off	Off	Off	On	On

255	On	On	On	On	On	On	On	On

Output Settings When portNumber = 1 (Output number)

outData Value	15	14	13	12	11	10	9	8

01	Off	Off	Off	Off	Off	Off	Off	On

02	Off	Off	Off	Off	Off	Off	On	Off

03	Off	Off	Off	Off	Off	Off	On	On

08	Off	Off	Off	Off	On	Off	Off	Off

09	Off	Off	Off	Off	On	Off	Off	On

10	Off	Off	Off	On	Off	Off	Off	Off

11	Off	Off	Off	On	Off	Off	Off	On

99	Off	On	On	Off	Off	Off	On	On

255	On	On	On	On	On	On	On	On

## Notes
Difference between OpBCD and Out

The Out and OpBCD instructions are very similar in the SPEL language.  However, there is one major difference between the two. This difference is shown below:
 - The OpBCD instruction uses the Binary Coded Decimal format for specifying 8 bit value to use for turning the outputs on or off. Since Binary Coded Decimal format precludes the values of &HA, &HB, &HC, &HD, &HE or &HF from being used, all combinations for setting the 8 output group cannot be satisfied.
 - The Out instruction works very similarly to the OpBCD instruction except that Out allows the range for the 8 bit value to use for turning outputs on or off to be between 0-255 (vs. 0-99 for OpBCD).  This allows all possible combinations for the 8 bit output groups to be initiated according to the users specifications.

Forced Flag

This flag is used to turn On the I/O output at Emergency Stop and Safety Door Open from NoPause task or NoEmgAbort task (special task using NoPause or NoEmgAbort at Xqt), or background tasks. Be sure that the I/O outputs change by Emergency Stop and Safety Door Open when designing the system.

## Examples
```spel
Function main Xqt iotask Do
    Go P1
    Go P2 Loop
Fend
```

```spel
Function iotask Do
    Out 0, &H0F
    Out 0, &H00
    Wait 10 Loop
Fend
```

```spel
> Out 1,6  'Turns on Outputs 9 & 10
> Out 2,1  'Turns on Output 8
> Out 3,91 'Turns on Outputs 24, 25, 27, 28, and 30
```

## See Also
In, InBCD, MemOn, MemOff, MemOut, MemSW, Off, OpBCD, Oport, On, Wait

Out Statement Example

The example shown below shows main task start a background task called iotask.  The iotask is a simple task to flip flop between turning output bits 0-3 On and then Off.  The Out instruction makes this possible using only 1 command rather than turning each output On and Off individually.

Function main

  Xqt iotask

  Do

    Go P1

    Go P2

  Loop

Fend

Function iotask

  Do

    Out 0, &H0F

    Out 0, &H00

    Wait 10

  Loop

Fend

Other simple examples from the command window are as follows:

> Out 1,6  'Turns on Outputs 9 & 10

> Out 2,1  'Turns on Output 8

> Out 3,91 'Turns on Outputs 24, 25, 27, 28, and 30


---

# OutW Function
**Type:** function | **Section:** Operator

## Syntax
```
OutW(
			wordPortNum
			)
```

## Parameters
wordPortNum	Integer expression representing I/O output words.

## Description
OutW Function

OutW Function

See_Also Example

Returns the status of one word (2 bytes) of outputs.

## Examples
```spel
OutW 0, &H1010
```

## See Also
OutW Statement

OutW Function Example

OutW 0, &H1010


---

# OutW Keyword
**Type:** reference | **Section:** Operator

## Description
OutW Keyword

OutW Keyword

The OutW keyword is used in these contexts:

OutW Statement

OutW Function


---

# OutW Statement
**Type:** statement | **Section:** Operator

## Syntax
```
OutW wordPortNum, outputData [, Forced]
```

## Parameters
wordPortNum	Integer expression representing I/O output words.

outputData	Specifies output data (integers from 0 to 65535) using an expression or numeric value.

Forced	Optional. Usually omitted.

## Description
Changes the current status of user I/O output port group specified by the word port number to the specified output data.

## Notes
Forced Flag

This flag is used to turn On the I/O output at Emergency Stop and Safety Door Open from NoPause task or NoEmgAbort task (special task using NoPause or NoEmgAbort at Xqt), or background tasks. Be sure that the I/O outputs change by Emergency Stop and Safety Door Open when designing the system.

## Examples
```spel
OutW 0, 25
```

## See Also
In

InW

Out

OutW Statement Example

OutW 0, 25


---

# P# (1. Point Definition) Statement
**Type:** reference | **Section:** Operator

## Syntax
```
point = pointExpr
```

## Parameters
point	Expression including numeric number
		 or ( ) (parenthesis)

P
		 number

		P(expr)

pointLabel

pointLabel	Point label

pointExpr	One of the following point data

P point number, Point label, Here, Pallet,
		 Point data function

(Here function, XY function, JA function,
		 Pulse function, etc..)

## Description
Define a robot point by setting it equal to another point or point expression.

## Examples
```spel
> P1 = 300,200,-50,100
```

```spel
> P2 = -400,200,-80,100/L
```

```spel
> P3 = P2 +X(20)
```

```spel
> plist 3
```

```spel
P3=-380,200,-80,100/L
```

```spel
>P4=P2 -Y(50) :Z(-30) /R
>plist 4
P4 = XY(-450,200,-30,100)/R
```

```spel
> P5 = Here
```

```spel
> P6 = pallet(3,5) +U(90)
```

## See Also
Defines a robot point by assigning it to a point expression.

Local

Pallet

PDef

PDel

Plist

Point Expression

Point Assignment Example

The following examples are done from the command window:

Assign coordinates to P1:

> P1 = 300,200,-50,100

Specify left arm posture:

> P2 = -400,200,-80,100/L

Add 20 to X coordinate of P2 and define resulting point as P3:

> P3 = P2 +X(20)

> plist 3

P3=-380,200,-80,100/L

Subtract 50 from Y coordinate of P2, substitute -30 for Z coordinate, and define the resulting point P4 as right arm posture:

>P4=P2 -Y(50) :Z(-30) /R

>plist 4

P4 = XY(-450,200,-30,100)/R

Add 90 to U coord of Pallet(3, 5), and define resulting point as P6:

> P5 = Here

> P6 = pallet(3,5) +U(90)


---

# P# (2. Point Expression) Statement
**Type:** reference | **Section:** Operator

## Syntax
```
point [ { + | - } point ] [local] [hand (arm)] [elbow] [wrist] [j4flag] [j6flag] [j1flag] [j2flag] [relativeOffsets] [absoluteCoords]
```

## Parameters
point	The base point specification. This can
		 be one of the following:

P
		 number

P(expr)

Here

Pallet(palletNumber, palletIndex)

pointLabel

XY(X,
		 Y, Z, U, [V], [W])

JA(J1,
		 J2, J3, J4, [J5], [J6])

Pulse(J1, J2, J3, J4, [J5], [J6])

local	Optional.
		 Local number from 1 to 15 preceeded by a forward slash (/1 to
		 /15) or at sign (@1 to @15). The forward slash means that the
		 coordinates will be in the local. The at sign means that the coordinates
		 will be translated into local coordinates.

When using conveyor
		 tracking, you can also specify a conveyor local coordinate system
		 using /CNV(expr) or @CNV(expr) where expr is a valid conveyor
		 number.

hand
		 (arm)	Optional for SCARA (including RS series)
		 and 6-axis robots. Specify /L
		 or /R for lefty or righty
		 hand (arm) orientation.

elbow	Optional for 6-axis robots.  Specify
		 /A or /B for above or below orientation.

wrist	Optional for 6-axis robots.  Specify
		 /F or /NF for flip or no flip orientation.

j4flag	Optional for 6-axis robots.  Specify
		 /J4F0 or /J4F1.

j6flag	Optional for 6-axis robots.  Specify
		 /J6F0 - /J6F127.

j1flag	Optional for RS series. Specify /J1F0
		 or /J1F1.

j2flag	Optional for RS series. Specify /J2F0
		 - /J2F127.

j1angle	Optional for RS series. Specify /J1A
		 (real value).

relativeOffsets	Optional. One or more relative coordinate
		 adjustments.

{+ | -}
		 {X | Y
		 | Z | U
		 | V | W
		 |R | S | T | ST} (expr)

The TL offsets are relative offsets
		 in the current tool coordinate system.

{+ | -}
		 {TLX | TLY
		 | TLZ | TLU
		 | TLV | TLW}
		 (expr)

absoluteCoords	Optional. One or more absolute coordinates.

:
		 {X | Y
		 | Z | U|
		 V | W
		 | R| S| T| ST } (
		 expr )

## Description
Point expressions are used in point assignment statements and motion commands.

Go P1 + P2

P1 = P2 + XY(100, 100, 0, 0)

Using relative offsets

You can offset one or more coordinates relative to the base point. For example, the following statement moves the robot 20 mm in the positive X axis from the current position:

Go Here +X(20)

If you execute the same statement again, the robot will move an additional 20 mm along the X axis, because this is a relative move.

You can also use relative tool offsets:

Go Here +TLX(20) -TLY(5.5)

When the 6-axis robot moves to a point calculated by such as pallet or relative offsets, the wrist part may rotate to an unintended direction. The point calculation above does not depend on robot models and results in motion without converting the required point flag. LJM function prevents the unintended wrist rotation.

Go LJM(Here +X(20))

Using absolute coordinates

You can change one or more coordinates of the base point by using absolute coordinates. For example, the following statement moves the robot to the 20 mm position on the X axis:

Go Here :X(20)

If you execute the same statement again, the robot will not move because it is already in the absolute position for X from the previous move.

Relative offsets and absolute coordinates make is easy to temporarily modify a point. For example, this code moves quickly above the pick point by 10 mm using a relative offset for Z or 10 mm, then moves slowly to the pick point.

Speed fast

Jump pick +Z(10)

Speed slow

Go pick

This code moves straight up from the current position by specifying an absolute value of 0 for the Z joint:

LimZ 0

Jump Here :Z(0)

Using Locals

You can specify a local number using a forward slash or at sign. Each has a separate function.

Use the forward slash to mark the coordinates in a local. For example, adding a /1 in the following statement says that P1 will be at location 0,0,0,0 in local 1.

P1 = XY(0, 0, 0, 0) /1

Use the at sign to translate the coordinates into local coordinates. For example, here is how to set the current position to P1:

P1 = Here @1

P1 is set to the current position translated to its position in local 1.

## Examples
```spel
Go P1 + P2
P1 = P2 + XY(100, 100, 0, 0)
```

```spel
Go Here +X(20)
```

```spel
Go Here +TLX(20) -TLY(5.5)
```

```spel
Go LJM(Here +X(20))
```

```spel
Go Here :X(20)
```

```spel
Speed fast
Jump pick +Z(10)
Speed slow
Go pick
```

```spel
LimZ 0
Jump Here :Z(0)
```

```spel
P1 = XY(0, 0, 0, 0) /1
```

```spel
P1 = Here @1
```

```spel
P1 = XY(300,200,-50,100)
P2 = P1 /R
P3 = pick /1
P4 = P5 + P6
P(i) = XY(100, 200, CZ(P100), 0)
Go P1 -X(20) :Z(-20) /R
Go Pallet(1, 1) -Y(25.5)
Move pick /R
Jump Here :Z(0)
Go Here :Z(-25.5)
```

```spel
Go JA(25, 0, -20, 180)
pick = XY(100, 100, -50, 0)

P1 = XY(300,200,-50,100, -90, 0)
P2 = P1 /F /B
P2 = P1 +TLV(25)
```

## See Also
Go, Jump, Local, LJM, Move, Pallet, Hand, Elbow, Wrist, J4Flag, J6Flag, J1Flag, J2Flag

Point Expression


---

# PAgl Function
**Type:** reference | **Section:** Operator

## Syntax
```
PAgl (point, jointNumber)
```

## Parameters
point	Point expression

jointNumber	Specifies the joint number (integer from 1 to 9) using an expression or numeric value.

The additional S axis is 8 and T axis is 9.

## Description
PAgl Function

PAgl Function

See_Also Example

Returns a joint value from a specified point.

## Examples
```spel
Real joint1
joint1 = PAgl(P10, 1)
```

## See Also
Agl

CX, CY, CZ, CU, CV, CW, CR, CS, CT Keywords

PPls

PAgl Function Example

Real joint1

joint1 = PAgl(P10, 1)


---

# PDef Function
**Type:** reference | **Section:** Operator

## Syntax
```
PDef (point)
```

## Parameters
point	An integer value or P
		 number
		 or P
		 ( expr
		 ) or point label.

Cautions for compatibility

No variables can be specified for point
		 parameter

To use variables, write

PDef(P(varName))

## Description
PDef Function

PDef Function

See_Also Example

Returns the definition status of a specified point.

## Examples
```spel
PDef(P(varName))
```

```spel
If Not PDef(1) Then
   Here P1
EndIf
Integer i
For i = 0 to 10 If PDef (P(i)) Then
    Print "P(";i;") is defined" EndIf
Next
```

## See Also
Here Statement, PDel

PDef Function Example

If Not PDef(1) Then

   Here P1

EndIf

Integer i

For i = 0 to 10

  If PDef (P(i)) Then

    Print "P(";i;") is defined"

  EndIf

Next


---

# PDel Statement
**Type:** reference | **Section:** Operator

## Syntax
```
PDel
			firstPointNum , [ lastPointNum ]
```

## Parameters
firstPointNum	The first point number in a sequence of points to delete. firstPointNum

						must be an integer.

lastPointNum	The last point number in a sequence of points to delete. lastPointNum

						must be an integer.

## Description
Deletes specified position data for the current robot. Deletes all position data from firstPointNum up to and including lastPointNum . To prevent Error 2 from occurring, firstPointNum must be less than lastPointNum .

## Examples
```spel
> p1=10,300,-10,0/L

> p2=0,300,-40,0

> p10=-50,350,0,0

> pdel 1,2 'Delete points 1 and 2

> plist

P10 = -50.000, 350.000, 0.000, 0.000 /R /0

> pdel 50 'Delete point 50

> pdel 100,200 'Delete from point 100 to point 200

>
```

## See Also
Clear

Plist

PDel Example

> p1=10,300,-10,0/L

> p2=0,300,-40,0

> p10=-50,350,0,0

> pdel 1,2 'Delete points 1 and 2

> plist

P10 = -50.000, 350.000, 0.000, 0.000 /R /0

> pdel 50 'Delete point 50

> pdel 100,200 'Delete from point 100 to point 200

>


---

# PG_FastStop Statement
**Type:** statement | **Section:** Operator

## Syntax
```
PG_FastStop
```

## Description
The PG_FastStop stops the current PG robot immediately with no deceleration.

To stop normally, use the PG_SlowStop statement.

## Examples
```spel
Function main

			  Motor On
		  PG_Scan 0
		  Wait 10
		  PG_FastStop                           ' Immediately stops the continuous motion
		Fend
```

## See Also
Stop the PG axes immediately.

PG_Scan

PG_SlowStop

PG_FastStop Example

The following program moves the PG axis for 10 seconds and stops it.

Function main

Motor On

		  PG_Scan 0

		  Wait 10

		  PG_FastStop                           ' Immediately stops the continuous motion

		Fend


---

# PG_Scan Statement
**Type:** statement | **Section:** Operator

## Syntax
```
PG_Scan direction As Integer
```

## Parameters
direction	Spinning direction

0: + (CW) direction

1: - (CCW) direction

## Description
The PG_Scan starts the continuous spinning motion of the current PG robot. To execute the continuous spinning motion, you need to enable the PG parameter continuous spinning by the robot configuration.

When the program execution task is completed, the continuous spinning stops.

## Examples
```spel
Function main Motor On Power High Speed 10; Accel 10, 10 PG_Scan 0 Wait 10 PG_SlowStop
Fend
```

## See Also
Starts the continuous spinning motion of the PG robot axes.

PG_FastStop

PG_Scan Example

The following example spins the PG axis for 10 seconds and stops it suddenly.

Function main

  Motor On

  Power High

  Speed 10; Accel 10, 10

  PG_Scan 0

  Wait 10

  PG_SlowStop

Fend


---

# PG_SlowStop Statement
**Type:** statement | **Section:** Operator

## Syntax
```
PG_SlowStop
```

## Description
PG_SlowStop decelates the continuous spinning motion of the current PG robot and bring it to a stop.

## Examples
```spel
Function main
		  Motor On
		  PG_Scan 0
		  Wait 10
		  PG_SlowStop       ' Stops suddenly the continuous spinning motion
		Fend
```

## See Also
PG_Scan

PG_FastStop

PG_SlowStop Example

The following example spins the PG axis for 10 seconds and stop it suddenly.

Function main

		  Motor On

		  PG_Scan 0

		  Wait 10

		  PG_SlowStop       ' Stops suddenly the continuous spinning motion

		Fend


---

# PPls Function
**Type:** reference | **Section:** Operator

## Syntax
```
PPls (point, jointNumber)
```

## Parameters
point	Point expression

jointNumber	Expression or numeric value specifying the joint number (integer from 1 to 9)

The additional S axis is 8 and T axis is 9.

## Description
PPls Function

PPls Function

See_Also Example

Return the pulse position of a specified joint value from a specified point.

## Examples
```spel
Long pulses1

pulses1 = PPls(P10, 1)
```

## See Also
Agl

CX, CY, CZ, CU, CV, CW, CR, CS, CT Keywords

PAgl

PPls Function Example

Long pulses1

pulses1 = PPls(P10, 1)


---

# PTCLR Statement
**Type:** statement | **Section:** Operator

## Syntax
```
PTCLR  [j1], [j2], [j3], [j4], [j5], [j6], [j7], [j8], [j9]
```

## Parameters
j1 - j9	Optional.  Integer expression representing the joint number.  If no parameters are supplied, then the peak torque values are cleared for all joints.

The additional S axis is 8 and T axis is 9.

## Description
PTCLR clears the peak torque values for the specified joints.

You must execute PTCLR before executing PTRQ.

## Examples
```spel
> ptclr

			> go p1
		> ptrq 1
		0.227
		> ptrq
		0.227
    0.118
		0.249
    0.083
		0.000
    0.000
```

## See Also
Clears and initializes the peak torque for one or more joints.

ATRQ

PTRQ

PTCLR Statement Example

> ptclr

> go p1

		> ptrq 1

		0.227

		> ptrq

		0.227
    0.118

		0.249
    0.083

		0.000
    0.000


---

# PTP Speed Acceleration for Small Distances
**Type:** reference | **Section:** Operator

## Description
PTP Speed Acceleration for Small Distances

PTP Speed Acceleration for Small Distances

You can change the speed and acceleration for small distances using PTPBoost and PTPBoostOK. Normally, PTPBoost is not required. In certain cases, you may want to shorten the cycle time even if vibration becomes larger, or conversely you may want to reduce vibration even if cycle time becomes longer. PTPBoost is a robot parameter with values from 0 - 100 that affects the speed and acceleration for small distances. Normally, for small distance motion, the desired speed cannot be attained using the current acceleration. By increasing PTPBoost, acceleration, deceleration, and speed are increased for small distance motion. To check if a motion command will be affected by PTPBoost, use the PTPBoostOK function. For details, refer to the following manual:

SPEL+ Language Reference: PTPBoost, PTPBoostOK


---

# PTPBoost Function
**Type:** reference | **Section:** Operator

## Syntax
```
PTPBoost(paramNumber)
```

## Parameters
paramNumber	Integer expression which can have the following values:

1: boost value

2: jump depart boost value

3: jump approach boost value

## Description
PTPBoost Function

PTPBoost Function

## Examples
```spel
Print PTPBoost(1)
```

## See Also
Returns the specified PTPBoost value.

PTPBoost Statement

PTPBoostOK

PTPBoost Function Example

Print PTPBoost(1)


---

# PTPBoost Keyword
**Type:** reference | **Section:** Operator

## Description
PTPBoost Keyword

PTPBoost Keyword

The PTPBoost keyword is used in these contexts:

PTPBoost Statement

PTPBoost Function


---

# PTPBoost Statement
**Type:** reference | **Section:** Operator

## Syntax
```
(1) PTPBoost
			boost, [departBoost], [approBoost]

(2) PTPBoost
```

## Parameters
boost	Integer expression from 0 - 100.

departBoost	Optional.  Jump depart boost value.  Integer expression from 0 - 100.

approBoost	Optional.  Jump approach boost value.  Integer expression from 0 - 100.

## Description
PTPBoost sets the acceleration, deceleration and speed for small distance PTP motion.
  It is effective only when the motion distance is small. The PTPBoostOK function can be used to confirm whether or not a specific motion distance to the destination is small enough to be affected by PTPBoost or not.

PTPBoost does not need modification under normal circumstances.  Use PTPBoost only when you need to shorten the cycle time even if vibration becomes larger, or conversely when you need to reduce vibration even if cycle time becomes longer.

When the PTPBoost value is large, cycle time becomes shorter, but the positioning vibration increases.  When PTPBoost is small, the positioning vibration becoms smaller, but cycle time becomes longer.  Specifying inappropriate PTPBoost causes errors or can damage the manipulator. This may degrade the robot, or sometimes cause the manipulator life to shorten.

The PTPBoost value initializes to the default values (low acceleration) when any one of the following conditions occurs:

Controller Startup

Motor On

SFree, SLock

Reset

Stop button or Quit All stops tasks

## Examples
```spel
PTPBoost 50, 30, 30
```

## See Also
Specifies or displays the acceleration, deceleration and speed algorithmic boost parameter for small distance PTP (point to point) motion.

PTPBoost Function

PTPBoostOK

PTPBoost Statement Example

PTPBoost 50, 30, 30


---

# PTPBoostOK Function
**Type:** function | **Section:** Operator

## Syntax
```
PTPBoostOK(targetPos)
```

## Parameters
targetPos	Point expression for the target position.

## Description
Use PTPBoostOK to the distance from the current position to the target position is small enough for PTPBoost to be effective.

## Examples
```spel
If PTPBoostOK(P1) Then
		  PTPBoost 50
		EndIf
```

```spel
Go P1
```

## See Also
Returns whether or not the PTP (Point to Point) motion from a current position to a target position is a small travel distance.

PTPBoost

PTPTBoostOK Function Example

If PTPBoostOK(P1) Then

		  PTPBoost 50

		EndIf

Go P1


---

# PTRQ Function
**Type:** function | **Section:** Operator

## Syntax
```
PTRQ(jointNumber)
```

## Parameters
jointNumber	Integer expression representing the joint number.

The additional S axis is 8 and T axis is 9.

## Description
PTRQ Function

PTRQ Function

## Examples
```spel
Function DisplayPeakTorque Integer i Print "Peak torques:" For i = 1 To 4
    Print "Joint ", i, " = ", PTRQ(i) Next i
Fend
```

## See Also
Returns the peak torque for the specified joint.

ATRQ

PTCLR

PTRQ Statement

PTRQ Function Example

This example uses the PTRQ function in a program:

Function DisplayPeakTorque

  Integer i

  Print "Peak torques:"

  For i = 1 To 4

    Print "Joint ", i, " = ", PTRQ(i)

  Next i

Fend


---

# PTRQ Keyword
**Type:** reference | **Section:** Operator

## Description
PTRQ Keyword

PTRQ Keyword

The PTRQ keyword is used in these contexts:

PTRQ Statement

PTRQ Function


---

# PTRQ Statement
**Type:** statement | **Section:** Operator

## Syntax
```
PTRQ  [jointNumber]
```

## Parameters
jointNumber	Optional.  Integer expression representing the joint number.

The additional S axis is 8 and T axis is 9.

## Description
Use PTRQ to display the peak torque value for one or all joints since the PTCLR statement was executed.

Peak torque is a real number from 0 to 1.

## Examples
```spel
> ptclr
> go p1
> ptrq 1
0.227
> ptrq
0.227    0.118
0.249    0.083
0.000    0.000
```

```spel
>
```

## See Also
Displays the peak torque for the specified joint.

ATRQ

PTCLR

PTRQ Function

PTRQ Statement Example

> ptclr

> go p1

> ptrq 1

0.227

> ptrq

0.227    0.118

0.249    0.083

0.000    0.000

>


---

# PTran Statement
**Type:** reference | **Section:** Operator

## Syntax
```
PTran joint, pulses
```

## Parameters
joint	Integer expression representing which joint to move.

The additional S axis is 8 and T axis is 9.

pulses	Integer expression representing the number of pulses to move.

## Description
Use PTran to move one joint a specifed number of pulses from the current position.

## Examples
```spel
PTran 1, 2000
```

## See Also
Go

JTran

Jump

Move

PTran Statement Example

PTran 1, 2000


---

# Pallet Function
**Type:** function | **Section:** Operator

## Syntax
```
(1) Pallet ( palletNumber, palletPosition )

(2) Pallet ( palletNumber, column, row )
```

## Parameters
palletNumber	Pallet number represented by integer expression from 0 to 15.

PalletPosition	The pallet position represented by an integer from 1 to 32767.

column	The pallet column represented by an integer expression from 1 to 32767.

row	The pallet row represented by an integer expression from 1 to 32767.

## Description
Palllet returns a position in a pallet which was previously defined by the Pallet statement. Use this function with motion commands such as Go and Jump to cause the arm to move to the specified pallet position.

The pallet position number can be defined arithmetically or simply by using an integer.

## Notes
Pallet Motion of 6 axis Robot (including N series)

When the 6-axis robot (including N series) moves to a point calculated by such as pallet or relative offsets, the wrist part may rotate to an unintended direction. The point calculation above does not depend on robot models and results in motion without converting the required point flag. LJM function prevents the unintended wrist rotation.

Pallet Motion of RS series

In the same way as the 6-axis, when the RS series robot moves to a point calculated by such as pallet or relative offsets, Arm #1 may rotate to an unintended direction. LJM function can be used to convert the point flag to prevent the unintended rotation of Arm #1.

In addition, the U axis of RS series may go out of the motion range when the orientation flag is converted, and it causes an error.

To prevent this error, LJM function adjusts the U axis target angle to inside the motion range. It is available when the orientation flag "2" is selected.

UVW Coordinate Values

When the UVW coordinate values of the 3 (or 4) points specified with the Pallet statement vary, the UVW coordinate values of the point 1 and the coordinate system data 1 are used.

The UVW coordinate values of the point numbers from 2 to 4 and the coordinate system numbers from 2 to 4 are ignored.

Additional Axes Coordinate Values

When the coordinate values of the 3 (or 4) points specified with the Pallet statement include the additional ST axis coordinate values, Pallet includes these additional coordinates in the position calcuations. In the case where the additional axis is used as the running axis, the motion of the running axis is considered and calculated with the Pallet definition. You need to define a pallet larger than the robot motion range considering the position of the running axis. Even if you define additional axes that are not affected by the pallet definition, be careful of the positions of additional axes when defining the pallet.

## Examples
```spel
Function main Integer index Pallet 1, P1, P2, P3, 3, 5 'Define pallet 1 Pallet 2, P12, P13, P11, 5, 3 'Define pallet 2 For index = 1 To 15
    Jump Pallet(1, index) 'Move to point index on pallet 1
    On 1 'Hold the workpiece
    Wait 0.5
    Jump Pallet(2, index) 'Move to point index on pallet 2
    Off 1 'Release the workpiece
    Wait 0.5 Next index
Fend
```

```spel
Function main Integer i, j P0 = XY(300, 300, 300, 90, 0, 180) P1 = XY(400, 0, 150, 90, 0, 180) P2 = XY(400, 500, 150, 90, 0, 180) P3 = XY(-400, 0, 150, 90, 0, 180) Pallet 1, P1, P2, P3, 10, 10 Motor On Power High Speed 50; Accel 50, 50 SpeedS 1000; AccelS 5000 Go P0 P11 = P0 - TLZ(50)
    For i = 1 To 10
      For j = 1 To 10
      'Specify points
         P10 = P11               'Depart point
         P12 = Pallet(1, i, j)   'Target point
         P11 = P12 -TLZ(50)      'Start approach point
         ' Converting each point to LJM
         P10 = LJM(P10)
         P11 = LJM(P11, P10)
         P12 = LJM(P12, P11)
         'Execute motion
         Jump3 P10, P11, P12 C0
       Next
      Next
Fend
Function main2 P0 = XY(300, 300, 300, 90, 0, 180) P1 = XY(400, 0, 150, 90, 0, 180) P2 = XY(400, 500, 150, 90, 0, 180) P3 = XY(-400, 0, 150, 90, 0, 180) Pallet 1, P1, P2, P3, 10, 10 Motor On Power High Speed 50; Accel 50, 50 SpeedS 1000; AccelS 5000 Go P0 Do
    ' Specify points
    P10 = Here -TLZ(50)                                'Depart point
    P12 = Pallet(1, Int(Rnd(9)) + 1, Int(Rnd(9)) + 1)   'Target point
    P11 = P12 -TLZ(50)                                  'Start approach point
    If TargetOK(P11) And TargetOK(P12) Then             'Point check
    ' Converting each point to LJM
    P10 = LJM(P10)
    P11 = LJM(P11, P10)
    P12 = LJM(P12, P11)
    ' Execute motion
      Jump3 P10, P11, P12 C0
    EndIf Loop
Fend
```

## See Also
LJM

Pallet Statement

Pallet Function Example

The following program transfers parts from pallet 1 to pallet 2.

Function main

  Integer index

  Pallet 1, P1, P2, P3, 3, 5 'Define pallet 1

  Pallet 2, P12, P13, P11, 5, 3 'Define pallet 2

  For index = 1 To 15

    Jump Pallet(1, index) 'Move to point index on pallet 1

    On 1 'Hold the workpiece

    Wait 0.5

    Jump Pallet(2, index) 'Move to point index on pallet 2

    Off 1 'Release the workpiece

    Wait 0.5

  Next index

Fend

Function main

  Integer i, j

  P0 = XY(300, 300, 300, 90, 0, 180)

  P1 = XY(400, 0, 150, 90, 0, 180)

  P2 = XY(400, 500, 150, 90, 0, 180)

  P3 = XY(-400, 0, 150, 90, 0, 180)

  Pallet 1, P1, P2, P3, 10, 10

  Motor On

  Power High

  Speed 50; Accel 50, 50

  SpeedS 1000; AccelS 5000

  Go P0

  P11 = P0 - TLZ(50)

    For i = 1 To 10

      For j = 1 To 10

      'Specify points

         P10 = P11               'Depart point

         P12 = Pallet(1, i, j)   'Target point

         P11 = P12 -TLZ(50)      'Start approach point

         ' Converting each point to LJM

         P10 = LJM(P10)

         P11 = LJM(P11, P10)

         P12 = LJM(P12, P11)

         'Execute motion

         Jump3 P10, P11, P12 C0

       Next

      Next

Fend

Function main2

  P0 = XY(300, 300, 300, 90, 0, 180)

  P1 = XY(400, 0, 150, 90, 0, 180)

  P2 = XY(400, 500, 150, 90, 0, 180)

  P3 = XY(-400, 0, 150, 90, 0, 180)

  Pallet 1, P1, P2, P3, 10, 10

  Motor On

  Power High

  Speed 50; Accel 50, 50

  SpeedS 1000; AccelS 5000

  Go P0

  Do

    ' Specify points

    P10 = Here -TLZ(50)                                'Depart point

    P12 = Pallet(1, Int(Rnd(9)) + 1, Int(Rnd(9)) + 1)   'Target point

    P11 = P12 -TLZ(50)                                  'Start approach point

    If TargetOK(P11) And TargetOK(P12) Then             'Point check

    ' Converting each point to LJM

    P10 = LJM(P10)

    P11 = LJM(P11, P10)

    P12 = LJM(P12, P11)

    ' Execute motion

      Jump3 P10, P11, P12 C0

    EndIf

  Loop

Fend


---

# Pallet Keyword
**Type:** reference | **Section:** Operator

## Description
Pallet Keyword

Pallet Keyword

The Pallet keyword is used in these contexts:

Pallet Statement

Pallet Function


---

# Pallet Statement
**Type:** statement | **Section:** Operator

## Syntax
```
Pallet [ Outside ,] [palletNumber, Pi, Pj, Pk [,Pm ], columns, rows ]
```

## Parameters
Outside	Optional.  Allow row and column indexes outside of the range of the specified rows and columns.

palletNumber	Pallet number represented by an integer number from 0 to 15.

Pi, Pj, Pk	Point variables which define standard 3 point pallet position.

Pm	Optional. Point variable which is used with Pi, Pj and Pk to define 4 point pallet.

columns	Integer expression representing the number of points on the Pi-to-Pj side of the pallet.  Range is from 1-32767.

rows	Integer expression representing the number of points on the Pi-to-Pk side of the pallet.  Range is from 1-32767.

## Description
Defines a pallet by teaching the robot, as a minimum, points Pi, Pj and Pk and by specifying the number of points from Pi to Pj and from Pi to Pk.

If the pallet is a well ordered rectangular shape, only 3 of the 4 corner points need to be specified.  However, in most situations it is better to use 4 corner points for defining a pallet.

To define a pallet, first teach the robot either 3 or 4 corner points, then define the pallet as follows:

A pallet defined with 4 points: P1, P2, P3 and P4 is shown below.  There are 3 positions from P1-P2 and 4 positions from P1-P3.  This makes a pallet which has 12 positions total.  To define this pallet the syntax is as follows:

Points that represent divisions of a pallet are automatically assigned division numbers, which, in this example, begin at P1.  These division numbers are also required by the Pallet Function.

When Outside is specified, row and column indexes outside of the range of rows and columns can be specified.  The Outside should be specified by two-dimensional division.  For example:

Pallet Outside 1, P1, P2, P3, 4, 5

Jump Pallet(1, -2, 10)

## Notes
The Maximum Pallet Size

The total number of points defined by a specific pallet must be less than 32,767.

Incorrect Pallet Shape Definitions

Be aware that incorrect order of points or incorrect number of divisions between points will result in an incorrect pallet shape definition.

Pallet Plane Definition

The pallet plane is defined by the Z axis coordinate values of the 3 corner points of the pallet.  Therefore, a vertical pallet could also be defined.

Pallet Definition for a Single Row Pallet

A single row pallet can be defined with a 3 point Pallet statement or command.  Simply teach a point at each end and define as follows: Specify 1 as the number of divisions between the same point.

> Pallet 2, P20, P21, P20, 5, 1 'Defines a 5x1 pallet

UVW Coordinate Values

When the UVW coordinate values of the 3 (or 4) points specified with the Pallet statement vary, the UVW coordinate values of the point 1 and the coordinate system data 1 are used.

The UVW coordinate values of the point numbers from 2 to 4 and the coordinate system numbers from 2 to 4 are ignored.

Additional Axes Coordinate Values

When the coordinate values of the 3 (or 4) points specified with the Pallet statement include the additional ST axis coordinate values, Pallet includes these additional coordinates in the position calcuations. In the case where the additional axis is used as the running axis, the motion of the running axis is considered and calculated with the Pallet definition. You need to define a pallet larger than the robot motion range considering the position of the running axis. Even if you define additional axes that are not affected by the pallet definition, be careful of the positions of additional axes when defining the pallet.

## Examples
```spel
Pallet Outside 1, P1, P2, P3, 4, 5
```

```spel
Jump Pallet(1, -2, 10)
```

```spel
> pallet 1, P1, P2, P3, 3, 5
> jump pallet(1, 2) 'Jump to position on pallet
```

## See Also
Pallet Function

Pallet Statement Example

The following instruction from the command window sets the pallet defined by P1, P2 and P3 points, and divides the pallet plane into 15 equally distributed pallet point positions, with the pallet point number 1, the pallet point number 2 and the pallet point number 3 sitting along the P1-to-P2 side.

> pallet 1, P1, P2, P3, 3, 5

> jump pallet(1, 2) 'Jump to position on pallet

The resulting Pallet is shown below:


---

# Pallets page: Robot Manager Window
**Type:** reference | **Section:** Operator

## Description
Pallets page: Robot Manager Window

[Tools]-[Robot Manager]-[Pallets] Page

This page allows you to define the pallet (Pallet). When the page is selected, values for the available pallet are displayed. When a Pallet is undefined, then all fields for the Pallet will be blank. The Pallet will be defined when you press the [Apply] button.

For more details on Pallet settings, refer to the following manual:

SPEL+ Language Reference - Pallet Statement

Navigating the grid

Press the [Tab] key to move to the next cell. Press the [Shift] + [Tab] key to move to the previous cell. Press the arrow [↑] or [↓] key to move to the cell above or below.

Item	Description

Points	Specify
		 the point variable to use for pallet definition.

Select either 3 or 4.

Columns	Specify
		 the division number of Point number 1(coordinate system data 1)
		 and Point number 2 (coordinate system data 2) by an integer.

		The range is from 1 to 32767. (Division 1 x Division 2 <32767)

Rows	Specify
		 the division number of Point number 1(coordinate system data 1)
		 and Point number 3 (coordinate system data 3) by an integer.

		The range is from 1 to 32767. (Division 1 x Division 3 <32767)

Outside	Creates
		 an accessible pallet outside the specified columns and rows. Optional.

X	Set the
		 X coordinate in millimeters.

Y	Set the
		 Y coordinate in millimeters.

Z	Set the
		 Z coordinate in millimeters.

U	Set the
		 U coordinate in degrees.

V	Set the
		 V coordinate in degrees.

W	Set the
		 W coordinate in degrees.

Apply	Sets
		 the current values.

Restore	Reverts
		 to the previous values.

Clear	Clears
		 all values.

Wizard

Select [Robot Manager]-[Pallets] tab to show the [Pallets] page.

(2)   Click the [Pallet Wizard] button. The following dialog appears.

(3)      Select the pallet number to define, the number of points to teach, the number of rows and columns, and whether to use "Outside". Then, click the [Next] button.

NOTE:  If a pallet is a well ordered rectangular shape, only 3 of the 4 corner points should be specified. However, in most situations, it is recommended to use 4 corner points to define a pallet.

(4)      Click the [Teach] button to show the [Teach first point] page.

NOTE:  You can proceed to the next step without teaching if a predefined pallet number is selected.

When doing so, only teach the points that require re-teaching.

(5)    Jog the robot to the first corner to teach the position of it. Click the [Teach] button. The following dialog will appear.

(6)    Teach the second to forth corners by following the steps (4) and (5).

(7)    The new pallet definition is displayed as shown below. Click [Finish] to apply the new definition.


---

# Parallel Processing
**Type:** reference | **Section:** Operator

## Syntax
```
motionCmd ! statements !
```

## Parameters
motionCmd	Any valid motion command included in the following list: Arc, Arc3, Go, Jump, Jump3, Jump3CP, Move, BGo, BMove, TGo, TMove.

statements	Any valid parallel processing I/O statement(s) which can be executed during motion. (See table below.)

## Description
Parallel processing commands are attached to motion commands to allow I/O statements to execute simultaneously with the beginning of motion travel. This means that I/O can execute while the arm is moving rather than always waiting for arm travel to stop and then executing I/O. There is even a facility to define when within the motion that the I/O should begin execution. (See the Dn parameter described in the table below.)

The table below shows all valid parallel processing statements. Each of these statements may be used as single statements or grouped together to allow multiple I/O statements to execute during one motion statement.

Dn	Used to specify %travel before a parallel statement is executed. Statements which follow the Dn parameter will begin execution after n% of the motion travel has been completed.

When used with the Jump, Jump3, and Jump3CP commands, %travel does not include depart and approach motion. To execute statements after the depart motion has completed, include D0 (zero) at the beginning of the statement.

Dn may appear a maximum of 16 times in a parallel processing statement.

On / Off n	Turn Output bit number n On or Off.

MemOn / MemOff n	Turns memory I/O bit number n on or off.

Out p,d OpBCD p,qOutW p,d	Outputs data d to output port p.

MemOut p, d

MemOutW p,d	Outputs data d to memory output port p

Signal s	Generates synchronizing signal.

Wait t	Delays for t seconds prior to execution of the next parallel processing statement.

WaitSig s	Waits for signal s before processing next statement.

Wait Sw(n) = j	Delays execution of next parallel processing statement until the input bit n is equal to the condition defined by j. (On or Off)

Wait MemSw(n) = j	Delays execution of the next parallel processing statement until the memory I/O bit n is equal to the condition defined by j. (On or Off)

Wait Other Conditions	Wait other than the above two patterns is available. Refer to Wait Statement for details.

Print	Prints data to the display device.

Print #	Prints data to the specified communications port.

External Functions	Executes the external functions declared with Declare statement.

Hand_On n

Hand_Off n	Executes Hand_On/Hand_Off operation of hand number "n".

## Notes
When Motion is Completed before All I/O Commands are Complete

If, after completing the motion for a specific motion command, all parallel processing statement execution has not been completed, subsequent program execution is delayed until all parallel processing statements execution has been completed. This situation is most likely to occur with short moves with many I/O commands to execute in parallel.

When the Till statement is used to stop the arm before completing the intended motion

If Till is used to stop the arm at an intermediate travel position, the system considers that the motion is completed. The next statement execution is delayed until the execution of all parallel processing statements has been completed.

When the AbortMotion statement or Trap is used to stop the arm before completing the motion

After the arm stops at an intermediate travel position, D statement cannot be executed.

Specifying n near 100% can cause path motion to decelerate

If a large value of n is used during CP motion, the robot may decelerate to finish the current motion. This is because the position specified would normally be during deceleration if CP was not being used. To avoid deceleration, consider placing the processing statement after the motion command. For example, in the example below, the On 1 statement is moved from parallel processing during the jump to P1 to after the jump.

CP On

Jump P1 !D96; On 1!

Go P2

CP On

Jump P1

On 1

Go P2

The Jump statement and Parallel Processing

Note that execution of parallel processing statements which are used with the Jump statement begins after the rising motion has completed and ends at the start of falling motion.

The Here statement and Parallel Processing

You cannot use both of the Here statement and parallel processing in one motion command like this:

Go Here :Z(0) ! D10; MemOn 1 !

Be sure to change the program like this:

P999 = Here

Go P999 Here :Z(0) ! D10; MemOn 1 !

## Examples
```spel
CP On
Jump P1 !D96; On 1!
Go P2
```

```spel
CP On
Jump P1
On 1
Go P2
```

```spel
Go Here :Z(0) ! D10; MemOn 1 !
```

```spel
P999 = Here
```

```spel
Go P999 Here :Z(0) ! D10; MemOn 1 !
```

```spel
Function test Jump P1 !D0; On 1; D50; Off 1!
Fend
```

```spel
Function test2 Move P1 !D10; On 5; Wait 0.5; Off 5!
Fend
```

## See Also
Arc, Arc3, Go, Jump, Jump3, Jump3CP, Move, Pulse

!...! Parallel Processing Example

The following examples show various ways to use the parallel processing feature with Motion Commands:.

Parallel processing with the Jump command causes output bit 1 to turn on at the end of the Z joint rising travel and when the 1st, 2nd, and 4th axes begin to move. Then output bit 1 is turned off again after 50% of the Jump motion travel has completed.

Function test

  Jump P1 !D0; On 1; D50; Off 1!

Fend

Parallel processing with the Move command causes output bit 5 to turn on when the joints have completed 10% of their move to the point P1. Then 0.5 seconds later turn output bit 5 off.

Function test2

  Move P1 !D10; On 5; Wait 0.5; Off 5!

Fend


---

# Pass Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Pass point [, {On | Off | MemOn | MemOff} bitNumber [, point ... ] [LJM [orientationFlag]]
```

## Parameters
point	P number or P(expr) or point label.

When the point data is continued and in the ascending order or the descending order, specify two point numbers binding with colon as P(1:5).

bitNumber	The I/O bit or memory I/O bit to turn on or off. Integer number between 0 - 511 or output label.

LJM	Optional. Convert the depart point, approach point, and target destination using LJM function.

orientationFlag	Optional. Specifies a parameter that selects an orientation flag for LJM function.

## Description
Pass moves the robot arm near but not through the specified point series.

To specify a point series, use points (P0, P1, ...) with commas between points.

To turn output bits on or off while executing motion, insert an On or Off command delimited with commas between points.  The On or Off is executed before the robot reaches the point immediately preceding the On or Off.

If Pass is immediately followed by another Pass, control passes to the following Pass without the robot stopping at the preceding Pass final specified point.

If Pass is immediately followed by a motion command other than another Pass, the robot stops at the preceding Pass final specified point, but Fine positioning will not be executed.

If Pass is immediately followed by a command, statement, or function other than a motion command, the immediately following command, statement or function will be executed prior to the robot reaching the final point of the preceding Pass.

If Fine positioning at the target position is desired, follow the Pass with a Go, specifying the target position as shown in the following example:

Pass P5; Go P5; On 1; Move P10

The larger the acceleration / deceleration values, the nearer the arm moves toward the specified point.  The Pass instruction can be used such that the robot arm avoids obstacles.

With LJM parameter, the program using LJM function can be more simple.

For example, the following four-line program

P11 = LJM(P1, Here, 1)

P12 = LJM(P2, P11, 1)

P13 = LJM(P3, P12, 1)

Pass P11, P12, P13

can be... one-line program.

Pass P1, P2, P3 LJM 1

LJM parameter is available for 6-axis (including N series) and RS series robots.

When using orientationFlag with the default value, it can be omitted.

Pass P1, P2, P3 LJM

## Examples
```spel
P11 = LJM(P1, Here, 1)
```

```spel
P12 = LJM(P2, P11, 1)
```

```spel
P13 = LJM(P3, P12, 1)
```

```spel
Pass P11, P12, P13
```

```spel
Pass P1, P2, P3 LJM 1
```

```spel
Pass P1, P2, P3 LJM
```

```spel
Function main Jump P1 Pass P2 'Move the arm toward P2, and perform 'the next instruction before reaching P2. On 2 Pass P3 Pass P4 Off 0 Pass P5
Fend
```

## See Also
Accel

Go

Jump

Speed

Pass Statement Example

The example shows the robot arm manipulation by Pass instruction:

Function main

  Jump P1

  Pass P2 'Move the arm toward P2, and perform

  'the next instruction before reaching P2.

  On 2

  Pass P3

  Pass P4

  Off 0

  Pass P5

Fend


---

# Pause Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Pause
```

## Description
When the Pause is executed, program execution for all tasks with pause enabled (tasks that does not use NoPause or NoEmgAbort in Xqt command) is suspended.  Also, if any task is executing a motion statement, it will be paused even if pause is not enabled for that task.

However, Pause cannot stop the background tasks.

## Notes
QP and its Affect on Pause:

The QP instruction is used to cause the arm to stop immediately upon Pause or to complete the current move and then Pause the program.  See the QP instruction help for more information.

Pause Statement Example

The example below shows the use of the Pause instruction to temporarily stop execution. The task executes program statements until the line containing the Pause command. At that point the task is paused. The user can then click the Run Window Continue Button to resume execution.

Function main

		  Xqt monitor

		  Go P1

		  On 1

		  Jump P2

		  Off 1

Pause 'Suspend program execution

		  Go P40

		  Jump P50

		Fend

## Examples
```spel
Function main
		  Xqt monitor
		  Go P1
		  On 1
		  Jump P2
		  Off 1

			  Pause 'Suspend program execution
		  Go P40
		  Jump P50
		Fend
```


---

# PauseOn Function
**Type:** reference | **Section:** Operator

## Syntax
```
PauseOn
```

## Description
PauseOn function is used only for NoPause and NoEmgAbort task (special task using NoPause or NoEmgAbort at Xqt), and background tasks.

The following example shows a program that monitors the controller pause and switches the I/O On/Off when pause occurs. However, when the status changes to pause by Safety Door open, the I/O does not turn On/Off.

Function main

  Xqt PauseMonitor, NoPause

  ..

  ..

Fend

Function PauseMonitor

  Boolean IsPause

  IsPause = False

  Do

    Wait 0.1

    If SafetyOn = On Then

      If IsPause = False Then

        Print "Saftey On"

         IsPause = True

      EndIf

     ElseIf PauseOn = On Then

       If IsPause = False Then

         Print "InPause"

         If SafetyOn = Off Then

           Off 10

           On 12

         EndIf

         IsPause = True

       EndIf

    Else

      If IsPause = True Then

            Print "OutPause"

        On 10

        Off 12

        IsPause = False

      EndIf

    EndIf

  Loop

Fend

## Examples
```spel
Return Valuesor signal."
EndIf
```

```spel
Function main Xqt PauseMonitor, NoPause .. ..
Fend
Function PauseMonitor Boolean IsPause IsPause = False Do
    Wait 0.1
    If SafetyOn = On Then
      If IsPause = False Then
        Print "Saftey On"
         IsPause = True
      EndIf
     ElseIf PauseOn = On Then
       If IsPause = False Then
         Print "InPause"
         If SafetyOn = Off Then
           Off 10
           On 12
         EndIf
         IsPause = True
       EndIf
    Else
      If IsPause = True Then
            Print "OutPause"
        On 10
        Off 12
        IsPause = False
      EndIf
    EndIf Loop
Fend
```

## See Also
ErrorOn

EstopOn

Xqt

PauseOn Function Example


---

# PeakForces Result
**Type:** result | **Section:** Operator

## Description
Returns average values of force and torque during execution of a force guide object.

## Notes
Returns the peak values of force and torque during execution of a force guide object or force guide sequence.

Peak value is the largest absolute value of the force and torque during execution of a force guide object or a force guide sequence.

If the number of elements in a specified array variable is less than six, returns force and torque in each direction for the defined element numbers.  Also, if the number of elements in the array variable exceeds six, returns force and torque in each direction from element number 0 to 5, while making no change to element number 6 and above.

## Examples
```spel
Function PeakForceTest
     Double dArray(6)
     Motor On
     FGRun Sequence1
     FGGet Sequence1.Contact01.PeakForces, dArray()  ' Acquisition of PeakForces
    Print dArray(FG_FX)
Fend
```

## See Also
FGGet


---

# Plane
**Type:** reference | **Section:** Operator

## Syntax
```
(1) Plane PlaneNum, [robotNumber], pCoordinateData

(2) Plane PlaneNum, [robotNumber], pOrigin, pXAxis, pYAxis

(3) Plane PlaneNum, [robotNumber],

(4) Plane
```

## Parameters
planeNumber	Integer expression
		 representing the plane number from 1 to 15.

robotNumber	Integer values
		 representing the robot number

If omitted,
		 the current robot is used.

pCoordinateData	Point data
		 representing the coordinate data of the approach check plane.

pOrigin	Integer expression
		 representing the origin point using the robot coordinate system.

pXAxis	Integer expression
		 representing a point along the X axis using the robot coordinate
		 system if X alignment is specified.

pYAxis	Integer expression
		 representing a point along the Y axis using the robot coordinate
		 system if Y alignment is specified.

## Description
Plane is used to set the approach check plane. The approach check plane is for checking whether the robot end effector is in one of the two areas devided by the specified approach check plane. The position of the end effector is calculated by the current tool. The approach check plane is set using the XY plane of the base coordinate system. The approach check plane detects the end effector when it approaches the area on the + Z side of the the approach check plane.

When the approach check plane is used, the system detects approaches in any motor power status during the controller is ON.

The details of each syntax are as follows.

(1) Specifies a coordinate system to create the approach check plane using the point data representing the translation and rotation based on the base coordinate system, and sets the approach check plane.

## Examples
```spel
> plane 1, xy(100, 200, -20, 90, 0, 180)
```

```spel
> plane 2, xy(50, 200, 0, 0, 45, 0)
```

```spel
> plane 3, here
```

## See Also
Specifies and displays the approach check plane.

Box

GetRobotInsidePlane

InsidePlane

PlaneClr

PlaneDef

Plane Statement


---

# PlaneClr
**Type:** reference | **Section:** Operator

## Syntax
```
PlaneClr PlaneNum, [ robotNumber ]
```

## Parameters
PlaneNum	Integer expression representing the plane number from 1 to 15.

robotNumber	Integer value representing the robot number

If omitted, the current robot is used.

## Description
Robot parameter data is stored in compact flash in controller.  Therefore, writing to command flash occurs when executing this command.  Frequent writing to compact flash affect to lifetime of compact flash.  We recommend to use this command minimally.

## Examples
```spel
PlaneClr 1
```

## See Also
Clears (undifines) a Plane definition.

GetRobotInsidePlane

InsidePlane

Plane

PlaneDef

PlaneClr Statement Example

PlaneClr 1


---

# PlaneDef
**Type:** reference | **Section:** Operator

## Syntax
```
PlaneDef (PlaneNum,
			[
			robotNumber
			]
			)
```

## Parameters
PlaneNum	Integer expression representing the plane number from 1 to 15.

robotNumber	Integer value representing the robot number

If omitted, the current robot is used.

## Description
PlaneDef

PlaneDef Function

## Examples
```spel
Function DisplayPlaneDef(planeNum As Integer)

		  If PlaneDef(planeNum) = False Then

		    Print "Plane ", planeNum, "is not defined"

		  Else

		    Print "Plane 1: ",

		    Print Plane(PlaneNum)

		   EndIf
		Fend
```

## See Also
Returns the setting of the approach check plane.

GetRobotInsidePlane

InsidePlane

Plane

PlaneClr

PlaneDef Function Example

Function DisplayPlaneDef(planeNum As Integer)

		  If PlaneDef(planeNum) = False Then

		    Print "Plane ", planeNum, "is not defined"

Else

Print "Plane 1: ",

		    Print Plane(PlaneNum)

		   EndIf

		Fend


---

# Plist Command
**Type:** reference | **Section:** Operator

## Syntax
```
(1) PList

(2) PList
			pointNumber

(3) PList
			startPoint,

(4) PList
			startPoint,  endPoint
```

## Parameters
pointNumber	The number range is 0 to 999.

StartPoint	The start point number. The number range is 0 to 999.

EndPoint	The end point index. The number range is 0 to 999.

## Description
Plist displays point data in memory for the current robot.

When there is no point data within the specified range of points, no data will be displayed.

When a start point number is specified larger than the end point number, then an error occurs.

(1) PList

Displays the coordinate data for all points.

(2) PList pointIndex

Displays the coordinate data for the specified point.

(3) PList startPoint,

Displays the coordinate data for all points starting with startPoint.

(4) PList startPoint,  endPoint

Displays the coordinate data for all points starting with startPoint and ending with endPoint.

Plist Example

Display type depends on the robot type and existence of additional axes.

The following examples are for a Scara robot without additional axes.

Displays the specified point data:

> plist 1

P1   = XY(
   200.000,
    0.000,
  -20.000,
    0.000) /R /0

>

This one displays the point data within the range of 10 and 20. In this example, only three points are found in this range.

> plist 10, 20

P10  = XY(
   290.000,
    0.000,
  -20.000,
    0.000) /R /0

P12  = XY(
   300.000,
    0.000,
    0.000,
    0.000) /R /0

P20  =
   XY(285.000,
   10.000,
  -30.000,
   45.000) /R /0

>

This example displays the point data starting with point number 10.

> plist 10,

P10  =
   XY(290.000,
    0.000,
  -20.000,
    0.000) /R /0

P12  =
   XY(300.000,
    0.000,
    0.000,
    0.000) /R /0

P20  =
   XY(285.000,
   10.000,
  -30.000,
   45.000) /R /0

P30  = XY(
   310.000,
   20.000,
  -50.000,
   90.000) /R /0

## Examples
```spel
> plist 1
```

```spel
P1   = XY(
   200.000,
    0.000, -20.000,
    0.000) /R /0
```

```spel
>
```

```spel
> plist 10, 20
```

```spel
P10  = XY(
   290.000,
    0.000, -20.000,
    0.000) /R /0
```

```spel
P12  = XY(
   300.000,
    0.000,
    0.000,
    0.000) /R /0
```

```spel
P20  =
   XY(285.000,
   10.000, -30.000,
   45.000) /R /0
```

```spel
>
```

```spel
> plist 10,
```

```spel
P10  =
   XY(290.000,
    0.000, -20.000,
    0.000) /R /0
```

```spel
P12  =
   XY(300.000,
    0.000,
    0.000,
    0.000) /R /0
```

```spel
P20  =
   XY(285.000,
   10.000, -30.000,
   45.000) /R /0
```

```spel
P30  = XY(
   310.000,
   20.000, -50.000,
   90.000) /R /0
```


---

# Pls Function
**Type:** reference | **Section:** Operator

## Syntax
```
Pls
			(jointNumber)
```

## Parameters
jointNumber	The specific joint for which to get the current encoder pulse count.

The additional S axis is 8 and T axis is 9.

## Description
Pls is used to read the current encoder position (or Pulse Count) of each joint. These values can be saved and then used later with the Pulse command.

## Examples
```spel
Function plstest
		  Real t1, t2, z, u
		  t1 = pls(1)
		  t2 = pls(2)
		  z = pls(3)
		  u = pls(4)
		  Print "T1 joint current Pulse Value: ", t1
		  Print "T2 joint current Pulse Value: ", t2
		  Print "Z joint current Pulse Value: ", z
		  Print "U joint current Pulse Value: ", u
		Fend
```

## See Also
Agl

CX, CY, CZ, CU, CV, CW, CR, CS, CT Keywords

PAgl

Pulse

Pls Function Example

Shown below is a simple example to get the pulse values for each joint and print them.

Function plstest

		  Real t1, t2, z, u

		  t1 = pls(1)

		  t2 = pls(2)

		  z = pls(3)

		  u = pls(4)

		  Print "T1 joint current Pulse Value: ", t1

		  Print "T2 joint current Pulse Value: ", t2

		  Print "Z joint current Pulse Value: ", z

		  Print "U joint current Pulse Value: ", u

		Fend


---

# Point to point motion
**Type:** reference | **Section:** Operator

## Description
Point to point motion

Point to point motion

Point to point (PTP) commands move the tool center point of the robot from its current position to a specified point. Motion of the tool center point may not be in a straight line.

To set the speed for point to point commands, use the Speed command.  To set acceleration and deceleration, use the Accel command.

Command	Description

Go	Move directly to a point using point
		 to point motion.

Jump	Jump to a
		 point. First move up to the current LimZ
		 setting, the move over the destination point, then move to the
		 point. (From the current position, the third axis is moved up
		 to the uppermost point (Z=0). A lateral orientation move is performed
		 to above the specified target position, and the third axis is
		 then lowered to the target position.) The Arch table settings
		 determine the Jump profile.

Jump3	Jump to a point in 3 dimensions. Move
		 in a straight line with the same orientation until the recede
		 point. The motion between the recede points is PTP motion.

Pass	Move near one or more points.

TGo	Move directly to a point in a tool coordinate
		 system.

BGo	Move in a PTP motion to the relative
		 specified point in Base / Local coordinate system


---

# Points page: Robot Manager command (Tools menu)
**Type:** reference | **Section:** Operator

## Description
Points page: Robot Manager command (Tools menu)

[Tools]-[Robot Manager]-[Points] Page

You can input/delete the point data.

When a point file is selected, the robot controller loads the file into memory.

As points are taught on the [Robot Manager]-[Jog & Teach] page, the spreadsheet on the Points page is updated.

For details on how to save points, refer to Saving your work.

Navigating the grid

Press the [Tab] key to move to the next cell. Press the [Shift] + [Tab] key to move to the previous cell. Press the arrow [↑] or [↓] key to move to the cell above or below.

Item	Description

Show
		 only registered	Only
		 shows registered point data.

Find
		 label.

Delete
		 Pxxx	Deletes
		 the selected point. You will be prompted to confirm the operation.

Delete
		 All	Deletes
		 all points in the file.

		You will be prompted to confirm the operation.

Save	Saves
		 the current values.

Restore	Reverts
		 to the previous values. You will be prompted to confirm the operation.


---

# PosFound Function
**Type:** reference | **Section:** Operator

## Syntax
```
PosFound
```

## Description
PosFound Function

PosFound Function

See_Also Example

Returns status of Find operation.

## Examples
```spel
Find Sw(5) = ON
		Go P10 Find
		If PosFound Then
		  Go FindPos
		Else
		  Print "Error: Cannot find the sensor signal."
		EndIf
```

## See Also
Find

PosFound Function Example

Find Sw(5) = ON

		Go P10 Find

		If PosFound Then

		  Go FindPos

		Else

		  Print "Error: Cannot find the sensor signal."

		EndIf


---

# Power Function
**Type:** function | **Section:** Operator

## Syntax
```
Power
```

## Description
Power Function

Power Function

See_Also Example

Returns status of power.

## Examples
```spel
If Power = 0 Then
		  Print "Low Power Mode"
		EndIf
```

## See Also
Power Statement

Power Function Example

If Power = 0 Then

		  Print "Low Power Mode"

		EndIf


---

# Power Keyword
**Type:** reference | **Section:** Operator

## Description
Power Keyword

Power Keyword

The Power keyword is used in these contexts:

Power Statement

Power Function


---

# Power Statement
**Type:** statement | **Section:** Operator

## Syntax
```
Power { High | Low } [,Forced]

Power
```

## Parameters
High | Low	The setting
		 can be High or Low. The default is Low.

Forced	Optional.
		  This parameter is usually omitted.

## Description
Switches Power Mode to High or Low. It also displays the current mode status.

Low - When Power is set to Low, Low Power Mode is On. This means that the robot will run slow (below 250 mm/sec) and the servo stiffness is set light so as to remove servo power if the robot bumps into an object. This is the normal mode of operation for teaching points.

High - When Power is set to High, Low Power Mode is Off. This means that the robot can run at full speed with the full servo stiffness. This is the normal mode of operation for running actual applications.

The following operations will switch to low power mode.  In this case, speed and acceleration settings will be limited to the default value.
  The default value is described in the each manipulator specification table.  See also the Epson RC+ Users Guide: 2. Sefety.

Conditions to cause Power Low:

Controller Startup

Controller Startup

Motor On

		SFree,  SLock, Brake

		Reset, Reset Error

		Stop button or Quit All stops tasks

Settings limited to the default value

Speed

		Accel

		SpeedS

		AccelS

## Notes
Low Power Mode (Power Low) and Its Effect on Max Speed:

In low power mode, motor power is limited, and effective motion speed setting is lower than the default value. If, when in Low Power mode, a higher speed is specified from the command window (directly) or in a program, the speed is set to the default value. If a higher speed motion is required, set Power High.

If you switched to low power mode while the manipulator operating in high power mode, overspeed error or low power torque error may occur.

High Power Mode (Power High) and Its Effect on Max Speed:

In high power mode, higher speeds than the default value can be set.

Forced Flag

The power mode can be changed during robot operation (including the pause state).

If the mode is switched to high power mode while the robot is moving in low power mode, the subsequent motion will be changed to high speed with the specified speed.

If the mode is switched to low power mode while the robot is moving in high power mode, the overspeed error or low power torque error may occur.

Stop the robot and specify the Forced flag to switch to low power mode.

## Examples
```spel
> Speed 50 'Specifies high speed in Low Power mode
```

```spel
> Accel 100, 100 'Specifies high accel
```

```spel
> Jump P1 'Moves in low speed and low accel
```

```spel
> Speed 'Display current speed values
```

```spel
Low Power Mode
```

```spel
50
```

```spel
50 50
```

```spel
> Accel 'Display current accel values
```

```spel
Low Power Mode
```

```spel
100 100
```

```spel
100 100
```

```spel
100 100
```

```spel
> Power High 'Set high power mode
```

```spel
> Jump P2 'Move robot at high speed
```

## See Also
Accel

Speed

Power Statement


---

# Pressing Motion
**Type:** reference | **Section:** Operator

## Description
Pressing Motion

Pressing Motion

To use the pressing motion, use the following torque control mode commands.

TC	(Returns the torque control mode setting
		 and current mode.)

TCSpeed	(Specifies / returns the speed limit
		 in the torque control.)

TCLim	(Specifies the torque limit of each
		 joint for the torque control mode.)

The low power mode is limited by a low power upper limit. Therefore, normally use the High power mode. For details and command usage, refer to the following manual:

SPEL+ Language Reference
  TC, TCSpeed, TCLim


---

# Print # Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Print #portNumber,  [expression [ , expression... ]
```

## Parameters
portNumber	ID number representing a file, communications port, database, or device.

File number can be specified in ROpen, WOpen, and AOpen statements.

Communications port number can be specified in OpenCom (RS232) and OpenNet (TCP/IP) statements.

Database number can be specified in OpenDB statement.

Device ID integers are as follows.

21 RC+

24 TP (TP1 only)

20 TP3

expression	Optional.  A number or string expression.

, (comma)	Optional.  If a comma is provided at the end of the statement, then a CRLF will not be added.

## Description
Print # outputs variable data, numerical values, or character strings to the communication port specified by portNumber .

Note

Maximum data length

This command can handle up to 256 bytes.

However, if the target is a database, it can handle up to 4096 bytes.

If the target is the communications port (TCP/IP), it can handle up to 1024 bytes.

Exchange variable data with other controller

When more than one string variable or both of numeric variable and string variable is specified, a comma (",") character has to be added expressly to the string data.

Sending end (Either pattern is OK.)

Print #PortNum, "$Status,", InData, OutData

Print #PortNum, "$Status", ",",InData, OutData

Receiving end

Input #PortNum, Response$, InData, OutData

File write buffering

File writing is buffered. The buffered data can be written with Flush statement. Also, when closing a file with Close statement, the buffered data can be written.

Be sure to use Print # with Wait command or a motion command within a loop

Do not use only Print # in a loop

The Controller may freeze up if only Print # is used in loop (loops with no Wait or no motion).

Depending on the Controller status, information may not be displayed properly even if the Wait command or a motion command is used.  If the output is TP1, set Wait time to 1 (seconds) or more.  In other cases, set Wait time to 0.1 (seconds) or more.

Bad example

Do

    Print #24，"1234"

Loop

Good example

Do

    Print #24,"1234"

    Wait 1

Loop

## Examples
```spel
Print #PortNum, "$Status,", InData, OutData
```

```spel
Print #PortNum, "$Status", ",",InData, OutData
```

```spel
Input #PortNum, Response$, InData, OutData
```

```spel
Do
```

```spel
Print #24，"1234"
```

```spel
Loop
```

```spel
Do
```

```spel
Print #24,"1234"
```

```spel
Wait 1
```

```spel
Loop
```

```spel
Function printex String temp$ Print #1, "5" 'send the character "5" to serial port 1 temp$ = "hello" Print #1, temp$ Print #2, temp$ Print #1, " Next message for " + Chr$(34) + "port 1" + Chr$(34) Print #2, " Next message for " + Chr$(34) + "port 2" + Chr$(34)
Fend
```

## See Also
Input #

Print

Write

WriteBin

Print # Statement Example

The following are some simple Print # examples:

Function printex

  String temp$

  Print #1, "5" 'send the character "5" to serial port 1

  temp$ = "hello"

  Print #1, temp$

  Print #2, temp$

  Print #1, " Next message for " + Chr$(34) + "port 1" + Chr$(34)

  Print #2, " Next message for " + Chr$(34) + "port 2" + Chr$(34)

Fend


---

# Print Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Print [expression [ , expression... ] [ , ]
```

## Parameters
expression	Optional. A number or string expression.

, (comma)	Optional. If a comma is provided at the end of the statement, then a CRLF will not be added.

## Description
Print displays variable data or character strings on the display device.

An end of line CRLF (carriage return and line feed) is automatically appended to each output unless a comma is used at the end of the statement.

## Notes
This command can handle up to 256 bytes.

Make sure Print is used with a Wait or a motion within a loop

Tight loops (loops with no Wait or no motion) are generally not good, especially with Print.

The controller may freeze up in the worst case.

Be sure to use Print with Wait command or a motion command within a loop.

Bad Example

    Do

       Print "1234"

    Loop

Good example

    Do

       Print "1234"

       Wait 0.1

    Loop

## Examples
```spel
Function test Real uvar uvar = CU(P100) Print "The U Axis Coordinate of " + Chr$(34) + "P100" + Chr$(34) + " is ", uvar
Fend
```

## See Also
Print #

Print Statement Example

The following example extracts the U Axis coordinate value from a Point P100 and puts the coordinate value in the variable uvar the value is then printed to the current display window.

Function test

  Real uvar

  uvar = CU(P100)

  Print "The U Axis Coordinate of " + Chr$(34) + "P100" + Chr$(34) + " is ", uvar

Fend


---

# Pulse Function
**Type:** function | **Section:** Operator

## Syntax
```
Pulse ( J1, J2, J3, J4 , [J5 , J6] , [J7] , [J8 , J9] )
```

## Parameters
J1, J2, J3, J4	The pulse value for joints 1 to 4.  The pulse value must be within the range defined by the Range instruction and should be an integer or long expression.

J5, J6	Optional.  For 6-axis robots (including N series) and Joint type 6-axis robots.

J7	Optional. For Joint type 7-axis robots.

J8, J9	Optional. For the additional axis.

## Description
Pulse Function

Pulse Function

See_Also Example

Returns a robot point whose coordinates are specified in pulses.

## Examples
```spel
Jump Pulse(1000, 2000, 0, 0)
```

## See Also
Go, JA, Jump, Move, Pulse Statement, XY

Pulse Function Example

Jump Pulse(1000, 2000, 0, 0)


---

# Pulse Keyword
**Type:** reference | **Section:** Operator

## Description
Pulse Keyword

Pulse Keyword

The Pulse keyword is used in these contexts:

Pulse Statement

Pulse Function


---

# Pulse Statement
**Type:** statement | **Section:** Operator

## Syntax
```
(1) Pulse    J1 , J2 , J3 , J4 , [J5, J6] , [J7] , [J8, J9]

(2) Pulse
```

## Parameters
J1, J2, J3, J4	The pulse value for each of the four joints.  The pulse value has to be within the range defined by the Range instruction and should be an integer or long expression.

J5, J6	Optional.  For 6-axis robots (including N series) and Joint type 6-axis robots.

J7	Optional. For Joint type 7-axis robots.

J8, J9	Optional. For the additional axis.

## Description
Pulse uses the joint pulse value from the zero pulse position to represent the robot arm position, rather than the orthogonal coordinate system.  The Pulse instruction moves the robot arm using point to point motion.

The Range instruction sets the upper and lower limits used in the Pulse instruction.

Note

Make Sure Path is Obstacle Free Before Using Pulse

Unlike Jump, Pulse moves all axes simultaneously, including Z joint raising and lowering in traveling to the target position. Therefore, when using Pulse, take extreme care so that the hand can move through an obstacle free path.

Potential Errors

Pulse value exceeds limit:

If the pulse value specified in Pulse instruction exceeds the limit set by the Range instruction, an error will occur.

## Examples
```spel
> pulse 16000, 10000, -100, 10
```

```spel
>pulse
PULSE:  1:  27306 pls 2:  11378 pls 3:  -3072 pls 4:   1297 pls
>
```

## See Also
Robot motion commands

!...!Parallel Processing

Go

Accel

Range

Speed

Pulse Statement Example

Following are examples on the Command window:

This example moves the robot arm to the position which is defined by each joint pulse.

> pulse 16000, 10000, -100, 10

This example displays the pulse numbers of 1st to 4th axes of the current robot arm position.

>pulse

PULSE:  1:  27306 pls 2:  11378 pls 3:  -3072 pls 4:   1297 pls

>


---

# QP Statement
**Type:** reference | **Section:** Operator

## Syntax
```
(1) QP { On | Off }

(2) QP
```

## Parameters
On | Off	Quick Pause can be either On or Off.

## Description
If during motion command execution either the Pause switch is pressed, or a pause signal is input to the controller, quick pause mode determines whether the robot will stop immediately, or will Pause after having executed the motion command.

Immediately decelerating and stopping is referred to as a "Quick Pause".

With the On parameter specified, QP turns the Quick Pause mode On.

With the Off parameter specified, QP turns the Quick Pause mode Off.

QP displays the current setting of whether the robot arm is to respond to the Pause input by stopping immediately or after the current arm operation is completed. QP is simply a status instruction used to display whether Quick Pause mode is on or off.

## Notes
Quick pause mode defaults to on after power is turned on:

The Quick Pause mode set by the QP instruction remains in effect after the Reset instruction. However, when the PC power or Drive Unit power is turned off and then back on, Quick Pause mode defaults to On.

QP and the Safe Guard Input

Even if QP mode is set to Off, if the Safe Guard Input becomes open the robot will pause immediately.

## Examples
```spel
> qp

QP ON

> qp on 'Sets QP to Quick Pause Mode

>
```

## See Also
Pause

QP Statement Example

This Command window example displays the current setting of whether the robot arm is to stop immediately on the Pause input. (i.e. is QP mode set On or Off)

> qp

QP ON

> qp on 'Sets QP to Quick Pause Mode

>


---

# Quit Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Quit { taskIdentifier | All }
```

## Parameters
taskIdentifier	Task name or integer expression representing the task number.

A task name is the function name used in an Xqt statement or a function started from the Run window or Operator window.

Task number range is:

Normal tasks :1 to 32

Background task :65 to 80

Trap tasks : 257 to 267

All	Specifies that all tasks should be terminated.

## Description
Quit stops the tasks that are currently being executed, or that have been temporarily suspended with Halt.

Quit also stops the task when the specified task is NoPause task or NoEmgAbort task (special task using NoPause or NoEmgAbort at Xqt), or the background tasks..

Quit All stops all tasks including the tasks above other than the background tasks.

Quit All sets the robot control parameter as below:

Robot Control parameter

Current robot Speed, SpeedR, SpeedS- (Initialized to default values)

Current robot QPDecelR , QPDecelS- (Initialized to default values)

Current robot LimZ parameter- (Initialized to 0)

Current robot CP parameter- (Initialized to Off)

Current robot SoftCP parameter- (Initialized to Off)

Current robot Fine- (Initialized to default values)

Currrent robot Power Low- (Low Power Mode set to On)

Current robot PTPBoost- (Initialized to default values)

Current robot TCLim, TCSpeed- (Initialized to default values)

Current robot PgLSpeed- (Initialized to default values)

## Examples
```spel
Function main Xqt winc1 'Start winc1 function Xqt winc2 'Start winc2 function Wait 10 Quit winc1 'Terminate task winc1 Quit winc2 'Terminate task winc2
Fend
```

```spel
Function winc1 Do
    On 1; Wait 0.2
    Off 1; Wait 0.2 Loop
Fend

Function winc2 Do
    On 2; Wait 0.5
    Off 2; Wait 0.5 Loop
Fend
```

## See Also
Exit Function

Halt

Resume

Xqt

Quit Statement Example

This example shows two tasks that are terminated after 10 seconds.

Function main

  Xqt winc1 'Start winc1 function

  Xqt winc2 'Start winc2 function

  Wait 10

  Quit winc1 'Terminate task winc1

  Quit winc2 'Terminate task winc2

Fend

Function winc1

  Do

    On 1; Wait 0.2

    Off 1; Wait 0.2

  Loop

Fend

Function winc2

  Do

    On 2; Wait 0.5

    Off 2; Wait 0.5

  Loop

Fend


---

# RSet$ Function
**Type:** reference | **Section:** Operator

## Syntax
```
RSet$
			(string, length)
```

## Parameters
string	String expression.

length	Integer expression for the total length of the string returned.

## Description
RSet$ Function

RSet$ Function

See_Also Example

Returns the specified string with leading spaces added up to the specified length.

## Examples
```spel
temp$ = "123"

temp$ = RSet$(temp$, 10)  ' temp$ = "       123"
```

## See Also
LSet$

Space$

RSet$ Function Example

temp$ = "123"

temp$ = RSet$(temp$, 10)  ' temp$ = "       123"


---

# RShift Function
**Type:** reference | **Section:** Operator

## Syntax
```
RShift (number, shiftBits)
```

## Parameters
number	Numeric expression to be shifted.

shiftBits	The number of bits (integer from 0 to 31) to shift number to the right.

## Description
RShift shifts the specified numeric data (number) to the right (toward a lower order digit) by the specified number of bits (shiftBits). The high order bits shifted are replaced by 0.

The simplest explanation for RShift is that it simply returns the result of number / 2shiftBits. (Number is divided by 2 shiftBit times.)

## Notes
Numeric Data Type:

The numeric data (number) may be any valid numeric data type. RShift works with data types: Byte, Double, Int32, Integer, Long, Real, Short, UByte, UInt32, and UShort.

## Examples
```spel
Function rshiftst Integer num, snum, i num = 32767 For i = 1 to 16
    Print "i =", i
    snum = RShift(num, 1)
    Print "RShift(32767, ", i, ") = ", snum Next i
Fend
```

```spel
> Print RShift(10,1)
5
> Print RShift(8,3)
1
> Print RShift(16,2)
4
```

## See Also
And

LShift

Not

Or

Xor

RShift Function Example

The example shown below shows a program which shows all the possible RShift values for an Integer data type starting with the integer set to 0.

Function rshiftst

  Integer num, snum, i

  num = 32767

  For i = 1 to 16

    Print "i =", i

    snum = RShift(num, 1)

    Print "RShift(32767, ", i, ") = ", snum

  Next i

Fend

Some other example results from the RShift instruction from the command window.

> Print RShift(10,1)

5

> Print RShift(8,3)

1

> Print RShift(16,2)

4


---

# RadToDeg Function
**Type:** reference | **Section:** Operator

## Syntax
```
RadToDeg(
			radians
			)
```

## Parameters
radians	Real expression representing the radians to convert to degrees.

## Description
RadToDeg Function

RadToDeg Function

See_Also Example

Converts radians to degrees.

## Examples
```spel
s = RadToDeg(x)
```

## See Also
Atan

Atan2

DegToRad

RadToDeg Function Example

s = RadToDeg(x)


---

# Range Statement
**Type:** reference | **Section:** Operator

## Syntax
```
(1) Range j1Min, j1Max, j2Min, j2Max, j3Min, j3Max, j4Min, j4Max, j5Min, j5Max, j6Min, j6Max, j7Min, j7Max, j8Min, j8Max, j9Min, j9Max

(2) Range
```

## Parameters
j1Min	The lower limit for joint 1 specified in pulses.

j1Max	The upper limit for joint 1 specified in pulses.

j2Min	The lower limit for joint 2 specified in pulses.

j2Max	The upper limit for joint 2 specified in pulses.

j3Min	The lower limit for joint 3 specified in pulses.

j3Max	The upper limit for joint 3 specified in pulses.

j4Min	The lower limit for joint 4 specified in pulses.

j4Max	The upper limit for joint 4 specified in pulses.

j5Min	Optional for 6-Axis robots (including N series) and Joint type 6-axis robots.

The lower limit for joint 5 specified in pulses.

j5Max	Optional for 6-Axis robots (including N series) and Joint type 6-axis robots.

The upper limit for joint 5 specified in pulses.

j6Min	Optional for 6-Axis robots (including N series) and Joint type 6-axis robots.

The lower limit for joint 6 specified in pulses.

j6Max	Optional for 6-Axis robots (including N series) and Joint type 6-axis robots.

The upper limit for joint 6 specified in pulses.

j7Min	Optional for Joint type 7-axis robots. The lower limit for joint 7 specified in pulses.

j7Max	Optional for Joint type 7-axis robots. The upper limit for joint 7 specified in pulses.

j8Min	Optional for the additional S axis. The lower limit for joint 8 specified in pulses.

j8Max	Optional for the additional S axis. The upper limit for joint 8 specified in pulses.

j9Min	Optional for the additional T axis. The lower limit for joint 9 specified in pulses.

j9Max	Optional for the additional T axis. The upper limit for joint 9 specified in pulses.

## Description
Range specifies the lower and upper limits of each motor joint in pulse counts. These joint limits are specified in pulse units. This allows the user to define a maximum and minimum joint motion range for each of the individual joints. XY coordinate limits can also be set using the XYLim instruction.

The initial Range values are different for each robot. The values specified by this instruction remain in effect even after the power is switched off.

When parameters are omitted, the current Range values are displayed.

Robot parameter data is stored in compact flash in controller.  Therefore, writing to command flash occurs when executing this command.  Frequent writing to compact flash affect to lifetime of compact flash.  We recommend to use this command minimally.

Potential Errors

Attempt to Move Out of Acceptable Range

If the robot arm attempts to move through one of the joint limits an will occur

Axis Does Not Move

If the lower limit pulse is equal to or greater than the upper limit pulse, the joint does not move.

Note:  Range of the lower/upper limits of Joint #6 in pulse differs depending on manipulator model

C4: -419430399  to 419430399

C8, C12, N2, N6: -26847955 to 26847955

## Examples
```spel
> range
-18205, 182045, -82489, 82489, -36864, 0, -46695, 46695
>
> range 0, 32000, 0, 32224, -10000, 0, -40000, 40000
>
```

## See Also
JRange

SysConfig

XYLim

Range Statement Example

This simple example from the command window displays the current range settings and then changes them.

> range

-18205, 182045, -82489, 82489, -36864, 0, -46695, 46695

>

> range 0, 32000, 0, 32224, -10000, 0, -40000, 40000

>


---

# Range page, Robot Manager
**Type:** reference | **Section:** Operator

## Description
Range page, Robot Manager

[Tools]-[Robot Manager]-[Range] Page

This page allows you to configure the robot joint software limits.

For more details on Range settings, refer to the following manual:

SPEL+ Language Reference - Range Statement

NOTE:  When using Safety Function (the Controller with Safety Board), the Safety Limited Position (SLP) of the Safety Function can be used.

Set them using the Safety Function Manager. For more details, refer to the following manual:

Robot Controller Safety Function Manual 4.3.4 Setting Safety Limited Position (SLP)

Item	Description

J1 -
		 J6	Type
		 in the minimum and maximum encoder pulse values for each joint.

Read
		 Current	Click
		 this button to read the current joint value of the robot into
		 the current field.

		The button text will change depending on which text field has focus.

Apply	Sets
		 the current values.

Restore	Reverts
		 to the previous values.

Defaults	Reverts
		 back to the default settings.


---

# Read Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Read #portNumber, stringVar$, count
```

## Parameters
portNumber	ID number representing a file or communications port to read from.

File number can be specified in ROpen, WOpen, and AOpen statements.

Communication port number can be specified in OpenCom (RS-232C) or OpenNet (TCP/IP) statements.

stringVar$	Name of a string variable that will receive the character string.

count	Maximum number of bytes to read.

## Description
Read Statement

Read Statement

See_Also Example

Reads characters from a file or communications port.

## Examples
```spel
Integer numOfChars
String data$

numOfChars = ChkCom(1)

If numOfChars > 0 Then Read #1, data$, numOfChars
EndIf
```

## See Also
ChkCom, ChkNet, OpenCom, OpenNet, Write, WriteBin

Read Example

Integer numOfChars

String data$

numOfChars = ChkCom(1)

If numOfChars > 0 Then

  Read #1, data$, numOfChars

EndIf


---

# ReadBin Statement
**Type:** reference | **Section:** Operator

## Syntax
```
ReadBin #portNumber, var

ReadBin #portNumber, array(), count
```

## Parameters
portNumber	ID number representing a file or communications port to read from.

File number can be specified in BOpen statement.

Communication port number can be specified in OpenCom (RS-232C) or OpenNet (TCP/IP) statements.

var	Name of a byte, integer, or long variable that will receive the data byte.

array()	Name of a byte, integer, or long array variable that will receive the data byte.  Specify a one dimension array variable.

count	Specify the number of bytes to read.

The specified count has to be less than or equal to the number of array elements and also smaller than 256 bytes.

If the communication port (TCP/IP) is the subject, the count has to be less than or equal to the number of array and also smaller than 1024 bytes.

## Description
ReadBin Statement

ReadBin Statement

Reads binary data from a file or communications port.

## Examples
```spel
Integer data
Integer dataArray(10)

numOfChars = ChkCom(1)
If numOfChars > 0 Then ReadBin #1, data
EndIf

NumOfChars = ChkCom(1)
If numOfChars > 10 Then ReadBin #1, dataArray(), 10
EndIf
```

## See Also
Write, WriteBin, Read

ReadBin Statement Example

Integer data

Integer dataArray(10)

numOfChars = ChkCom(1)

If numOfChars > 0 Then

  ReadBin #1, data

EndIf

NumOfChars = ChkCom(1)

If numOfChars > 10 Then

  ReadBin #1, dataArray(), 10

EndIf


---

# Real Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Real varName [( subscripts )] [, varName [( subscripts )]...
```

## Parameters
varName	Variable name which the user wants to declare as type Real.

subscripts	Optional.  Dimensions of an array variable; up to 3 dimensions may be declared.  The subscripts syntax is as follows

(ubound1, [ubound2], [ubound3])

ubound1, ubound2, ubound3 each specify the maximum upper bound for the associated dimension.

The elements in each dimension of an array are numbered from 0 and the available number of array elements is the upper bound value + 1.

When specifying the upper bound value, make sure the number of total elements is within the range shown below:

Local variable   2000

Global Preserve variable   4000

Global variable and module variable   100000

## Description
Real is used to declare variables as type Real.  Local variables should be declared at the top of a function.  Global and module variables must be declared outside functions.  Number of valid digits are six digits for Real type.

## Examples
```spel
Function realtest Real var1 Real A(10) 'Single dimension array of real Real B(10, 10) 'Two dimension array of real Real C(5, 5, 5) 'Three dimension array of real Real arrayVar(10) Integer i Print "Please enter a Real Number:" Input var1 Print "The Real variable var1 = ", var1 For i = 1 To 5
    Print "Please enter a Real Number:"
    Input arrayVar(i)
    Print "Value Entered was ", arrayVar(i) Next i
Fend
```

## See Also
Data Types Overview

Variable Declarations

Variable Naming Conventions

Boolean

Byte

Double

Global

Int32

Integer

Long

Short

String

UByte

UInt32

UShort

Real Statement Example

The following example shows a simple program which declares some variables using Real.

Function realtest

  Real var1

  Real A(10) 'Single dimension array of real

  Real B(10, 10) 'Two dimension array of real

  Real C(5, 5, 5) 'Three dimension array of real

  Real arrayVar(10)

  Integer i

  Print "Please enter a Real Number:"

  Input var1

  Print "The Real variable var1 = ", var1

  For i = 1 To 5

    Print "Please enter a Real Number:"

    Input arrayVar(i)

    Print "Value Entered was ", arrayVar(i)

  Next i

Fend


---

# RealTorque Function
**Type:** reference | **Section:** Operator

## Syntax
```
RealTorque (jointNumber)
```

## Parameters
jointNumber	Specifies the joint number to acquire the torque instruction value using an expression or numeric value.

The additional S axis is 8 and T axis is 9.

## Description
RealTorque Function

RealTorque Function

Returns the current torque instruction value of the specified joint.

## Examples
```spel
Print "Current Z axis torqueinstruction value (SCARA):", RealTorque(3)
```

## See Also
TC, TCSpeed, TCLim

RealTorque Function Example

Print "Current Z axis torqueinstruction value (SCARA):", RealTorque(3)


---

# Redim Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Redim [Preserve] arrayName
			(
			subscripts
			)
```

## Parameters
Preserve	Optional.  Specifies to preserve the previous contents of the array.  If omitted, the array will be cleared.

arrayName	Name of the array variable; follows standard variable naming conventions.  The array must have already been declared.

subscripts	New dimensions of the array variable.  You must supply the same number of dimensions as when the variable was declared.
  The syntax is as follows

(
						dim1 [, dim2 [, dim3]])

dim1, dim2, dim3 can be an integer expression from 0 - 2147483646.

Others than String	String

Local variable	2000	200

Global Preserve variable	4000	400

Global variable and module variable	100000	10000

10000

## Description
Use Redim to change an array's dimensions at run time.  Use Preserve to retain previous values.  The array variable declared by Byref cannot use Redim.

Frequent Redim will decrease the speed of program execution.  Especially, we recommend using the minimum of Redim for the global preserve variables.

## Examples
```spel
Integer i, numParts, a(0)

Print "Enter number of parts:"
		Input numParts

Redim a(numParts)

For i= 0 to UBound(a)
		  a(i) = i
		Next

' Redimension the array with 20 more elements

			Redim Preserve a(numParts + 20)

' The first element values are retained
		For i = 0 to UBound(a)
		  Print a(i)
		Next
```

## See Also
UBound

Redim Statement Example

Integer i, numParts, a(0)

Print "Enter number of parts:"

		Input numParts

Redim a(numParts)

For i= 0 to UBound(a)

		  a(i) = i

		Next

' Redimension the array with 20 more elements

Redim Preserve a(numParts + 20)

' The first element values are retained

		For i = 0 to UBound(a)

		  Print a(i)

		Next


---

# Reset Statement
**Type:** reference | **Section:** Operator

## Syntax
```
(1) Reset

(2) Reset Error
```

## Description
Reset resets the items shown below.

Reset Error finishes all non-background tasks and resets the error status and robot control parameters.

To execute the Reset Error statement from programs you need to set the [Enable advanced task commands] preference in the [Setup]-[System Configuration]-[Controller]-[Preference] page of the Epson RC+.

Emergency Stop Status (reset by Reset only)

Error status

Output Bits (reset by Reset only)

All Output Bits output set to Off except the I/O for Remote and the I/O for hand..

User can set Option Switch to turn this feature off.

Robot Control parameter

SpeedR, SpeedS- (Initialized to default values)

QPDecelR , QPDecelS- (Initialized to default values)

LimZ parameter- (Initialized to 0)

CP parameter - (Initialized to Off)

SoftCP parameter - (Initialized to Off)

Fine - (Initialized to default values)

Power Low - (Low Power Mode set to On)

PTPBoost- (Initialized to default values)

TCLim, TCSpeed - (Initialized to default values)

PgLSpeed - (Initialized to default values)

For servo related errors, Emergency Stop status, and any other conditions requiring a Reset, no command other than Reset will be accepted. In this case first execute Reset, then execute other processing as necessary.

For example, after an emergency stop, first verify safe operating conditions, execute Reset, and then execute Motor On.

Critical error state will not be canceled by Reset.

When a critical error occurs, turn Off the controller and solve the cause of the error.

The Reset Statement cannot be executed from a background task or tasks started with the Trap Emergency or Trap Error. Emergency Stop status cannot be reset from programs.

## Notes
Reset Outputs Preference

(Setup | System Configuration | Preferences page) If the "Reset turns off outputs" controller preference is on, then when the Reset instruction is issued, all outputs except bit for hand will be turned off. This is important to remember when wiring the system such that turning the outputs off should not cause tooling to drop or similar situations.

For details of hand, refer to Hand Function Manual.

## Examples
```spel
>reset
```

```spel
>
```

## See Also
Accel

AccelS

LimZ

Motor On

Off

On

PTPBoost

SFree

SLock

Speed

SpeedS

Reset Statement


---

# Resume Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Resume { taskIdentifier | All }
```

## Parameters
taskIdentifier	Task name or integer expression representing the task number.

Task name is a function name used in an Xqt statement or a function started from the Run window or Operator window.

Task number range is:

Normal tasks :	1 ~ 32

Background task :	65 ~ 80

Trap tasks : 	257 ~ 267

All	Specifies that all tasks should be resumed.

## Description
Resume continues the execution of the task suspended by the Halt instruction.

## Examples
```spel
Function main
		  Xqt 2, flicker 'Execute flicker as task 2

Do
		    Wait 3 'Allow flicker to execute for 3 seconds
		    Halt flicker 'Halt the flicker task
		    Wait 3

			    Resume flicker 'Resume the flicker task
		  Loop
		Fend

Function flicker
		  Do
		    On 1
		    Wait 0.2
		    Off 1
		    Wait 0.2
		  Loop
		Fend
```

## See Also
Halt

Quit

Xqt

Resume Statement Example

This shows the use of Resume instruction after the Halt instruction.

Function main

		  Xqt 2, flicker 'Execute flicker as task 2

Do

		    Wait 3 'Allow flicker to execute for 3 seconds

		    Halt flicker 'Halt the flicker task

		    Wait 3

Resume flicker 'Resume the flicker task

		  Loop

		Fend

Function flicker

		  Do

		    On 1

		    Wait 0.2

		    Off 1

		    Wait 0.2

		  Loop

		Fend


---

# Return Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Return
```

## Description
The Return statement is used with the GoSub statement.  The primary purpose of the Return statement is to return program control back to the instruction following the GoSub instruction which initiated the subroutine in the first place.

The
			GoSub
			instruction causes program control to branch to the user specified statement line number or label.  The program then executes the statement on that line and continues execution through subsequent line numbers until a Return instruction is encountered.  The Return instruction then causes program control to transfer back to the line which immediately follows the line which initiated the GoSub in the first place. (i.e. the GoSub instruction causes the execution of a subroutine and then execution Returns to the statement following the GoSub instruction.)

Potential Errors

Return Found Without GoSub

A Return instruction is used to "return" from a subroutine back to the original program which issued the GoSub instruction.  If a Return instruction is encountered without a GoSub having first been issued then an error will occur.  A stand alone Return instruction has no meaning because the system doesn't know where to Return to.

## Examples
```spel
Function main
		  GoSub checkio
		  On 1
		  On 2
		  Exit Function

checkio: 'Subroutine starts here
		  If InW(0) <> 0 Then
		    Print "Message to Operator here"
		  EndIf
		finished:

			  Return 'Subroutine ends here and returns
		Fend
```

## See Also
OnErr

GoSub

GoTo

Return Statement Example

The following example shows a simple function which uses a GoSub instruction to branch to a label called checkio and check the first 16 user inputs. Then the subroutine returns back to the line after the Gosub in the main program.

Function main

		  GoSub checkio

		  On 1

		  On 2

		  Exit Function

checkio: 'Subroutine starts here

		  If InW(0) <> 0 Then

		    Print "Message to Operator here"

		  EndIf

		finished:

Return 'Subroutine ends here and returns

		Fend


---

# Right$ Function
**Type:** reference | **Section:** Operator

## Syntax
```
Right$
			(string, count)
```

## Parameters
string	String variable or character string of up to 255 characters from which the rightmost characters are copied.

count	The number of characters to copy from string
 starting with the rightmost character.

## Description
Right$ returns the rightmost count characters of a string specified by the user.  Right$ can return up to as many characters as are in the character string.

## Examples
```spel
Function SplitPartData(DataIn$ As String, ByRef PartNum$ As String, ByRef PartName$ As String, ByRef PartCount As Integer)

Integer pos
		  PartNum$ = Left$(DataIn$, 10)

pos = Instr(DataIn$, ",")
		  DataIn$ = Right$(datain$, Len(DataIn$) - pos)

PartName$ = Mid$(DataIn$, 11, 10)

PartCount = Val(Right$(dataIn$, 5))

Fend
```

```spel
> Print Right$("ABCDEFG", 2)

			FG

> Print Right$("ABC", 3)

			ABC
```

## See Also
Asc, Chr$, InStr, Left$, Len, Mid$, Space$, Str$, Val

Right$ Function Example

The example shown below shows a program which takes a part data string as its input and splits out the part number, part name, and part count.

Function SplitPartData(DataIn$ As String, ByRef PartNum$ As String, ByRef PartName$ As String, ByRef PartCount As Integer)

Integer pos

		  PartNum$ = Left$(DataIn$, 10)

pos = Instr(DataIn$, ",")

		  DataIn$ = Right$(datain$, Len(DataIn$) - pos)

PartName$ = Mid$(DataIn$, 11, 10)

PartCount = Val(Right$(dataIn$, 5))

Fend

Some other example results from the Right$ instruction from the Command window.

> Print Right$("ABCDEFG", 2)

FG

> Print Right$("ABC", 3)

ABC


---

# Robot Manager
**Type:** reference | **Section:** Operator

## Description
Robot Manager

Robot Manager

The Robot Manager is a dialog box that can have any number of the following pages, depending on how it was setup.


---

# Robot motion commands
**Type:** reference | **Section:** Operator

## Description
Robot motion commands

Robot motion commands

SPEL+ includes several commands for controlling the robot from your programs.

Homing the robot

Point to point motion

Linear Motion

Joint motion

Controlling position accuracy

Curves

CP Motion Speed / Acceleration and Tool Orienation

PTP Speed Acceleration for Small Distances

Pressing Motion

Collision Detection Function

Torque Restriction Function

Weight, Inertia, and Eccentricity / Offset Measurement Utility


---

# SFree Function
**Type:** function | **Section:** Operator

## Syntax
```
SFree(jointNumber)
```

## Parameters
jointNumber	Integer expression representing the joint number to check.

The additional S axis is 8 and T axis is 9.

## Description
SFree Function

SFree Function

See_Also Example

Returns free joint status for a specified joint.

## Examples
```spel
If SFree(1) Then Print "Joint 1 is free"
EndIf
```

## See Also
SFree Statement

SFree Function Example

If SFree(1) Then

  Print "Joint 1 is free"

EndIf


---

# SFree Keyword
**Type:** reference | **Section:** Operator

## Description
SFree Keyword

SFree Keyword

The SFree keyword is used in these contexts:

SFree Statement

SFree Function


---

# SFree Statement
**Type:** statement | **Section:** Operator

## Syntax
```
SFree jointNumber [ , jointNumber,... ]
```

## Parameters
jointNumber	An integer expression representing a servo joint number (1 ~ 9).

The additional S axis is 8 and T axis is 9.

## Description
SFree removes servo power from the specified servo joints.  This instruction is used for the direct teaching or the part installation by state free joint the specified joint.  To release the free joint state, execute the SLock instruction, Motor On, or Motor Off

SFree initializes the robot control parameter.

See Motor On for the details.

## Notes
SFree Sets Some System Items back to Their Initial State:

SFree, for safety purposes, initializes parameters concerning the robot arm speed or acceleration (Speed, SpeedS, Accel,  AccelS) and the LimZ parameter.  For details, refer to the Motor On.

Firmware version earlier than 7.5.1.0, SFree is available with only Motor ON state.

SFree changes the motion as following below depends to the firmware version.

Firmware	SFree Available / Not available

Before 7.5.1.0	Only when motor is on

After 7.5.1.0	When motor is on, or motor is off

SFree and Its Use with the Z Joint and U Joint for SCARA robots (including RS series)

The Z joint has electronic brakes so setting SFree for the Z joint does not immediately allow the Z joint to be moved.  To move the Z joint by hand requires the brake to be released continuously by pressing the brake release switch on the top of the robot arm.

Some models have electronic brake on the U joint. When the robot has the U joint electronic brake, setting SFree for the U joint does not immediately allow the U joint to be moved. To move the U joint by hand requires the brake to be released continuously by pressing the brake release switch on the top of the robot arm.

SFree and Its Use with 6-Axis robots (including N series)

All joints of the 6-axis robots (including N series) have an electromagnetic brake.  The brake can be released using the Brake command with the motor off.  In the motor off state, SFree is not valid.  If you execute SFree with the motor on, an electromagnetic brake will be on.  You cannot move any joint by hand using SFree.

Executing motion commands while joints are in free joint state

Attempting to execute a motion command while in the free joint condition will cause an error in the controller's default state. However, to allow motion while 1 or more of the axes are in the free joint state, turn on the "Allow Motion with one or more axes free" controller preference.  (This preference can be set in the Setup | System Configuration | Controller | Preferences page.)

Do not use SFree during Conveyor Tracking

Error 5057 or 5058 might occur if SFree is used during conveyor tracking. Use SFree after terminating conveyor tracking such as Cnv_AbortTrack.

## Examples
```spel
Function GoPick Speed pickSpeed SFree 1, 2    'State J1 and J2 to free joint
                'and control the Z and U joints for part installation. Go pick SLock 1, 2    'Release the free joint state of J1 and J2.
```

```spel
Fend
```

## See Also
Brake

LimZ

Motor

SFree Function

SLock

SFree Statement Example

This is a simple example on the usage of the SFree instruction.  The Motion with SFree controller preference must be enabled for this example to work.

Function GoPick

  Speed pickSpeed

  SFree 1, 2    'State J1 and J2 to free joint

                'and control the Z and U joints for part installation.

  Go pick

  SLock 1, 2    'Release the free joint state of J1 and J2.

Fend


---

# SLock Statement
**Type:** reference | **Section:** Operator

## Syntax
```
SLock jointNumber [ , jointNumber,... ]
```

## Parameters
jointNumber	The servo joint number (1 ~ 9).

The additional S axis is 8 and T axis is 9.

## Description
SLock release the free joint state which was free joint state by the SFree instruction for the direct teaching or part installation.

If the joint number is omitted, all joints are released free joint.

Executing SLock the 3rd joint (Z) causes the brake to release.

Executing SLock while in Motor Off state will cause an error.

SLock initializes the robot control parameter.

See Motor On for the details.

6-axis robots (including N series) cannot be free joint state by the SFree instruction.  When SLock is executed, an error occurs.

## Notes
SLock Sets Some System Items back to Their Initial State:

SLock, for safety purposes, initializes parameters concerning the robot arm speed (Speed and SpeedS), acceleration (Accel and AccelS) and the LimZ parameter.

## Examples
```spel
Function test .

SFree 1, 2   'State J1 and J2 to free joint
               'and control the Z and U joints for part installation. Go P1 SLock 1, 2   'Release the free joint state of J1 and J2. . .
Fend
```

## See Also
Brake

LimZ

Reset

SFree

SLock Statement Example

This is a simple example on the usage of the SLock instruction.  The Motion with SFree controller preference must be enabled for this example to work.

Function test

  .

SFree 1, 2   'State J1 and J2 to free joint

               'and control the Z and U joints for part installation.

  Go P1

  SLock 1, 2   'Release the free joint state of J1 and J2.

  .

  .

Fend


---

# ST Function
**Type:** reference | **Section:** Operator

## Syntax
```
ST (sValue As Real, tValue As Real )
```

## Parameters
sValue	Real value
		 that specifies the S axis coordinate value

tValue	Real value
		 that specifies the T axis coordinate value

## Description
This function is used when you are using the additional ST axes.

When using this function like Go ST(10,20), the additional axis will move to the specified coordinate but the manipulator will not move.  If you want to move the manipulator as well, use like Go XY(60,30,-50,45) : ST( 10,20).

For the details of the additional axis, refer to Epson RC+ Users Guide: 21. Additional Axis.

## Examples
```spel
P10 = ST(10, 20)
```

## See Also
XY Function

ST Function Example

P10 = ST(10, 20)


---

# SafetyOn Function
**Type:** reference | **Section:** Operator

## Syntax
```
SafetyOn
```

## Description
SafetyOn function is used only for NoPause task or NoEmgAbort task (special task using NoPause or NoEmgAbort at Xqt), and background tasks.

## Notes
Forced Flag

This program example uses Forced flag for On/Off command.

Be sure that the I/O outputs change during error, or at Emergency Stop or Safety Door Open when designing the system.

Function main

  Xqt SafetyOnOffMonitor, NoPause

   ...

   ...

Fend

Function SafetyOnOffMonitor

  Do

    Wait SafetyOn = On

     Print "Saftey Open"

    Off 10, Forced

    On 12, Forced

    Wait SafetyOn = Off

    Print "Saftey Close"

    On 10, Forced

    Off 12, Forced

  Loop

Fend

## See Also
Return the Safety Door open status.

ErrorOn

EStopOn

PauseOn

Wait

Xqt

SafetyOn Function Example

The following example shows a program that monitors the Safety Door open and switches the I/O On/Off when Safety Door open occurs.


---

# Saving your work
**Type:** reference | **Section:** Operator

## Description
Saving your work

Saving your work

You can save your work in the following three ways.

-  In the [Teach...] tab, click the [Save] button.

-  In the Epson RC+ 8.0, click [File]-[Save], or click the [Save]  on the toolbar.

-  In the Epson RC+ 8.0 menu, execute [Project]-[Save], or click the [Save all files]  button on the toolbar.

When you want to restore the data without saving the point files, select [Restore] from the [File] menu.

When you close the [Robot Manager], you will be prompted if you want to save your changes. Click the [Yes] button to save changes. Click the [No] button to discard changes without saving.


---

# Select...Send
**Type:** reference | **Section:** Operator

## Syntax
```
Select selectExpr

  Case caseExpr
 statements

  [ Case caseExpr
 statements ]
 [ Default
 statements ]

Send
```

## Parameters
selectExpr	Any numeric or string expression.

caseExpr	Any numeric or string expression that evaluates to the same type as selectExpr.

statements	One or more valid SPEL+ statements or multi-statements.

## Description
If any one caseExpr is equivalent to selectExpr, then the statements after the Case statement are executed.  After execution, program control transfers to the statement following the Send statement.

If no caseExpr is equivalent to selectExpr, the Default statements are executed and program control transfers to the statement following the Send statement.

If no caseExpr is equivalent to selectExpr and Default is omitted, nothing is executed and program control transfers to the statement immediately following the Send statement.

selectExpr and caseExpr may include constants, variables, and logical operators that use And, Or and Xor.  caseExpr also may include constants, variables, and logical operators that use And, Or and Xor. In this case, the calculation result of caseExpr is compared to that of selectExpr and do not specify the variable in caseExpr because the motion becomes complicated.

## Examples
```spel
Function Main Integer i For i = 0 To 10
    Select I
      Case 0
        Off 1;On 2;Jump P1
      Case 3
        On 1;Off 2
        Jump P2;Move P3;On 3
      Case 7
       On 4
      Default
        On 7
    Send Next
Fend
```

## See Also
If...Then...Else

Select Example

Shown below is a simple example for Select...Send:

Function Main

  Integer i

  For i = 0 To 10

    Select I

      Case 0

        Off 1;On 2;Jump P1

      Case 3

        On 1;Off 2

        Jump P2;Move P3;On 3

      Case 7

       On 4

      Default

        On 7

    Send

  Next

Fend


---

# Sense Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Sense [ condition ]
```

## Parameters
condition	Input status
		 specified as a trigger

[Event]
		 comparative operator ( =, <>, >=, >, <, <=)
		 [Integer expression]

The following
		 functions and variables can be used in the Event:

Functions
		 :Sw, In, InW, Oport, Out, OutW, MemSw, MemIn, MemInW, Ctr, GetRobotInsideBox,
		 GetRobotInsidePlane, AIO_In, AIO_InW, AIO_Out, AIO_OutW, Hand_On,
		 Hand_Off

Variables
		 :Byte, Int32, Integer, Long, Short, UByte, UInt32, UShort global
		 preserve variable, Global variable, module variable

In addition,
		 using the following operators you can specify multiple event conditions.

Operator
		 : And, Or, Xor

## Description
Sense is used to stop approach motion during a Jump, Jump3, and Jump3CP instructions.
  The Sense condition must include at least one of the functions above.

When variables are included in the Sense condition, their values are computed when setting the Sense condition. No use of variable is recommended. Otherwise, the condition may be an unintended condition. .Multiple Sense statements are permitted. The most recent Sense condition remains current until superseded with another Sense statement.

Jump, Jump3, Jump3CP with Sense Modifier

Checks if the current Sense condition is satisfied.
  If satisfied, the Jump instruction completes with the robot stopped above the target position. (i.e. When the Sense Condition is True, the robot arm remains just above the target position without executing approach motion.  When the Sense condition is False, the robot arm completes the full Jump instruction motion through to the target position.

When parameters are omitted, the current Sense definition is displayed.

## Notes
Sense Setting at Main Power On

At power on, the initialSense condition is:

Sense Sw(0) = On
         ''Robot does not execute downward motion when Input bit 0 is on

Use of JS and Stat to Verify Sense

Use JS or Stat to verify if the Sense condition has been satisfied after execting a motion command using Sense modificators..

To use a variables in the event condition expression

Available variables are Integer type (Byte, Integer, Long)

Array variables are not available

Local variables are not available

If a variable value cannot satisfy the event condition for more than 0.01 seconds, the system cannot retrieve the change in variables.

Up to 64 can wait for variables in one system (including the ones used in the event condition expressions such as Wait). If it is over 64, an error occurs during the project build.

If you try to transfer a variable waiting for variables as a reference with Byref, an error occurs.

When a variable is included in the right side member of the event condition expression, the value is calculated when the motion command start. We recommend not using variables in an integer expression to avoid making unintended conditions.

See Also

In, JS, Jump, Jump3, Jump3CP, MemIn, MemSW, Stat, Sw

Sense Statement Example

This is a simple example on the usage of the Sense instruction.

Function test

  .

  .

TrySense:

  Sense Sw(1) = Off 'Specifies the arm stops

                    'above the target when

                    'the input bit 1 is 0.

  Jump P1 C2 Sense

If JS = True Then

    GoSub ERRPRC   'If the arm remains stationary

    GoTo TrySense  'above the point specified,

                   'then execute ERRPRC and go to TrySense.

  EndIf

  On 1; Wait 0.2; Off 1

  .

  .

Fend

[Other Syntax

## Examples
```spel
Sense Sw(5) = On
```

```spel
Sense Sw(5) = On And Sw(6) = Off
```

```spel
Function test . .
TrySense: Sense Sw(1) = Off 'Specifies the arm stops
                    'above the target when
                    'the input bit 1 is 0. Jump P1 C2 Sense If JS = True Then
    GoSub ERRPRC   'If the arm remains stationary
    GoTo TrySense  'above the point specified,
                   'then execute ERRPRC and go to TrySense. EndIf On 1; Wait 0.2; Off 1 . .
Fend
```

```spel
> Sense Sw(1)=1 And MemSw(1)=1

> Sense Sw(0) Or (Sw(1) And MemSw(1))
```


---

# SetCom Statement
**Type:** reference | **Section:** Operator

## Syntax
```
SetCom #portNumber, [baud [, dataBits [, stopBits [, parity [, terminator [, HWFlow [, SWFlow [, timeOut ]]]]]]]]

When all parameters are omitted, displays a communication port setting.

If the several ports are used in the communication at one time with more than 19200 baud rate, error 2929 or 2922 may occur. In this case, select the lower baud rate or avoid using several ports at one time.

When using the Windows Part port, some data may drop in the baud rate of 19200 or more.

If any data drops, select the lower baud rate or use the Real Part port.

Parameter is stored to the Compact Flash inside the Controller. When you execute SetCom, the data is written to the Conpact Flash. If a data is written to the Compact Flash fequentlly, it may shorten the Compact Flash life. Using SetCom only when changing the parameter is recommended.
```

## Parameters
portNumber	Integer value representing a RS-232C port number

Real Part1 ~ 8

Windows Part1001 to 1008

110	2400	19200

300	4800	38400

600	9600	56000

1200	14400	115200

(Default: 9600)

When using the Windows Part port , some data may drop in the baud rate of 19200 or more.

(Default: 9600)

dataBits	Optional. Specifies the number of data bits per character. Valid values are 7 and 8.

stopBits	Optional. Specifies the number of stop bits per character. Valid values are 1 and 2.

parity	Optional. Specifies the parity. Valid values are O (Odd), E (Even), and N (None).

terminator	Optional. Specifies the line termination characters. Valid values are CR, LF, CRLF.

HWFlow	Optional. Specifies hardware control. Valid values are RTS and NONE.

SWFlow	Optional. Specifies software control. Valid values are XON and NONE.

timeOut	Optional. Specifies the maximum time for transmit or receive in seconds. If this value is 0, then there is no time out.

## Description
SetCom Statement

SetCom Statement

See_Also Example

Sets or displays parameters for a communications port.

## Examples
```spel
SetCom #1, 9600, 8, 1, N, CRLF, NONE, NONE, 0

SetCom #2, 4800
```

## See Also
OpenCom

CloseCom

SetNet

SetCom Statement Example

SetCom #1, 9600, 8, 1, N, CRLF, NONE, NONE, 0

SetCom #2, 4800


---

# SetNet Statement
**Type:** reference | **Section:** Operator

## Syntax
```
(1) SetNet #portNumber, hostAddress [, TCP_IP_PortNum [, terminator [, SWFlow [, timeOut, [, protocol [, CloseNet timeout]]]]]]

(2) SetNet
```

## Parameters
portNumber	Specifies which TCP/IP port to set parameters for. Valid values are 201 - 216.

hostAddress	Specifies the host IP address.

TCP_IP_PortNum	Specifies the TCP/IP port number for this node.

terminator	Specifes the line termination characters. Valid values are CR, LF, CRLF.

SWFlow	Specifies software control. Valid value is NONE.

timeOut	Specifes the maximun time for transmit or receive in seconds. If this value is 0, then there is no time out.

protocol	Specifies the protocol (TCP/UDP/UDP_SEND/UDP_RECV) of communication.

TCP: TCP communication

UDP: UDP communication

UDP_SEND: UDP send

UDP_RECV: UDP receive

CloseNet timeOut	Specifies the time before closing the socket with CloseNet in seconds. (Integer from 0 to 5)

When 0 is set, closes the socket without waiting for a response to the shutdown request.

## Description
Parameters are stored to the Compact Flash inside the Controller.  When you execute SetNet, the data is written to the Compact Flash.  If a data is written to the Compact Flash frequently, it may shorten the Compact Flash life.  Using SetNet only when changing the parameter is recommended.

## Examples
```spel
SetNet #201, "192.168.0.1", 2001, CRLF, NONE, 0, TCP, 5
```

## See Also
OpenNet

WaitNet

CloseNet

SetCom

SetNet Statement Example

SetNet #201, "192.168.0.1", 2001, CRLF, NONE, 0, TCP, 5


---

# Sgn Function
**Type:** reference | **Section:** Operator

## Syntax
```
Sgn(Operand )
```

## Parameters
Operand	A numeric expression.

## Description
The Sgn function determines the sign of the numeric value of the operand.

## Examples
```spel
>print sgn(123)

1

>print sgn(-123)

-1

>
```

## See Also
Abs	Not

And	Sin

Atan	Sqr

Atan2	Str$

Cos	Tan

Int	Val

Mod	Xor

Or

Sgn Function Example

This is a simple command window example on the usage of the Sgn function.

>print sgn(123)

1

>print sgn(-123)

-1

>


---

# Short Statement
**Type:** statement | **Section:** Operator

## Syntax
```
Short varName [( subscripts )] [, varName [( subscripts )]
```

## Parameters
varName	Variable name which the user wants to declare.

subscripts	Optional.  Dimensions of an array variable; up to 3 dimensions may be declared.  The subscripts syntax is as follows

(ubound1, [ubound2], [ubound3])

ubound1, ubound2, ubound3 each specify the maximum upper bound for the associated dimension.

The elements in each dimension of an array are numbered from 0 and the available number of array elements is the upper bound value + 1.

When specifying the upper bound value, make sure the number of total elements is within the range shown below:

Local variable   2000

Global Preserve variable   4000

Global variable and module variable   100000

## Description
Short is used to declare variables as type integer.  Integer variables can contain values from -32768 to 32767.  Local variables should be declared at the top of a function.  Global and module variables must be declared outside of functions.

## Examples
```spel
Function shorttest Short A(10) 'Single dimension array of Short Short B(10, 10) 'Two dimension array of Short Short C(5, 5, 5) 'Three dimension array of Short Short var1, arrayvar(10) Integer i Print "Please enter an integer Number" Input var1 Print "The Integer variable var1 = ", var1 For i=1 To 5
    Print "Please enter an Integer Number"
    Input arrayvar(i)
    Print "Value Entered was ", arrayvar(i) Next i
Fend
```

## See Also
Data Types Overview

Variable Naming Conventions

Variable Declarations

Boolean

Byte

Double

Global

Int32

Integer

Long

Real

String

UByte

UInt32

UShort

Short Statement Example

The following example shows a simple program that declares some variables using Short.

Function shorttest

  Short A(10) 'Single dimension array of Short

  Short B(10, 10) 'Two dimension array of Short

  Short C(5, 5, 5) 'Three dimension array of Short

  Short var1, arrayvar(10)

  Integer i

  Print "Please enter an integer Number"

  Input var1

  Print "The Integer variable var1 = ", var1

  For i=1 To 5

    Print "Please enter an Integer Number"

    Input arrayvar(i)

    Print "Value Entered was ", arrayvar(i)

  Next i

Fend


---

# Signal Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Signal
			signalNumber
```

## Parameters
signalNumber	Signal number to transmit. Range is 0 to 63.

## Description
Signal can be used to synchronize multi-task execution.

Previous signals issued before WaitSig is executed are ignored.

## Examples
```spel
Function Main
		  Xqt SubTask1
		  Xqt SubTask2
		  Wait 2

			  Signal 1

Fend
```

```spel
Function SubTask1
		  WaitSig 1
		  Print "Received Signal in SubTask1"
		Fend
```

```spel
Function SubTask2
		  WaitSig 1
		  Print "Received Signal in SubTask2"
		Fend
```

## See Also
WaitSig

Signal Statement Example

Function Main

		  Xqt SubTask1

		  Xqt SubTask2

		  Wait 2

Signal 1

Fend

Function SubTask1

		  WaitSig 1

		  Print "Received Signal in SubTask1"

		Fend

Function SubTask2

		  WaitSig 1

		  Print "Received Signal in SubTask2"

		Fend


---

# Sin Function
**Type:** reference | **Section:** Operator

## Syntax
```
Sin(
			radians
			)
```

## Parameters
radians	Real expression in Radians.

## Description
Sin returns the sine of the numeric expression.  The numeric expression (radians) must be in radian units.  The value returned by the Sin function will range from -1 to 1

To convert from radians to degrees, use the RadToDeg function.

## Examples
```spel
Function sintest
		  Real x
		  Print "Please enter a value in radians:"
		  Input x
		  Print "Sin of ", x, " is ", Sin(x)
		Fend
```

## See Also
Abs	Not

Atan	Sgn

Atan2	Sqr

Cos	Str$

Int	Tan

Mod	Val

Sin Function Example

The following example shows a simple program which uses Sin.

Function sintest

		  Real x

		  Print "Please enter a value in radians:"

		  Input x

		  Print "Sin of ", x, " is ", Sin(x)

		Fend


---

# Space$ Function
**Type:** reference | **Section:** Operator

## Syntax
```
Space$(count)
```

## Parameters
count	The number of spaces to put in the return string.

## Description
Space$ returns a string of count space characters as specified by the user. Space$ can return up to 255 characters (the maximum number of characters allowed in a string variable).

The Space$ instruction is normally used to insert spaces before, after, or between other strings of characters.

## Examples
```spel
> Print "XYZ" + Space$(1) + "ABC"

XYZ ABC
```

```spel
> Print Space$(3) + "ABC"

ABC

>
```

## See Also
Asc, Chr$, InStr, Left$, Len, LSet$, Mid$, Right$, RSet$, Str$, Val

Space$ Function Example

> Print "XYZ" + Space$(1) + "ABC"

XYZ ABC

> Print Space$(3) + "ABC"

ABC

>


---

# Speed Function
**Type:** function | **Section:** Operator

## Syntax
```
Speed(paramNumber)
```

## Parameters
paramNumber	Integer expression which evaluates to one of the values shown below.

1: PTP motion speed

2: JUMP depart speed

3: JUMP approach speed

## Description
Speed Function

Speed Function

See_Also Example

Returns one of the three speed settings.

## Examples
```spel
Function SpeedEx
		  Integer savSpeed

savSpeed = Speed(1)
		  Speed 50
		  Go pick
		  Speed savSpeed
		Fend
```

## See Also
Speed Statement

Speed Function Example

Function SpeedEx

		  Integer savSpeed

savSpeed = Speed(1)

		  Speed 50

		  Go pick

		  Speed savSpeed

		Fend


---

# Speed Keyword
**Type:** reference | **Section:** Operator

## Description
Speed Keyword

Speed Keyword

The Speed keyword is used in these contexts:

Speed Statement

Speed Function


---

# Speed Statement
**Type:** statement | **Section:** Operator

## Syntax
```
(1) Speed
			percent,  [ departSpeed], [approSpeed ]

(2) Speed
```

## Parameters
percent	Integer expression between 1-100 representing the arm speed as a percentage of the maximum speed.

departSpeed	Integer expression between 1-100 representing the depart motion speed for the Jump instruction.  Available only with Jump command.

approSpeed	Integer expression between 1-100 representing the approach motion speed for the Jump instruction.  Available only with Jump command.

## Description
Speed specifies the arm speed for all point to point motion instructions.  This includes motion caused by the Go, Jump and Pulse robot motion instructions.  The speed is specified as a percentage of maximum speed with the range of acceptable values between 1-100.  (1 represents 1% of the maximum speed and 100 represents 100% of maximum speed).  Speed 100 represents the maximum speed possible.

Depart and approach speed values apply only to the Jump instruction.  If omitted, each defaults to the percent value.

The Speed value initializes to its default value when any one of the following is performed:

Controller Startup

		Motor On

SFree, SLock, Brake

Reset, Reset Error

		Stop button or Quit All stops tasks

In Low Power Mode, the effective speed setting is lower than the default value.  If a higher speed is specified directly (from the command window) or in a program, the speed is set to the default value. In High Power Mode, the motion speed setting is the value specified with Speed.

If higher speed motion is required, set high power mode using Power High and close the safety door.  If the safety door is open, the Speed settings will be changed to their default value.

If Speed is executed when the robot is in low power mode, the following message is displayed.  The following example shows that the robot will move at the default speed (5) because it is in Low Power Mode even though the speed setting value by Speed is 80.

> speed 80

		> speed

Low Power Mode

80

			80 80

>

## Examples
```spel
> speed 80
		> speed

		Low Power Mode

			80
			80 80

>
```

```spel
Function speedtst
		  Integer slow, fast, i
		  slow = 10
		  fast = 100
		  For i = 1 To 10

			    Speed slow
		    Go P0
		    Go P1

			    Speed fast
		    Go P0
		    Go P1
		  Next i
		Fend
```

```spel
> Speed 100,100,50 'Z joint downward speed set to 50
```

```spel
> Speed 50
```

```spel
> Speed
```

```spel
Low Power State: Speed is limited to 5
```

```spel
50
```

```spel
50 50
```

```spel
>
```

## See Also
Robot motion commands

Accel

Go

Jump

Power

Pass

Pulse

Speed Function

SpeedS

Speed Statement Example

Speed can be used from the command window or in a program.  Shown below are simple examples of both methods.

Function speedtst

		  Integer slow, fast, i

		  slow = 10

		  fast = 100

		  For i = 1 To 10

Speed slow

		    Go P0

		    Go P1

Speed fast

		    Go P0

		    Go P1

		  Next i

		Fend

From the command window the user can also set Speed values.

> Speed 100,100,50 'Z joint downward speed set to 50

> Speed 50

> Speed

Low Power State: Speed is limited to 5

50

50 50

>


---

# SpeedR Function
**Type:** reference | **Section:** Operator

## Syntax
```
SpeedR
```

## Description
SpeedR Function

SpeedR Function

## Examples
```spel
Real currSpeedR

currSpeedR = SpeedR
```

## See Also
Returns tool rotation speed value.

AccelR Statement

SpeedR Statement

SpeedR Function Example

Real currSpeedR

currSpeedR = SpeedR


---

# SpeedR Keyword
**Type:** reference | **Section:** Operator

## Description
SpeedR Keyword

SpeedR Keyword

The SpeedR keyword is used in these contexts:

SpeedR Statement

SpeedR Function


---

# SpeedR Statement
**Type:** reference | **Section:** Operator

## Syntax
```
(1) SpeedR
			rotSpeed

(2) SpeedR
```

## Parameters
rotSpeed	Real expression in degrees / second.

Valid entries range of the parameters differs by robot models as follows.

E2C	0.1 to 2631.584

E2S/E2L	0.1 to 1875

E2H	0.1 to 1428

G series	0.1 to 1000

PS series (ProSix)	0.1 to 1000

## Description
SpeedR is effective when the ROT modifier is used in the Move, Arc, Arc3, BMove, TMove, and Jump3CP motion commands.

The SpeedR value initializes to its default value when any one of the following is performed:

Controller Startup

		Motor On

SFree, SLock, Brake

Reset, Reset Error

		Stop button or Quit All stops tasks

## Examples
```spel
SpeedR 200
```

## See Also
Sets or displays the tool rotation speed for CP motion when ROT is used.

AccelR, Arc, Arc3, BMove, Jump3CP, Power, SpeedR Function, TMove

SpeedR Statement Example

SpeedR 200


---

# SpeedS Function
**Type:** function | **Section:** Operator

## Syntax
```
SpeedS [(paramNumber)]
```

## Parameters
paramNumber	Optional.  Integer expression specifying which SpeedS value to return.

1: CP speed

2: Jump3 depart speed

3: Jump3 approach speed

## Description
SpeedS Function

SpeedS Function

See_Also Example

Returns the current SpeedS setting.

## Examples
```spel
Real savSpeeds

savSpeeds =
			SpeedS

Print "Jump3 depart speed = ", Speeds(2)
```

## See Also
SpeedS Statement

SpeedS Function Example

Real savSpeeds

savSpeeds =
			SpeedS

Print "Jump3 depart speed = ", Speeds(2)


---

# SpeedS Statement
**Type:** statement | **Section:** Operator

## Syntax
```
(1) SpeedS speed, [departSpeed], [approSpeed ]

(2) SpeedS
```

## Parameters
speed	Real expression representing the CP motion speed in units of mm/sec.

departSpeed	Optional.  Real expression representing the Jump3 depart speed in units of mm/sec.

approSpeed	Optional.  Real expression representing the Jump3 approach speed in units of mm/sec.

Valid entries range of the parameters:

Other than N series: 0.1 to 2000

N series: 0.1 to 1120

## Description
SpeedS specifies the tool center point speed for use with all the continuous path motion instructions.  This includes motion caused by the Move and Arc instructions.

SpeedS is specified in mm/Sec which represents a Tool Center Point velocity for the robot arm.  Valid entries for SpeedS range is 1-2000 for 6-axis robots and 1-1120 for other robots.  The default value varies from robot to robot. See the robot manual for the default SpeedS values for your robot model.  This is the initial SpeedS value set up automatically by the controller each time main power is turned on.

The SpeedS value initializes to its default value when any one of the following is performed:

Controller Startup

Motor On

SFree, SLock, Brake

Reset, Reset Error

Stop button or Quit All stops tasks

In Low Power Mode, the effective SpeedS setting is lower than the default value.  If a higher speed is specified directly (from the command window) or in a program, the speed is set to the default value.  In High Power Mode, the motion SpeedS setting is the value of SpeedS.

If higher speed motion is required, set high power mode using Power High and close the safety door.  If the safety door is open, the SpeedS settings will be changed to their default value.

If SpeedS is executed when the robot is in low power mode, the following message is displayed.  The following example shows that the robot will move at the default speed (50) because it is in Low Power Mode even though the speed setting value by SpeedS is 800.

> SpeedS 800

Low Power State: SpeedS is limited to 50

>

> SpeedS

Low Power State: SpeedS is limited to 50

800

>

## Examples
```spel
> SpeedS 800
Low Power State: SpeedS is limited to 50
>
> SpeedS
Low Power State: SpeedS is limited to 50
800
>
```

```spel
Function speedtst Integer slow, fast, i slow = 50 fast = 500 For i = 1 To 10
    SpeedS slow
    Move P0
    Move P1
    SpeedS fast
    Move P0
    Move P1 Next i
```

```spel
Fend
```

```spel
> speeds 1000
> speeds 500
> speed 30 'set point to point speed
> go p0 'point to point move
> speeds 100 'set straight line speed in mm/Sec
> move P1 'move in straight line
```

## See Also
Robot motion commands

AccelS

Arc

Jump3, Jump3CP

Move

Speed

SpeedS Statement Example

SpeedS can be used from the command window or in a program. Shown below are simple examples of both methods.

Function speedtst

  Integer slow, fast, i

  slow = 50

  fast = 500

  For i = 1 To 10

    SpeedS slow

    Move P0

    Move P1

    SpeedS fast

    Move P0

    Move P1

  Next i

Fend

From the command window the user can also set SpeedS values.

> speeds 1000

> speeds 500

> speed 30 'set point to point speed

> go p0 'point to point move

> speeds 100 'set straight line speed in mm/Sec

> move P1 'move in straight line


---

# Speeds Keyword
**Type:** reference | **Section:** Operator

## Description
Speeds Keyword

SpeedS Keyword

The Speeds keyword is used in these contexts:

Speeds Statement

Speeds Function


---

# Sqr Function
**Type:** reference | **Section:** Operator

## Syntax
```
Sqr(Operand )
```

## Parameters
Operand	A real expression.

## Description
The Sqr function returns the non-negative square root value of the operand.

Potential Errors

Negative operand:

If the operand is or has a negative numeric value, an error will occur.

## Examples
```spel
>print sqr(2)
```

```spel
1.414214
```

```spel
>
```

```spel
Function sqrtest
		  Real x
		  Print "Please enter a numeric value:"
		  Input x
		  Print "The Square Root of ", x, " is ", Sqr(x)
		Fend
```

## See Also
Abs	Or

And	Sgn

Atan	Sin

Atan2	Str$

Cos	Tan

Int	Val

Mod	Xor

Not

Sqr Function Example

This is a simple Command window example on the usage of the Sqr function.

>print sqr(2)

1.414214

>

The following example shows a simple program which uses Sqr.

Function sqrtest

		  Real x

		  Print "Please enter a numeric value:"

		  Input x

		  Print "The Square Root of ", x, " is ", Sqr(x)

		Fend


---

# StartMain Statement
**Type:** reference | **Section:** Operator

## Syntax
```
StartMain
			mainFuncname
```

## Parameters
mainFuncname	Main function name you want to execute (main ~ main63)

## Description
To execute StartMain, you need to set the [Enable advanced task commands] preference in the Setup | System Configuration | Controller | Preferences page.

If a task is executed using the Xqt statement from a background task, the executed task becomes a background task.  With StartMain, you can execute the main function as a non-background task from a background task.

If you have already executed the main function or execute StartMain from a non-background task, an error occurs.

Caution: 	When executing StartMain command from a program, you must understand the command specification and confirm that the system has the proper conditions for this command.  Improper use such as continuous execution of a command within a loop may deteriorate the system safety.

## Examples
```spel
Function bgmain
			...

		  If Sw(StartMainSwitch) = On And Sw(ErrSwitch) = Off Then
		    StartMain main

			  EndIf
```

```spel
...
		Fend
```

## See Also
Executes the main function from a background task.

This command is for the experienced user and you need to understand the command
specification before use.

Xqt

StartMain Example

Function bgmain

			...

If Sw(StartMainSwitch) = On And Sw(ErrSwitch) = Off Then

		    StartMain main

EndIf

...

		Fend


---

# Stat Function
**Type:** reference | **Section:** Operator

## Syntax
```
Stat (address)
```

## Parameters
address	Defines which status bits to check.

## Description
The Stat instruction returns information as shown in the table below:

Address	Bit	Value	Controller Status Indicated When Bit is On

0	0

to

15	&H1

to

&H8000	Task 1 is being executed (Xqt) or in Halt State

to

Task 16 is being executed (Xqt) or in Halt State

	16	&H10000	Task(s) is being executed

	17	&H20000	Pause condition

	18	&H40000	Error Condition

	19	&H80000	Teach mode

	20	&H100000	Emergency Stop Condition

	21	&H200000	Low Power Mode (Power Low)

	22	&H400000	Safe Guard Input is Closed

	23	&H800000	Enable Switch is Open

	24	&H100000	Undefined

	25	&H200000	Undefined

	26	&H400000	Test mode

	27	&H800000	T2 mode

	28-31		Undefined

1	0	&H1	Log of Stop above target position upon satisfaction of condition in Jump...Sense statement. (This log is erased when another Jump statement is executed).

	1	&H2	Log of stop at intermediate travel position upon satisfaction of condition in Go/Jump/Move...Till statement. (This log is erased when another Go/Jump/Move...Till statement is executed

	2	&H4	Undefined

	3	&H8	Log of stop at intermediate travel position upon satisfaction of condition in Trap statement

	4	&H10	Motor On mode

	5	&H20	Current position is home position

	6	&H40	Low power state

	7	&H80	Undefined

	8	&H100	4th Joint Motor is On

	9	&H200	3rd Joint Motor is On

	10	&H400	2nd Joint Motor is On

	11	&H800	1st Joint Motor is On

	12	&H1000	6th Joint Motor is On

	13	&H2000	5th Joint Motor is On

	14	&H4000	Axis T motor is on

	15	&H8000	Axis S motor is on

	16	&H10000	7th Joint motor is on

	17-31		Undefined

2	0-15	&H1 to &H8000	Task (17~32) is being executed (Xqt) or in Halt State

## Examples
```spel
Function StatDemo Integer rbt1_sts rbt1_sts = RShift((Stat(0) And &H070000), 16) Select TRUE
    Case (rbt1_sts And &H01) = 1
      Print "Tasks are running"
    Case (rbt1_sts And &H02) = 2
      Print "Pause Output is ON"
    Case (rbt1_sts And &H04) = 4
      Print "Error Output is ON" Send
```

```spel
Fend
```

## See Also
EStopOn

TillOn

PauseOn

SafetyOn

Stat Function Example

Function StatDemo
 Integer rbt1_sts

  rbt1_sts = RShift((Stat(0) And &H070000), 16)

  Select TRUE

    Case (rbt1_sts And &H01) = 1

      Print "Tasks are running"

    Case (rbt1_sts And &H02) = 2

      Print "Pause Output is ON"

    Case (rbt1_sts And &H04) = 4

      Print "Error Output is ON"

  Send

Fend


---

# StepID Property
**Type:** property | **Section:** Operator

## Description
This property sets StepID during the execution of the force guide objects.

It is only used when AutoStepID is False.

Values

Minimum value 0

Maximum value 32767

Default: Automatically set according to the numbers of the force guide sequence and the force guide object.

## See Also
Applies To

Contact Object, PressMove Object

AutoStepID Property


---

# Str$ Function
**Type:** reference | **Section:** Operator

## Syntax
```
Str$
			(number)
```

## Parameters
number	Integer or real expression.

## Description
Str$ converts a number to a string. Any positive or negative number is valid.

## Examples
```spel
Function strtest
		  Integer intvar
		  Real realvar
		  '
		  intvar = -32767
		  Print "intvar = ", Str$(intvar)
		  '
		  realvar = 567.9987
		  Print "realvar = ", Str$(realvar)
		  '
		Fend
```

```spel
> Print Str$(99999999999999)

			1.000000E+014

> Print Str$(25.999)

			25.999
```

## See Also
Abs, Asc, Chr$, Int, InStr, Left$, Len, Mid$, Mod, Right$, Sgn, Space$, Val

Str$ Function Example

The example shown below shows a program which coverts several different numbers to strings and then prints them to the screen.

Function strtest

		  Integer intvar

		  Real realvar

		  '

		  intvar = -32767

		  Print "intvar = ", Str$(intvar)

		  '

		  realvar = 567.9987

		  Print "realvar = ", Str$(realvar)

		  '

		Fend

Some other example results from the Str$ instruction from the command window.

> Print Str$(99999999999999)

1.000000E+014

> Print Str$(25.999)

25.999


---

# String Statement
**Type:** reference | **Section:** Operator

## Syntax
```
String varName$ [( subscripts )] [, varName$ [( subscripts )]...
```

## Parameters
varName$	Variable name
		 which the user wants to declare as type String.

subscripts	Optional.
		  Dimensions of an array variable; up to 3 dimensions may
		 be declared.  The subscripts syntax is as follows

(ubound1, [ubound2],
		 [ubound3])

ubound1, ubound2,
		 ubound3 each specify the maximum upper bound for the associated
		 dimension.

The elements
		 in each dimension of an array are numbered from 0 and the available
		 number of array elements is the upper bound value + 1.

When specifying
		 the upper bound value, make sure the number of total elements
		 is within the range shown below:

Local variable
		   200

Global Preserve
		 variable   400

Global variable
		 and module variable   10,000

## Description
String is used to declare variables as type String. Variables of type String can contain up to 255 characters.  Local variables should be declared at the top of a function.  Global and module variables must be declared outside of functions.

String Operators

The following operators can be used to manipulate String variables:
 + Merges character Strings together. Can be used in the assignment statements for String variables or in the Print instruction.

## Notes
Variable Names Must Include "$" Character:

Variables of type String must have the character "$" as the last character in the variable name.

## Examples
```spel
Example: name$ = fname$ + " " + lname$
```

```spel
Example: If temp1$ = "A" Then GoSub test
```

```spel
Example: If temp1$ <> "A" Then GoSub test
```

```spel
String password$
String A$(10) 'Single dimension array of string
String B$(10, 10) 'Two dimension array of string
String C$(5, 5, 5) 'Three dimension array of string

Print "Enter password:"
Input password$
If UCase$(password$) = "EPSON" Then Call RunMaintenance
Else Print "Password invalid!"
EndIf
```

## See Also
Boolean, Byte, Double, Global, Int32, Int64, Integer, Long, Real, Short, UByte, UInt32, UInt64, UShort

String Statement


---

# Sw Function
**Type:** reference | **Section:** Operator

## Syntax
```
Sw(
			bitNumber
			)
```

## Parameters
bitNumber	Integer expression representing an input port.

## Description
Sw provides a status check for the inputs. Sw is most commonly used to check the status of one of the inputs which could be connected to a feeder, conveyor, gripper solenoid, or a host of other devices which works via discrete I/O. Obviously the input checked with the Sw instruction has 2 states (1 or 0). These indicate whether the device is On or Off.

See Also

In, InBCD, MemOn, MemOff, MemOut, MemSW, Off, OpBCD, Oport, Out, Wait

Sw Function Example

The example shown below simply checks the discrete input #5 and branches accordingly. On is used instead of 1 for more clarity.

Function main

		  Integer i, feed5Ready

		  feed5Ready = Sw(5)

		  'Check if feeder is ready

		  If feed5Ready = On Then

		    Call mkpart1

		  Else

		    Print "Feeder #5 is not ready. Please reset and"

		    Print "then restart program"

		  EndIf

		Fend

Other simple examples are as follows from the command window:

> print s
			w(5)

1

>

## Examples
```spel
Function main
		  Integer i, feed5Ready
		  feed5Ready = Sw(5)
		  'Check if feeder is ready
		  If feed5Ready = On Then
		    Call mkpart1
		  Else
		    Print "Feeder #5 is not ready. Please reset and"
		    Print "then restart program"
		  EndIf
		Fend
```

```spel
> print s
			w(5)
```

```spel
1
```

```spel
>
```


---

# SyncLock Statement
**Type:** statement | **Section:** Operator

## Syntax
```
SyncLock syncID [, timeOut]
```

## Parameters
syncID	Integer expression representing signal
		 number to receive.  Range is from 0 to 63.

timeOut	Optional.  Real expression representing
		 the maximum time to wait for lock.

## Description
Use SyncLock to lock use of a common resource so that only one task at a time can use it.  When the task is finished with the resource, it must call SyncUnlock to release the lock so other tasks can use it.

A task can only unlock a syncID that it previously locked.

A task must execute SyncUnlock to release the lock.

If the task is finished, then the lock it previously locked will releases.

When SyncLock is second consecutive used to a same signal number, an error occurs.

If the timeOut parameter is used, then the Tw function must be used to check if the lock was successful.

Note:

In EPSON RC+ 6.0, RC+ 7.0, and Epson RC+ 8.0, the lock is automatically released when the task is finished while it is not in EPSON RC+5.0.

## Examples
```spel
Function Main Xqt Func1 Xqt Func2
Fend

Function Func1 Long count Do
    Wait .5
    count = count + 1
    LogMsg "Msg from Func1, " + Str$(count) Loop
Fend

Function Func2 Long count Do
    Wait .5
    count = count + 1
    LogMsg "Msg from Func2, " + Str$(count) Loop
Fend
```

```spel
Function LogMsg(msg$ As String) SyncLock 1 OpenCom #1 Print #1, msg$ CloseCom #1 SyncUnlock 1
Fend
```

```spel
Function MySyncLock(syncID As Integer) Do
    SyncLock syncID, .5
    If Tw = 0 Then
      Exit Function
    EndIf
    If Sw(1) = On Then
      Off 1
    EndIf Loop
Fend
```

## See Also
Signal, SyncUnlock, Tw, Wait, WaitPos

SyncLock Example

The following example uses SyncLock and SyncUnlock to allow only one task at a time to write a message to a communications port.

Function Main

  Xqt Func1

  Xqt Func2

Fend

Function Func1

  Long count

  Do

    Wait .5

    count = count + 1

    LogMsg "Msg from Func1, " + Str$(count)

  Loop

Fend

Function Func2

  Long count

  Do

    Wait .5

    count = count + 1

    LogMsg "Msg from Func2, " + Str$(count)

  Loop

Fend

Function LogMsg(msg$ As String)

  SyncLock 1

  OpenCom #1

  Print #1, msg$

  CloseCom #1

  SyncUnlock 1

Fend

The following example uses SyncLock with optional time out.  Tw is used to check if the lock was successful.  By using a timeout, you can execute other code periodically while waiting to lock a resource.

Function MySyncLock(syncID As Integer)

  Do

    SyncLock syncID, .5

    If Tw = 0 Then

      Exit Function

    EndIf

    If Sw(1) = On Then

      Off 1

    EndIf

  Loop

Fend


---

# SyncRobots Function
**Type:** reference | **Section:** Operator

## Syntax
```
SyncRobots
```

## Description
SyncRobots function checks the motion reservation status of the SYNC parameter of the robot motion commands. The status the SyncRobots checks are displayed in the bit status corresponding to the robot number. Each bit shows either the robot motion is reserved (1) or not (2). You can start the robot moton reserved using the SyncRobots statement.

## Examples
```spel
Function Main Xqt Func1 Xqt Func2 Do
    Wait 0.1
    If (SyncRobots and &H03) = &H03 Then
       Exit Do
   EndIf Loop SyncRobots 1, 2
Fend

Function Func1 Robot 1 Motor On Go P1 SYNC
Fend
```

```spel
Function Func2 Robot 2 Motor On Go P2 SYNC
Fend
```

## See Also
SyncRobots Statement

SyncRobots Example

The example below uses the SYNC parameter of a motion command and SyncRobots to start the motions of two robots simultaneously.

Function Main

  Xqt Func1

  Xqt Func2

  Do

    Wait 0.1

    If (SyncRobots and &H03) = &H03 Then

       Exit Do

   EndIf

  Loop

  SyncRobots 1, 2

Fend

Function Func1

  Robot 1

  Motor On

  Go P1 SYNC

Fend

Function Func2

  Robot 2

  Motor On

  Go P2 SYNC

Fend


---

# SyncRobots Statement
**Type:** reference | **Section:** Operator

## Syntax
```
SyncRobots
			robotNumber [, robotNumber] [, ...]

SyncRobots
			All
```

## Parameters
robotNumber	Integer expression that specifies a robot number you want to start the motion.

All	All robots whose motion is reserved

## Description
SyncRobots is used to start the robot motion reserved with the SYNC parameter of each motion command.  The robots specified by the SyncRobots start to move in the same timing.  This is more useful than synchronizing the normal multi-task programs by waiting for the I/O signal event because there is no effect of switching tasks.  It can synchronize the robot motion start more precisely.

If a robot number is specified whose motion is not reserved, an error occurs.

## Examples
```spel
Function Main
		  Xqt Func1
		  Xqt Func2
		  Do
		    Wait 0.1
		    If (SyncRobots and &H03) = &H03 Then
		       Exit Do
		    EndIf
		  Loop
		  SyncRobots 1, 2
		Fend

Function Func1
		  Robot 1
		  Motor On
		  Go P1 SYNC
		Fend
```

```spel
Function Func2
		  Robot 2
		  Motor On
		  Go P2 SYNC
		Fend
```

## See Also
SyncRobots Function

SyncRobots Example

The example below uses the SYNC parameter of a motion command and SyncRobots to start the motions of two robots simultaneously.

Function Main

		  Xqt Func1

		  Xqt Func2

		  Do

		    Wait 0.1

		    If (SyncRobots and &H03) = &H03 Then

		       Exit Do

		    EndIf

		  Loop

		  SyncRobots 1, 2

		Fend

Function Func1

		  Robot 1

		  Motor On

		  Go P1 SYNC

		Fend

Function Func2

		  Robot 2

		  Motor On

		  Go P2 SYNC

		Fend


---

# SyncUnlock Statement
**Type:** statement | **Section:** Operator

## Syntax
```
SyncUnlock
			syncID
```

## Parameters
syncID	Integer expression representing signal number to receive.  Range is from 0 to 63.

## Description
Use SyncUnlock to unlock a sync ID previously locked with SyncLock.

A task can only unlock a syncID that it previously locked.

## Examples
```spel
Function Main

Xqt task
		  Xqt task
		  Xqt task
		  Xqt task
		Fend
		Function task
		  Do
		    SyncLock 1
		    Print "resource 1 is locked by task", MyTask
		    Wait .5

			    SyncUnlock 1
		  Loop
		Fend
```

## See Also
Signal, SyncLock, Wait, WaitPos

SyncUnlock Example

Function Main

Xqt task

		  Xqt task

		  Xqt task

		  Xqt task

		Fend

		Function task

		  Do

		    SyncLock 1

		    Print "resource 1 is locked by task", MyTask

		    Wait .5

SyncUnlock 1

		  Loop

		Fend


---

# SysConfig Command
**Type:** reference | **Section:** Operator

## Syntax
```
SysConfig
```

## Description
Display current configurated value for system control data.  When the robot is delivered or after changing the data it is normally a good idea to save this data.  This can be done with Backup Controller from the Controller Tools dialog.

The following data will be displayed. (The following data is for reference only since data will vary from controller to controller.)

'Version:

'   Firmware 1, 0, 0, 0

' Options:

'   External Control Point

'   RC+ API

' HOUR: 414.634

' Controller:

'   Serial #: 0001

' ROBOT 1:

' Name: Mnp01

' Model: PS3-AS10

' Serial #: 0001

' Motor On Time: 32.738

'   Motor 1: Enabled, Power = 400

'   Motor 2: Enabled, Power = 400

'   Motor 3: Enabled, Power = 200

'   Motor 4: Enabled, Power = 50

'   Motor 5: Enabled, Power = 50

'   Motor 6: Enabled, Power = 50

ARCH 0, 30, 30

  ARCH 1, 40, 40

  ARCH 2, 50, 50

  ARCH 3, 60, 60

  ARCH 4, 70, 70

  ARCH 5, 80, 80

  ARCH 6, 90, 90

  ARMSET 0, 0, 0, 0, 0, 0

  HOFS 0, 0, 0, 0, 0, 0

  HORDR 63, 0, 0, 0, 0, 0

  RANGE -7427414, 7427414, -8738134, 2621440, -3145728, 8301227, -5534152, 5534152, -3640889, 3640889, -6553600, 6553600

  BASE 0, 0, 0, 0, 0, 0

  WEIGHT 2, 0

  INERTIA  0.1, 0

  XYLIM 0, 0, 0, 0, 0, 0

' Extended I/O Boards:

'   1: Installed

'   2: Installed

'   3: None installed

'   4: None installed

' Fieldbus I/O Slave Board:

'   Installed

'   Type: PROFIBUS

' Fieldbus I/O Master Board:

'   None installed

' RS232C Boards:

'   1: Installed

'   2: None installed

' PG Boards:

'   1: None installed'

'   2: None installed'

'   3: None installed

'   4: None installed

SysConfig Example

> sysconfig

## Examples
```spel
> sysconfig
```


---

# SysErr
**Type:** reference | **Section:** Operator

## Syntax
```
SysErr [(infoNo)]
```

## Parameters
infoNo	Optional. Integer number representing the error code or warning code to get.

0 : Error code (When the parameter is omitted, 0 is automatically selected.)

1 : Warning code

## Description
SysErr is used only for NoEmgAbort task (special task using NoEmgAbort at Xqt) and background tasks.

Error codes or warning codes of controller are the error codes or warning codes displayed on the LCD.

When there are no errors or warnings, the return value will be 0.

## Notes
Forced Flag

This program example uses Forced flag for On/Off command. Be sure that the I/O outputs change during error, or at Emergency Stop or Safety Door Open when designing the system.

After Error Occurance

As this program, finish the task promptly after completing the error handling.

Function main

  Xqt ErrorMonitor, NoEmgAbort

  :

  :

Fend

Function ErrorMonitor

  Wait ErrorOn

  If 4000 < SysErr Then

    Print "Motion Error = ", SysErr

    Off 10, Forced

    On 12, Forced

  Else

    Print "Other Error = ", SysErr

    Off 11, Forced

    On 13, Forced

  EndIf

Fend

## Examples
```spel
Function main Xqt ErrorMonitor, NoEmgAbort : :
Fend
```

```spel
Function ErrorMonitor Wait ErrorOn If 4000 < SysErr Then
    Print "Motion Error = ", SysErr
    Off 10, Forced
    On 12, Forced Else
    Print "Other Error = ", SysErr
    Off 11, Forced
    On 13, Forced EndIf
Fend
```

## See Also
Returns the latest error status or warning status.

ErrMsg$

ErrorOn

Xqt

SysErr Function Example

The following example shows a program that monitors the controller error and switches the I/O On/Off according to the error number when error occurs.


---

# System History Dialog Box
**Type:** reference | **Section:** Operator

## Description
System History Dialog Box

System History Window

Display [System History]. This window shows events, errors, and warnings that have been logged in the current controller's system history.

The data can be sorted by clicking on any column header. Drop and drop columns to rearrange the order. To sort multiple columns, hold down the shift key and click on multiple columns headers.

Item	Description

Data
		 To Display	Select
		 which data you would like to view. (All, Error, Event, Warning)

From
		 / To	Select
		 the dates you want to view data from. When the window is first
		 opened, these are automatically set to the first and last dates
		 in the history data.

Message
		 Contains	Enter
		 the error message to search, and then click the [Refresh] button,
		 or press the [Enter] key.

Time
		 Zone	Select
		 a time zone. Time of event, warning, and error occurrences are
		 displayed according to the selected time zone.

Refresh	Click
		 this button to reload the data from the controller.

Type	Event	Information
		 for operation and mode change.

Warning	Program
		 can be executed continuously, however, needs countermeasure.

Error	Error
		 occurred in the program or the Robot.

Number	For
		 more details on the number, refer to the following manual:

"Status
		 Code / Error Code List" manual

Message		Displays
		 event, warning, and error messages.

Function
		 and Line number	Function
		 name and the line number are displayed when error occurred while
		 executing a program.

Robot
		 and

		axis number	Robot
		 and the axis number are displayed when Robot error occurred.

Task
		 number	Task
		 number of the task with error is displayed when error occurred
		 while executing the program. "0" is displayed for others.

Additional

		information

		1 and 2	More
		 details are displayed for some errors. Refer to the following
		 manual:

"Status
		 Code / Error Code List" manual


---

# TC Statement
**Type:** reference | **Section:** Operator

## Syntax
```
(1) TC { On | Off }

(2) TC
```

## Parameters
On | Off	On : Torque
		 control mode ON

		Off : Torque control mode OFF

## Description
TC On/Off set the torque control mode available/unavailable.

The torque control mode sets the motor output limit to generate the constant force. This is used in pressing a hand to an object at constant force or making the close contact and coordinate moving of hand with an object .

Before setting the torque control available, configure the limits of torque control and speed control in TCLim and TCSpeed.

Under the torque control, the robot moves as positioning to the target while an operation command is executed. When the robot contact an object and motor output is at the torque control limit, the robot stops its operation and keeps the constant torque.

In any of the following cases, the torque mode turns unavailable.

Controller Startup

		Motor On

		SFree, SLock

		Reset

		Stop button or Quit All stops tasks

## Examples
```spel
Speed 5
Go ApproachPoint

'Set the Z axis torque limit to 20%
TCLim -1, -1, 20, -1
'Set the speed in torque control to 5%
TcSpeed 5

TC On
Go ContactPoint
Wait 3
Go ApproachPoint
TC Off
```

## See Also
TCLim Function

TCSpeed

TC Statement Example

Speed 5

Go ApproachPoint

'Set the Z axis torque limit to 20%

TCLim -1, -1, 20, -1

'Set the speed in torque control to 5%

TcSpeed 5

TC On

Go ContactPoint

Wait 3

Go ApproachPoint

TC Off


---

# TCLim Function
**Type:** function | **Section:** Operator

## Syntax
```
TCLim(jointNumber)
```

## Parameters
jointNumber	Specifies the joint number to retrieve the torque limit from using an expression or numeric value.

The additional S axis is 8 and T axis is 9.

## Description
TCLim Function

TCLim Function

See_Also Example

Returns the current torque limit setting for a specified joint.

## Examples
```spel
Print "The Z axis torque limit: ", TCLim(3)
```

## See Also
TCLim Statement

TCLim Function Example

Print "The Z axis torque limit: ", TCLim(3)


---

# TCLim Statement
**Type:** statement | **Section:** Operator

## Syntax
```
TCLim [ J1TorqueLimit, J2TorqueLimit, J3TorqueLimit, J4TorqueLimit, [J5TorqueLimit], [J6TorqueLimit], [j7Torque limit], [j8Torque limit], [j9Torque limit]  ]
```

## Parameters
J1TorqueLimit	Specifies the proportion to the maximum momentary torque (1 to 100 / unit: %) using an expression or numeric value.

					-1: Disable the torque limit and turns the mode to normal position control.

J2TorqueLimit	Specifies the proportion to the maximum momentary torque (1 to 100 / unit: %) using an expression or numeric value.

					-1: Disable the torque limit and turns the mode to normal position control.

J3TorqueLimit	Specifies the proportion to the maximum momentary torque (1 to 100 / unit: %) using an expression or numeric value.

					-1: Disable the torque limit and turns the mode to normal position control.

J4TorqueLimit	Specifies the proportion to the maximum momentary torque (1 to 100 / unit: %) using an expression or numeric value.

					-1: Disable the torque limit and turns the mode to normal position control.

J5TorqueLimit	Option.  Specifies the proportion to the maximum momentary torque (1 to 100 / unit: %) using an expression or numeric value.

					-1: Disable the torque limit and turns the mode to normal position control.

J6TorqueLimit	Option.  Specifies the proportion to the maximum momentary torque (1 to 100 / unit: %) using an expression or numeric value.

					-1: Disable the torque limit and turns the mode to normal position control.

J7TorqueLimit	Option.  Specifies the proportion to the maximum momentary torque (1 to 100 / unit: %) using an expression or numeric value.

					-1: Disable the torque limit and turns the mode to normal position control.

J8TorqueLimit	Option.  Specifies the proportion to the S axis maximum momentary torque (1 to 100 / unit: %) using an expression or numeric value.

					-1: Disable the torque limit and turns the mode to normal position control.

J9TorqueLimit	Option.  Specifies the proportion to the T axis maximum momentary torque (1 to 100 / unit: %) using an expression or numeric value.

					-1: Disable the torque limit and turns the mode to normal position control.

## Description
Setting to the torque limit becomes available at TC On.

When the limit value is too low, the robot doesn't work and operation command stops before the robot reaches the target position.

In any of the following cases, TCLim set value is initialized.

Controller Startup

Motor On

SFree, SLock

Reset

Stop button or Quit All stops tasks

## Examples
```spel
Speed 5

		Go ApproachPoint

'Set the Z axis torque limit to 20%
		TCLim -1, -1, 20, -1

		'Set the speed in torque control to 5%

		TcSpeed 5

TC On

		Go ContactPoint

		Wait 3

		Go ApproachPoint

		TC Off
```

## See Also
TC Statement

TCLim Function

TCSpeed Statement

TCLim Example

Speed 5

		Go ApproachPoint

'Set the Z axis torque limit to 20%

		TCLim -1, -1, 20, -1

		'Set the speed in torque control to 5%

		TcSpeed 5

TC On

		Go ContactPoint

		Wait 3

		Go ApproachPoint

		TC Off


---

# TCSpeed Function
**Type:** function | **Section:** Operator

## Syntax
```
TCSpeed
```

## Description
TCSpeed Function

TCSpeed Function

See_Also Example

Returns the speed limit in the torque control.

## Examples
```spel
Integer var
		var = TCSpeed
```

## See Also
TC

TCSpeed Statement

TCLim Statement

TCSpeed Example

Integer var

		var = TCSpeed


---

# TCSpeed Statement
**Type:** statement | **Section:** Operator

## Syntax
```
TCSpeed [ speed ]
```

## Parameters
speed	Specifies the proportion to the maximum speed (1 -100 / unit: %) using an expression or numeric value.

## Description
Under the torque control, the speed is limited to the TCSpeed setting despite of the speed settings of such as Speed command.

Error occurs if the speed goes over the limit in the torque control.

In any of the following cases, TCSpeed set value is initialized to 100%:

Controller Startup

Motor On

SFree, SLock, Brake

Reset, Reset Error

Stop button or Quit All stops tasks

## Examples
```spel
Speed 5
		Go ApproachPoint
		' Set Z axis torque limit to 20 %
		TCLim -1, -1, 20, -1

			TCSpeed 5
		TC On
		Go ContactPoint
		Wait 3
		Go ApproachPoint
		TC Off
```

## See Also
TCLim

TCSpeed Function

TCSpeed Statement Example

Speed 5

		Go ApproachPoint

		' Set Z axis torque limit to 20 %

		TCLim -1, -1, 20, -1

TCSpeed 5

		TC On

		Go ContactPoint

		Wait 3

		Go ApproachPoint

		TC Off


---

# TGo Statement
**Type:** reference | **Section:** Operator

## Syntax
```
TGo destination [CP] [searchExpr] [!...!] [SYNC]
```

## Parameters
destination	The target destination of the motion using a point expression.

CP	Optional. Specifies continuous path motion.

searchExpr	Optional. A Till or Find expression.

Till | Find

Till Sw(expr) = {On | Off}

Find Sw(expr) = {On | Off}

!...!	Optional. Parallel Processing statements can be added to execute I/O and other commands during motion.

SYNC	Reserves a motion command. The robot will not move until SyncRobots is executed.

## Description
Executes point to point relative motion in the current tool coordinate system.

Arm orientation attributes specified in the destination point expression are ignored.  The manipulator keeps the current arm orientation attributes.  However, for a 6-Axis manipulator (including N series), the arm orientation attributes are automatically changed in such a way that joint travel distance is as small as possible.

The Till modifier is used to complete TGo by decelerating and stopping the robot at an intermediate travel position if the current Till condition is satisfied.

The Find modifier is used to store a point in FindPos when the Find condition becomes true during motion.

When Till is used and the Till condition is satisfied, the manipulator halts immediately and the motion command is finished.  If the Till condition is not satisfied, the manipulator moves to the destination point.

When Find is used and the Find condition is satisfied, the current position is stored.  Please refer to Find for details.

When parallel processing is used, other processing can be executed in parallel with the motion command.

The CP parameter causes acceleration of the next motion command to start when the deceleration starts for the current motion command.  In this case the robot will not stop at the destination coordinate and will continue to move to the next point.

## Examples
```spel
>TGo XY(100, 0, 0, 0)   'Move 100mm in X direction
```

```spel
'(in the tool coordinate system)
```

```spel
Function TGoTest Speed 50 Accel 50, 50 Power High Tool 0 P1 = XY(300, 300, -20, 0) P2 = XY(300, 300, -20, 0) /L Go P1 Print Here TGo XY(0, 0, -30, 0) Print Here Go P2 Print Here TGo XY(0, 0, -30, 0) Print Here

Fend
```

```spel
[Output]
```

```spel
X:  300.000 Y:  300.000 Z:  -20.000 U     0.000 V:    0.000 W     0.000 /N /0
```

```spel
X:  300.000 Y:  300.000 Z:  -50.000 U     0.000 V:    0.000 W     0.000 /N /0
```

```spel
X:  300.000 Y:  300.000 Z:  -20.000 U     0.000 V:    0.000 W     0.000 /L /0
```

```spel
X:  300.000 Y:  300.000 Z:  -50.000 U     0.000 V:    0.000 W     0.000 /L /0
```

## See Also
Accel

CP

Find

!....! Parallel Processing

Point Assignment

Speed

Till

TMove

Tool

TGo Example

>TGo XY(100, 0, 0, 0)   'Move 100mm in X direction

                        '(in the tool coordinate system)

Function TGoTest

  Speed 50

  Accel 50, 50

  Power High

  Tool 0

  P1 = XY(300, 300, -20, 0)

  P2 = XY(300, 300, -20, 0) /L

  Go P1

  Print Here

  TGo XY(0, 0, -30, 0)

  Print Here

  Go P2

  Print Here

  TGo XY(0, 0, -30, 0)

  Print Here

Fend

[Output]
 X:  300.000 Y:  300.000 Z:  -20.000 U     0.000 V:    0.000 W     0.000 /N /0
 X:  300.000 Y:  300.000 Z:  -50.000 U     0.000 V:    0.000 W     0.000 /N /0
 X:  300.000 Y:  300.000 Z:  -20.000 U     0.000 V:    0.000 W     0.000 /L /0
 X:  300.000 Y:  300.000 Z:  -50.000 U     0.000 V:    0.000 W     0.000 /L /0


---

# TLClr Statement
**Type:** statement | **Section:** Operator

## Syntax
```
TLClr  toolNumber
```

## Parameters
toolNumber	Integer expression representing which of the 3 tools to clear (undefine).  (Tool 0 is the default tool and cannot be cleared.)

## Description
Robot parameter data is stored in compact flash in controller.  Therefore, writing to command flash occurs when executing this command.  Frequent writing to compact flash affect to lifetime of compact flash.  We recommend to use this command minimally.

## See Also
Arm, ArmClr, Armset, Local, LocalClr, Tool, TLSet

TLClr Example

TLClr 1


---

# TLSet Function
**Type:** function | **Section:** Operator

## Syntax
```
TLSet(toolNumber)
```

## Parameters
toolNumber	Integer expression representing the number of the tool to retrieve.

## Description
TLSet Function

TLSet Function

See_Also Example

Returns a point containing the tool definition for the specified tool.

## Examples
```spel
P1 = TLSet(1)
```

## See Also
TLSet Statement

TLSet Function Example

P1 = TLSet(1)


---

# TLSet Keyword
**Type:** reference | **Section:** Operator

## Description
TLSet Keyword

TLSet Keyword

The TLSet keyword is used in these contexts:

TLSet Statement

TLSet Function


---

# TLSet Statement
**Type:** statement | **Section:** Operator

## Syntax
```
(1) TLSet toolNum , toolDefPoint

(2) TLSet toolNum

(3) TLSet
```

## Parameters
toolNum	Integer number from 1-15 representing which of 15 tools to define. (Tool 0 is the default tool and cannot be modified.)

toolDefPoint	P number or P(expr) or point label or point expression.

## Description
Defines the tool coordinate systems Tool 1, Tool 2 or Tool 3 by specifying tool coordinate system origin and rotation angle in relation to the Tool 0 coordinate system (Hand coordinate system).

TLSet 1, XY(50,100,-20,30)

TLSet 2, P10 +X(20)

In this case, the coordinate values of P10 are referenced and 20 is added to the X value. Arm attribute and local coordinate system numbers are ignored.

TlSet for 6-Axis robots

The origin of Tool 0 is the flange side of the sixth joint.  When all joints are at the 0 degree position, the Tool 0 coordinate system's X axis is aligned with the robot coordinate system's Z axis, the Y axis is aligned with the robot coordinate system's X axis, and the Z axis is perpendicular to the flange face, and is aligned with the robot coordinate system's Y axis, as shown in the figure below:

Tool 0 coordinate systems are defined for ceiling and wall mounted robots as shown in the figures below.

TLSet for N series robots

When all joints are at the 0 degree position, the Tool 0 coordinate system's X axis is aligned with the robot coordinate system's -X axis, the Y axis is aligned with the robot coordinate system's Y axis, and the Z axis is aligned with the robot coordinate system's -Z axis, as shown in the figure below:

Robot parameter data is stored in compact flash in controller.  Therefore, writing to command flash occurs when executing this command.  Frequent writing to compact flash affect to lifetime of compact flash.  We recommend to use this command minimally.

## Notes
TLSet values are maintained

The TlSet values are preserved. Use TLClr to clear a tool definition.

## Examples
```spel
TLSet 1, XY(50,100,-20,30)
```

```spel
TLSet 2, P10 +X(20)
```

```spel
> TlSet 1, XY(100, 0, 0, 0) 'Define tool coordinate system for
'Tool 1 (plus 100 mm in x direction
'from hand coordinate system)
> Tool 1   'Selects Tool 1 as defined by TLSet
> TGo P1   'Positions the Tool 1 tip position at P1
> Tool 0   'Tells robot to use no tool for future motion
> Go P1    'Positions the center of the U-Joint at P1
```

## See Also
Arm

ArmSet

TLClr

TLSet Function

Tool

TLSet Statement Example

The example shown below shows a good test which can be done from the command window to help understand the difference between moving when a tool is defined and when no tool is defined.

> TlSet 1, XY(100, 0, 0, 0) 'Define tool coordinate system for

'Tool 1 (plus 100 mm in x direction

'from hand coordinate system)

> Tool 1   'Selects Tool 1 as defined by TLSet

> TGo P1   'Positions the Tool 1 tip position at P1

> Tool 0   'Tells robot to use no tool for future motion

> Go P1    'Positions the center of the U-Joint at P1


---

# TMOut Statement
**Type:** reference | **Section:** Operator

## Syntax
```
TMOut
			seconds
```

## Parameters
seconds	Real expression representing the number of seconds until a timeout occurs.  Valid range is 0-2147483 seconds in 1 second intervals.

## Description
TMOut sets the amount of time to wait (when using the Wait instruction) until a timeout error is issued.  If a timeout of 0 seconds is specified, then the timeout is effectively turned off.  In this case the Wait instruction waits indefinitely for the specified condition to be satisfied.

The default initial value for TMOut is 0.

## Examples
```spel
TMOut 5
		Wait MemSw(0) = On
		If TW Then
		  Print "Time out occurred"
		EndIf
```

## See Also
In, MemSW, OnErr, Sw, Tw, Wait

TMOut Statement Example

TMOut 5

		Wait MemSw(0) = On

		If TW Then

		  Print "Time out occurred"

		EndIf


---

# TMove Statement
**Type:** reference | **Section:** Operator

## Syntax
```
TMove destination  [ROT] [CP] [ searchExpr ] [ !...! ] [SYNC]
```

## Parameters
destination	The target destination of the motion using a point expression.

ROT	Optional.  Decides the speed/acceleration/deceleration in favor of tool rotation.

CP	Optional.  Specifies continuous path motion.

searchExpr	Optional.  A Till or Find expression.

Till | Find

Till Sw(expr) = {On | Off}

Find Sw(expr) = {On | Off}

!...!	Optional.  Parallel Processing statements can be added to execute I/O and other commands during motion.

SYNC	Reserves a motion command. The robot will not move until SyncRobots is executed.

## Description
Executes linear interpolated relative motion in the current tool coordinate system.

Arm orientation attributes specified in the destination point expression are ignored.  The manipulator keeps the current arm orientation attributes.  However, for a 6-Axis manipulator (including N series), the arm orientation attributes are automatically changed in such a way that joint travel distance is as small as possible. This is equivalent to specifying the LJM modifier parameter for Move statement.  Therefore, if you want to change the arm orientation larger than 180 degrees, execute it in several times.

TMove uses the SpeedS speed value and AccelS acceleration and deceleration values.  Refer to Using Move with CP below on the relation between the speed/acceleration and the acceleration/deceleration.  If, however, the ROT modifier parameter is used, TMove uses the SpeedR speed value and AccelR acceleration and deceleration values.  In this case SpeedS speed value and AccelS acceleration and deceleration value have no effect.

Usually, when the move distance is 0 and only the tool orientation is changed, an error will occur.  However, by using the ROT parameter and giving priority to the acceleration and the deceleration of the tool rotation, it is possible to move without an error. When there is not an orientational change with the ROT modifier parameter and movement distance is not 0, an error will occur.

Also, when the tool rotation is large as compared to move distance, and when the rotation speed exceeds the specified speed of the manipulator, an error will occur. In this case, please reduce the speed or append the ROT modifier parameter to give priority to the rotational speed/acceleration/deceleration.

The Till modifier is used to complete TMove by decelerating and stopping the robot at an intermediate travel position if the current Till condition is satisfied.

The Find modifier is used to store a point in FindPos when the Find condition becomes true during motion.

When Till is used and the Till condition is satisfied, the manipulator halts immediately and the motion command is finished.  If the Till condition is not satisfied, the manipulator moves to the destination point.

When Find is used and the Find condition is satisfied, the current position is stored.  Please refer to Find for details.

When parallel processing is used, other processing can be executed in parallel with the motion command.

## Notes
Using TMove with CP

The CP parameter causes the arm to move to destination without decelerating or stopping at the point defined by destination.  This is done to allow the user to string a series of motion instructions together to cause the arm to move along a continuous path while maintaining a specified speed throughout all the motion.  The TMove instruction without CP always causes the arm to decelerate to a stop prior to reaching the point destination.

## Examples
```spel
>TMove XY(100, 0, 0, 0)   'Move 100mm in the X direction
'(in the tool coordinate system)
Function TMoveTest Speed 50 Accel 50, 50 SpeedS 100 AccelS 1000, 1000 Power High Tool 0 P1 = XY(300, 300, -20, 0) P2 = XY(300, 300, -20, 0) /L Go P1 Print Here TMove XY(0, 0, -30, 0) Print Here Go P2 Print Here TMove XY(0, 0, -30, 0) Print Here

Fend
```

```spel
[Output]
```

```spel
X:  300.000 Y:  300.000 Z:  -20.000 U     0.000 V:    0.000 W     0.000 /N /0
```

```spel
X:  300.000 Y:  300.000 Z:  -50.000 U     0.000 V:    0.000 W     0.000 /N /0
```

```spel
X:  300.000 Y:  300.000 Z:  -20.000 U     0.000 V:    0.000 W     0.000 /L /0
```

```spel
X:  300.000 Y:  300.000 Z:  -50.000 U     0.000 V:    0.000 W     0.000 /L /0
```

## See Also
AccelS

CP

Find

!...! Parallel Processing

Point Assignment

SpeedsS

TGo

Till

Tool

TMove Example

>TMove XY(100, 0, 0, 0)   'Move 100mm in the X direction

'(in the tool coordinate system)

Function TMoveTest

  Speed 50

  Accel 50, 50

  SpeedS 100

  AccelS 1000, 1000

  Power High

  Tool 0

  P1 = XY(300, 300, -20, 0)

  P2 = XY(300, 300, -20, 0) /L

  Go P1

  Print Here

  TMove XY(0, 0, -30, 0)

  Print Here

  Go P2

  Print Here

  TMove XY(0, 0, -30, 0)

  Print Here

Fend

[Output]
 X:  300.000 Y:  300.000 Z:  -20.000 U     0.000 V:    0.000 W     0.000 /N /0
 X:  300.000 Y:  300.000 Z:  -50.000 U     0.000 V:    0.000 W     0.000 /N /0
 X:  300.000 Y:  300.000 Z:  -20.000 U     0.000 V:    0.000 W     0.000 /L /0
 X:  300.000 Y:  300.000 Z:  -50.000 U     0.000 V:    0.000 W     0.000 /L /0


---

# TW Function
**Type:** reference | **Section:** Operator

## Syntax
```
TW
```

## Description
The Timer Wait function TW returns the status of the preceding Wait condition with time interval with False (wait condition was satisfied) or True (time interval has elapsed).

## Examples
```spel
Wait Sw(0)=On, 5   'Waits up to 5 seconds for input bit 0 On
If TW = True Then Print "Time Up"  'Displays "Time UP" after 5 seconds
EndIf
```

## See Also
TMOut, Wait, Hand_TW

TW Function Example

Wait Sw(0)=On, 5   'Waits up to 5 seconds for input bit 0 On

If TW = True Then

  Print "Time Up"  'Displays "Time UP" after 5 seconds

EndIf


---

# Tan Function
**Type:** reference | **Section:** Operator

## Syntax
```
Tan(
			radians
			)
```

## Parameters
radians	Real expression given in radians.

## Description
Tan returns the Tangent of the numeric expression. The numeric expression (radians) may be any numeric value as long as it is expressed in radian units.

To convert from radians to degrees, use the RadToDeg function.

## Examples
```spel
Function tantest
		  Real num
		  Print "Enter number in radians to calculate tangent for:"
		  Input num
		  Print "The tangent of ", num, "is ", Tan(num)
		Fend
```

```spel
> print tan(0)
		0.00
		> print tan(45)
		1.6197751905439

>
```

## See Also
Abs	Not

Atan	Sgn

Atan2	Sin

Cos	Sqr

Int	Str$

Mod	Val

Tan Function Example

Function tantest

		  Real num

		  Print "Enter number in radians to calculate tangent for:"

		  Input num

		  Print "The tangent of ", num, "is ", Tan(num)

		Fend

The examples shown below show some typical results using the Tan instruction from the command window.

> print tan(0)

		0.00

		> print tan(45)

		1.6197751905439

>


---

# The Operator Window
**Type:** reference | **Section:** Operator

## Description
The Operator Window

The Operator Window

The Operator Window can be used as a simple interface for operators. You can configure Epson RC+ 8.0 to open only the Operator Window when started. In addition, when Remote Control is being used, the Operator Window can be displayed for monitoring purposes.

Symbol	Item

a	Title

b	Status Bar

c	Operator Button

Item	Description

Status
		 Bar	The status
		 bar is located at the top of the window and shows emergency stop
		 and safeguard status.

		In addition, if a warning is detected from the controller (such
		 as low encoder battery), a warning label will be displayed on
		 the right side of the status bar. If the mouse is over this label,
		 you can see the warning error message. When there is no warning,
		 the warning label is hidden.

Program
		 to Run	Select
		 a program to run.

Start	Starts
		 the selected program.

Stop	Stops
		 all tasks.

Pause	Pauses
		 all tasks that are enabled for pause.

Continue	Continues
		 paused tasks.

Robot
		 Manager	Display
		 the [Robot Manager] dialog in operator mode. It cannot be shown
		 while the program is running.

I/O Monitor	Opens
		 the I/O Monitor in operator mode.

		This window can remain open while programs are running.

System
		 History	Display
		 the [System History] window.

		This window can remain open while programs are running.

Simulator	Opens
		 the [Simulator] window.

		This window can remain open while programs are running.

Number
		 of Displays	Sets
		 the number of displays to be shown.

Camera	Project
		 cameras appear in a drop-down list.

Configure	Opens
		 the [Configure Video Displays] window.

You can set the window to be displayed
		 as the main window.


---

# Till Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Till [ eventCondition ]
```

## Parameters
eventCondition	Input status specified as a trigger

[Event] comparative operator ( =, <>, >=, >, <, <=) [Integer expression]

The following functions and variables can be used in the Event:

Functions :Sw, In, InW, Oport, Out, OutW, MemSw, MemIn, MemInW, Ctr, GetRobotInsideBox, GetRobotInsidePlane, Force, AIO_In, AIO_InW, AIO_Out, AIO_OutW, Hand_On, Hand_Off

Variables :Byte, Int32, Integer, Long, Short, UByte, UInt32, UShort global preserve variable, Global variable, module variable

In addition, using the following operators you can specify multiple event conditions.

Operator : And, Or, Xor

## Description
The Till statement can be used by itself or as a search expression in a motion command statement.

The Till condition must include at least one of the functions above.

When variables are included, their values are computed when setting the Till condition. No use of variable is recommended. Otherwise, the condition may be an unintended condition. Multiple Till statements are permitted. The most recent Till condition remains current until superseded.

When parameters are omitted, the current Till definition is displayed.

## Notes
Till Setting at Main Power On

At power on, the Till condition is initialized to Till Sw(0) = On.

Use of Stat or TillOn to Verify Till

After executing a motion command which uses the Till qualifier there may be cases where you want to verify whether or not the Till condition was satisfied. This can be done through using the Stat function or the TillOn function.

To use a variables in the event condition expression

-Available variables are Integer type (Byte, Int32, Integer, Long, Short, UByte, UInt32, UShort)

-Array variables are not available

-Local variables are not available

-If a variable value cannot satisfy the event condition for more than 0.01 seconds, the system cannot retrieve the change in variables.

-Up to 64 can wait for variables in one system (including the ones used in the event condition expressions such as Wait). If it is over 64, an error occurs during the project build.

-If you specify Byref to a waiting variable on any function call, an error occurs.

-When a variable is included in the right side member of the event condition expression, the value is calculated when starting the motion command. We recommend not using variables in an integer expression to avoid making unintended conditions.

## Examples
```spel
Till Sw(5) = On
```

```spel
Till Sw(5) = On And Till(6) = Off
```

```spel
Till Sw(1) = Off 'Specifies Till condition (Input bit 1 off)
Go P1 Till 'Stop if previous line condition is satisfied

Till Sw(1) = On And Sw($1) = On 'Specify new Till condition
Move P2 Till 'Stop if previous line condition satisfied

Move P5 Till Sw(10) = On 'Stop if condition on this line
'is satisfied

If TillOn Then Print "Till condition occurred"
EndIf
```

## See Also
Find, Go, In, InW, Jump, MemIn, MemSW, Move, Stat, Sw, TillOn

Till Statement Example

Shown below are some sample lines from programs using the Till instruction

Till Sw(1) = Off 'Specifies Till condition (Input bit 1 off)

Go P1 Till 'Stop if previous line condition is satisfied

Till Sw(1) = On And Sw($1) = On 'Specify new Till condition

Move P2 Till 'Stop if previous line condition satisfied

Move P5 Till Sw(10) = On 'Stop if condition on this line

'is satisfied

If TillOn Then

  Print "Till condition occurred"

EndIf


---

# TillOn Function
**Type:** reference | **Section:** Operator

## Syntax
```
TillOn
```

## Description
TillOn Function

TillOn Function

See_Also Example

Returns the current Till status.

## Notes
TillOn returns True if Till condition occurred.

TillOn is equivalent to ((Stat(1) And 2) <> 0).

## Examples
```spel
Go P0 Till Sw(1) = On
		If TillOn Then
		  Print "Till condition occurred during move to P0"
		EndIf
```

## See Also
EStopOn, SafetyOn, Sense, Stat, Till

TillOn Function Example

Go P0 Till Sw(1) = On

		If TillOn Then

		  Print "Till condition occurred during move to P0"

		EndIf


---

# Time Result Force Guide
**Type:** reference | **Section:** Operator

## Description
Returns execution time for a force guide sequence or force guide object.

## Notes
Returns execution time for a force guide sequence or force guide object.

## Examples
```spel
Function TimeTest
     Integer rVar
     Motor On
     FGRun Sequence1
     FGGet Sequence1.Contact01.Time, rVar ' Acquisition of Time
     Print rVar
Fend
```

## See Also
Contact object

FGGet


---

# TimedOut Result Force Guide
**Type:** reference | **Section:** Operator

## Description
It is whether the time-out period set in Timeout property had been reached.

## See Also
Time Result


---

# Tool Function
**Type:** function | **Section:** Operator

## Syntax
```
Tool
```

## Description
Tool Function

Tool Function

See_Also Example

Returns the current tool number.

## Examples
```spel
Integer savTool

savTool = Tool

Tool 2

Go P1

Tool savTool
```

## See Also
Tool Statement

Tool Function Example

Integer savTool

savTool = Tool

Tool 2

Go P1

Tool savTool


---

# Tool Keyword
**Type:** reference | **Section:** Operator

## Description
Tool Keyword

Tool Keyword

The Tool keyword is used in these contexts:

Tool Statement

Tool Function


---

# Tool Statement
**Type:** statement | **Section:** Operator

## Syntax
```
(1) Tool
			toolNumber

(2) Tool
```

## Parameters
toolNumber	Integer expression from 0-15 representing which of 16 tool definitions to use with the upcoming motion instructions.

## Description
Tool selects the tool specified by the tool number (toolNum). When the tool number is 0, no tool is selected and all motions are done with respect to the center of the end effector joint. However, when Tool entry 1, 2, or 3 is selected motion is done with respect to the end of the tool as defined with the tool definition.

Note

Power Off and Its Effect on the Tool Selection:

Turning main power off does not change the tool coordinate system selection.

## Examples
```spel
>tlset 1, 100, 0, 0, 0 'Define tool coordinate system for

			'Tool 1 (plus 100 mm in x direction
			'from hand coordinate system)

>tool 1 'Selects Tool 1 as defined by TLSet
		>tgo p1 'Positions the Tool 1 tip position at P1

>tool 0 'Tells robot to use no tool for future motion
		>go p1 'Positions the center of the U-Joint at P1
```

## See Also
TGo

TLSet

Tool Function

Tool Statement Example

The example shown below shows a good test which can be done from the command window to help understand the difference between moving when a tool is defined and when no tool is defined.

>tlset 1, 100, 0, 0, 0 'Define tool coordinate system for

'Tool 1 (plus 100 mm in x direction

			'from hand coordinate system)

>tool 1 'Selects Tool 1 as defined by TLSet

		>tgo p1 'Positions the Tool 1 tip position at P1

>tool 0 'Tells robot to use no tool for future motion

		>go p1 'Positions the center of the U-Joint at P1


---

# Tools page: Robot Manager Window
**Type:** reference | **Section:** Operator

## Description
Tools page: Robot Manager Window

[Tools]-[Robot Manager]-[Tools] Page

This page allows you to define tool settings for a robot. When the tab is selected, the values of 15 tools you can define are displayed.

When a tool is undefined, then all fields for that tool will be blank. When you enter a value in any of the fields for an undefined robot tool, then the remaining fields will be set to zero.

Click the [Apply] button to define the tool coordinate system.

For more details on tool settings, refer to the following manual:

SPEL+ Language Reference - TLSet Statement

Navigating the grid

Press the [Tab] key to move to the next cell. Press the [Shift] + [Tab] key to move to the previous cell. Press the arrow [↑] or [↓] key to move to the cell above or below.

Item	Description

Tool
		 Wizard	This
		 button starts the Tool Wizard. Follow the instructions for each
		 step of the wizard to define a tool. See details in the next section.

X	The X
		 coordinate of the tool.

Y	The Y
		 coordinate of the tool.

Z	Z offset
		 of tool.

U	Rotation
		 angle of the tool about the Z axis. (roll)

V	Rotation
		 angle of the tool about the Y axis. (pitch)

W	Rotation
		 angle of the tool about the X axis. (yaw)

Apply	Sets
		 the current values.

Restore	Reverts
		 to the previous values.

Clear	Clears
		 all selected values.

Define tools with wizard

A wizard is provided for defining a tools coordinate system. This section describes the procedure for SCARA and 6-axis robots when [Define a tool by using jog & teach] is selected. For details of the Tool definition, refer to 7. Vision Calibration in the Vision Guide 8.0 Software manual.

Using the Tool Wizard for SCARA Robots

(1)    Select [Robot Manager]-[Tools] tab to show the [Tools] page.

(2)    Select [Define a tool by using jog & teach], and then click the [Tool Wizard] button. The following dialog appears.

Select the tool number to define and click the [Next] button.

(3)    Jog the robot until the tool is aligned with the reference point.

Then click the [Teach] button to show the [Jog & Teach] dialog box. Match the tool and the reference point.

(4)    Click the [Teach] button. The following dialog appears.

After rotating the U axis as shown below to change the angle, jog the X and Y axes until the tool is aligned with the reference point. Then click the [Teach] button to show the [Jog & Teach] dialog box. Match the tool and the reference point.

(5)    Click the [Teach] button. The new tool definition is displayed as shown below.

Click the [Finish] button to apply the new definition.

NOTE:  The robot can be calibrated with a different posture from the wizard.

For 6-axis robots (including N series)

NOTE:  There are two calibration methods for 6-axis robots. 3D Tool moves the robot in X, Y, Z, U, V, and W directions to calibrate, while 2D Tool moves the robot in X, Y, Z, and U directions. The robot can be calibrated with 2D Tool only when the robot posture is "V=0 degree, W=0 degree", or "V=0 degree, W=180 degree (-180 degree).

NOTE:  When comparing 2D Tool and 3D Tool, 2D Tool has following advantages and disadvantages. Choose the suitable method according to the intended use.

Advantages:

-     Shorter calibration time than 3D Tool

-     Since V and W axes are not moved, peripherals and cables are less likely to interfere the calibration

Disadvantages:

-     Calibration accuracy may be worse than 3D Tool

-     The Z-axis direction offset is not performed automatically (*1)

* 1: If the Z-axis direction offset is required, enter the offset value in the following dialog box after calibration.

(1)    Select [Robot Manager]-[Tools] tab to show the [Tools] page.

(2)    Select [Define a tool by using jog & teach], and then click the [Tool Wizard] button. The following dialog appears. Select the tool number to define and click the [Next] button.

(3)    Click the [Next] button. Select either 3D Tool or 2D Tool.

(4)    If using 3D Tool, select the number of points to teach, and click the [Next] button.

NOTE:  The "number of points to teach" is the amount of times to teach the same point (reference point) in the robot motion range while changing only the tool direction. The number to teach should be at least three. Although it depends on the teaching accuracy of each point, more accurate tool setting can be set by increasing the number.

To increase the tool setting accuracy, set the angle of approximately 10 degrees or more for J5 pulse in order to avoid singularity near 0 degree when teaching the reference point.

(5)    Jog the robot until the tool is aligned with the reference point.

Then click the [Teach] button to show the [Jog & Teach] dialog box. Match the tool and the reference point.

(6)    Click the [Teach] button. The following dialog appears.

If using 3D Tool, rotate the U, V, and W axes as shown below, and then jog the X, Y, and Z axes until the tool is aligned with the reference point. Repeat teaching until the robot can reach the reference point from other tool orientation as often as you specified in (3).

If using 2D Tool, rotate only the U axis as shown below, and then jog the X, Y, and Z axes until the tool is aligned with the reference point.

Clicking the [Teach] button displays the [Jog & Teach] dialog box for both 3D Tool and 2D Tool. Match the tool and the reference point.

NOTE:  When moving the U, V, and W axes, move the arm upward in order to avoid collision of the tool and the reference point.

For 3D Tool:

For 2D Tool:

(7)    The new tool definition is displayed as shown below. Click [Finish] to apply the new definition.

NOTE:  Although it is recommended to calibrate the robot with the same posture as the wizard, it is possible to calibrate the robot with the different robot posture from wizard. When you don't use the robot with the same posture as the wizard, change the robot posture for five degrees or more. The bigger the robot posture change, the more accurate the tool setting.


---

# Torque Restriction Function
**Type:** function | **Section:** Operator

## Description
Torque Restriction Function

Torque Restriction Function

The torque restriction function reduces damage at the collision similarly with "6.18.10 Collision Detection Function".

The torque restriction value used for this function is defined by adding the margin to the upper limit torque value used in the program in order to avoid malfunction.  By using the torque restriction function, the pressing force can be reduced.

For example, if the torque is restricted at 30%, the pressing force can also be reduced to 30%.  Also, the robot immediately stops when the torque reaches the upper limit value.  By stopping the robot immediately, a further 20-30% reduction effect can be obtained.

When the torque is restricted at 30% and the robot is stopped immediately, the total of less than 25% or equivalent reduction effect can be obtained.

For SCARA robots, the end of the extended shaft may get caught and bent.  To reduce occurrence of the bent shaft, it is recommended to use this function to reduce the pressing force to the maximum degree.

If malfunction occurs, take any of the following measures for the axis of malfunction.

- Set LimitTorqueStop or LimitTorqueStopLp off

- Increase the threshold value of LimitTorque or LimitTorqueLp

To use the torque restriction function for jogging motion, follow the steps below.

(1) Execute PTCLR and start torque measurement.

(2) Execute the jogging motion.

(3) Measure the maximum torque value by PTRQ, and then add the margin to it.

(4) Set LimitTorqeLP and LimitTorqeLPStop.

If the robot is temporarily stopped in the low power motion, the value larger than the normal program operation or jogging motion may be obtained.  In such case, execute the temporary stop while measuring PTRQ and include it into measurement.

For details of the command and function, refer to the following manual.

Epson RC+ 8.0 SPEL+ Language Reference

LimitTorque Statement, LimitTorque Function,

LimitTorqueLP Statement, LimitTorqueLP Function,

LimitTorqueStop Statement, LimitTorqueStop Function,

LimitTorqueStopLP Statement, LimitTorqueStopLP Function

The following is a sample program which automatically configures the collision detection function and the torque restriction function.

The program repeats the motion called "all_ax_move".

The program enables the collision detection function, measures the maximum torque in the first five moves, adds the margin to the measured value (1.2 times if HighPower, 1.4 times if LowPower), and sets the upper limit torque value to stop the robot at the upper limit torque.

This is the example of automatic setting to repeat motion with the above settings from the sixth time.

When the upper limit torque value is changed, the changed value will be considered as "1.0" for the subsequent PTRQ measurement. If the margin of 1.2 times is set, PTRQ will be slightly larger than 0.8, and if the margin of 1.4 rimes is set, PTRQ will be slightly smaller than 0.7.

Setting example)

Function main

    Integer icnt

    Real rtrq(6)

Motor On

    Power High

'    Power Low

    Weight 2

    Speed 50

    Accel 80, 80

icnt = 1

    PTCLR

    LimitTorque 100        'init HighPower limit torque

    LimitTorqueLP 100        'init LowPower  limit torque

    CollisionDetect On

    Do

        Call all_ax_move

        Print PTRQ(1), PTRQ(2), PTRQ(3), PTRQ(4), PTRQ(5), PTRQ(6)

        icnt = icnt + 1

        If icnt = 5 Then

            If Power = 1 Then    'High power case

                Print "LimitTorque set"

                rtrq(1) = PTRQ(1) * 1.2 * LimitTorque(1) + 1.0

                rtrq(2) = PTRQ(2) * 1.2 * LimitTorque(2) + 1.0

                rtrq(3) = PTRQ(3) * 1.2 * LimitTorque(3) + 1.0

                rtrq(4) = PTRQ(4) * 1.2 * LimitTorque(4) + 1.0

                rtrq(5) = PTRQ(5) * 1.2 * LimitTorque(5) + 1.0

                rtrq(6) = PTRQ(6) * 1.2 * LimitTorque(6) + 1.0

                Print LimitTorque(1), LimitTorque(2), LimitTorque(3), LimitTorque(4), LimitTorque(5), LimitTorque(6)

                LimitTorque rtrq(1), rtrq(2), rtrq(3), rtrq(4), rtrq(5), rtrq(6)

                Print LimitTorque(1), LimitTorque(2), LimitTorque(3), LimitTorque(4), LimitTorque(5), LimitTorque(6)

                LimitTorqueStop On

            Else                'Low poser case

                Print "LimitTorqueLP set"

                rtrq(1) = PTRQ(1) * 1.4 * LimitTorqueLP(1) + 1.0

                rtrq(2) = PTRQ(2) * 1.4 * LimitTorqueLP(2) + 1.0

                rtrq(3) = PTRQ(3) * 1.4 * LimitTorqueLP(3) + 1.0

                rtrq(4) = PTRQ(4) * 1.4 * LimitTorqueLP(4) + 1.0

                rtrq(5) = PTRQ(5) * 1.4 * LimitTorqueLP(5) + 1.0

                rtrq(6) = PTRQ(6) * 1.4 * LimitTorqueLP(6) + 1.0

                Print LimitTorqueLP(1), LimitTorqueLP(2), LimitTorqueLP(3), LimitTorqueLP(4), LimitTorqueLP(5), LimitTorqueLP(6)

                LimitTorqueLP rtrq(1), rtrq(2), rtrq(3), rtrq(4), rtrq(5), rtrq(6)

                Print LimitTorqueLP(1), LimitTorqueLP(2), LimitTorqueLP(3), LimitTorqueLP(4), LimitTorqueLP(5), LimitTorqueLP(6)

                LimitTorqueStopLP On

            EndIf

        EndIf

        If icnt > 5 Then

            icnt = 6

        Endif

    Loop While icnt > 0

Fend

Function all_ax_move

    Integer icount

        Go JA(10, 10, 10, 10, 10, 10)

        Go JA(-10, -10, -10, -10, -10, -10)

Fend

## Examples
```spel
Function main
    Integer icnt
    Real rtrq(6)

    Motor On
    Power High
'    Power Low
    Weight 2
    Speed 50
    Accel 80, 80

    icnt = 1
    PTCLR
    LimitTorque 100        'init HighPower limit torque
    LimitTorqueLP 100        'init LowPower  limit torque
    CollisionDetect On
    Do
        Call all_ax_move
        Print PTRQ(1), PTRQ(2), PTRQ(3), PTRQ(4), PTRQ(5), PTRQ(6)
        icnt = icnt + 1
        If icnt = 5 Then
            If Power = 1 Then    'High power case
                Print "LimitTorque set"
                rtrq(1) = PTRQ(1) * 1.2 * LimitTorque(1) + 1.0
                rtrq(2) = PTRQ(2) * 1.2 * LimitTorque(2) + 1.0
                rtrq(3) = PTRQ(3) * 1.2 * LimitTorque(3) + 1.0
                rtrq(4) = PTRQ(4) * 1.2 * LimitTorque(4) + 1.0
                rtrq(5) = PTRQ(5) * 1.2 * LimitTorque(5) + 1.0
                rtrq(6) = PTRQ(6) * 1.2 * LimitTorque(6) + 1.0
                Print LimitTorque(1), LimitTorque(2), LimitTorque(3), LimitTorque(4), LimitTorque(5), LimitTorque(6)
                LimitTorque rtrq(1), rtrq(2), rtrq(3), rtrq(4), rtrq(5), rtrq(6)
                Print LimitTorque(1), LimitTorque(2), LimitTorque(3), LimitTorque(4), LimitTorque(5), LimitTorque(6)
                LimitTorqueStop On
            Else                'Low poser case
                Print "LimitTorqueLP set"
                rtrq(1) = PTRQ(1) * 1.4 * LimitTorqueLP(1) + 1.0
                rtrq(2) = PTRQ(2) * 1.4 * LimitTorqueLP(2) + 1.0
                rtrq(3) = PTRQ(3) * 1.4 * LimitTorqueLP(3) + 1.0
                rtrq(4) = PTRQ(4) * 1.4 * LimitTorqueLP(4) + 1.0
                rtrq(5) = PTRQ(5) * 1.4 * LimitTorqueLP(5) + 1.0
                rtrq(6) = PTRQ(6) * 1.4 * LimitTorqueLP(6) + 1.0
                Print LimitTorqueLP(1), LimitTorqueLP(2), LimitTorqueLP(3), LimitTorqueLP(4), LimitTorqueLP(5), LimitTorqueLP(6)
                LimitTorqueLP rtrq(1), rtrq(2), rtrq(3), rtrq(4), rtrq(5), rtrq(6)
                Print LimitTorqueLP(1), LimitTorqueLP(2), LimitTorqueLP(3), LimitTorqueLP(4), LimitTorqueLP(5), LimitTorqueLP(6)
                LimitTorqueStopLP On
            EndIf
        EndIf
        If icnt > 5 Then
            icnt = 6
        Endif
    Loop While icnt > 0

Fend

Function all_ax_move
    Integer icount
        Go JA(10, 10, 10, 10, 10, 10)
        Go JA(-10, -10, -10, -10, -10, -10)
Fend
```


---

# Trap Statement (User defined trigger)
**Type:** reference | **Section:** Operator

## Syntax
```
Trap trapNumber, eventcondition GoTo {label}

Trap trapNumber, eventcondition Call funcname

Trap trapNumber, eventcondition Xqt funcname

Trap trapNumber
```

## Parameters
trapNumber	Integer number
		 from 1-4 representing which of 4 Trap numbers to use. (SPEL supports
		 up to 4 active Trap interrupts at the same time.)

eventcondition	Input status specified as a trigger

[Event] comparative operator ( =, <>,
		 >=, >, <, <=) [Integer expression]

The following functions and variables
		 can be used in the Event:

Functions :Sw, In, InW, Oport,
		 Out, OutW, MemSw, MemIn, MemInW, Ctr, GetRobotInsideBox, GetRobotInsidePlane,
		 AIO_In, AIO_InW, AIO_Out, AIO_OutW, Hand_On, Hand_Off

Variables
		 :Byte, Int32, Integer, Long, Short, UByte, UInt32, UShort global
		 preserve variable, Global variable, module variable

In addition, using the following operators
		 you can specify multiple event conditions.

Operator : And, Or, Xor

## Description
A Trap executes interrupt processing which is specified by GoTo, Call, or Xqt when the specified condition is satisfied.

The Trap condition must include at least one of the functions above.

When variables are included in the Trap condition, their values are computed when setting the Trap condition. No use of variable is recommended. Otherwise, the condition may be an unintended condition.

Once the interrupt process is executed, its Trap setting is cleared. If the same interrupt process is necessary, the Trap instruction must execute it again.

To cancel a Trap setting simply execute the Trap instruction with only the trapNumber parameter. e.g. "Trap 3" cancels Trap #3.

When the Function that executed Trap GoTo ends (or exit), the Trap Goto will be canceled automatically.

When the declared task ends, Trap Call will be canceled.

Trap Xqt will be canceled when all tasks have stopped.

If GoTo is specified:

In the task set to Trap, the command being executed will be processed as described below, then control branches to the specified line number or label.

- Any arm motion will pause immediately

- Waiting status by the Wait or Input commands will discontinue

- All other commands will complete execution before control branches

If Call is specified:

After executing the same process as GoTo described above, then control branches to the specified line number or label.

Once the function ends, program execution returns to the next statement after the statement where program interruption occurred.  Call statements cannot be used in the Trap processing function.

When an error occurred in the trap processed function, error handling with OnErr will be invalid and an error will occur.

If Xqt is specified:

Program control generates the specified function as an interrupt processing  task.  In this case, the task which executes the Trap command will not wait for the Trap function to finish and will continue to execute.  You cannot execute a task with an Xqt statement from an interrupt processing task.

## Notes
For EPSON RC+4.x user

The Trap Call function of EPSON RC+ 4.x or before is replaced with Trap Xqt in Epson RC+ 8.0.

The Trap GoSub function of EPSON RC+ 4.x or before is removed in Epson RC+ 8.0. Instead, use Trap Call.

To use a variables in the event condition expression

-Available variables are Integer type (Byte, Integer, Long) -Array variables are not available

-Local variables are not available

-If a variable value cannot satisfy the event condition for more than 0.01 seconds, the system cannot retrieve the change in variables.

-Up to 64 can wait for variables in one system (including the ones used in the event condition expressions such as Wait). If it is over 64, an error occurs during the project build.

-If you specify Byref to a waiting variable on any function call, an error occurs.

-When a variable is included in the right side member of the event condition expression, the value is calculated when setting the Trap condition. We recommend not using variables in an integer expression to avoid making unintended conditions.

## Examples
```spel
Trap 1, Sw(5) = On Call, TrapFunc
```

```spel
Trap 1, Sw(5) = On And Till(6) = Off, Call
		 TrapFunc
```

```spel
Function Main Trap 1, Sw(0) = On GoTo EHandle 'Defines Trap . . .
EHandle: On 31 'Signal tower lights OpenCom #1 Print #1, "Error is issued" CloseCom #1
Fend
```

```spel
Function Main Trap 2, MemSw(0) = On Or MemSw(1) = On Call Feeder . . .
Fend
.
Function Feeder Select TRUE
    Case MemSw(0) = On
      MemOff 0
      On 2
    Case MemSw(1) = On
       MemOff 1
      On 3 Send ' Re-arm the trap for next time Trap 2, MemSw(0) = On Or MemSw(1) = On Call Feeder
Fend
```

```spel
Global Integer gi
Function main Trap 1, gi = 5 GoTo THandle Xqt sub Wait 100 Exit Function
THandle: Print "IN Trap ", gi
Fend
Function sub For gi = 0 To 10
    Print gi
    Wait 0.5 Next
Fend
```

## See Also
Call

Era

Erl

Err

Ert

ErrMsg$

GoSub

GoTo

OnErr

Trap Statement Example

[Example 1] Error process defined by User

Sw(0) Input is regarded as an error input defined by user.

Function Main

  Trap 1, Sw(0) = On GoTo EHandle 'Defines Trap

  .

  .

  .

EHandle:

  On 31 'Signal tower lights

  OpenCom #1

  Print #1, "Error is issued"

  CloseCom #1

Fend

[Example 2] Usage like multi-tasking

Function Main

  Trap 2, MemSw(0) = On Or MemSw(1) = On Call Feeder

  .

  .

  .

Fend

.

Function Feeder

  Select TRUE

    Case MemSw(0) = On

      MemOff 0

      On 2

    Case MemSw(1) = On

       MemOff 1

      On 3

  Send

  ' Re-arm the trap for next time

  Trap 2, MemSw(0) = On Or MemSw(1) = On Call Feeder

Fend

[Example 3] Using global variable as event condition

Global Integer gi

Function main

  Trap 1, gi = 5 GoTo THandle

  Xqt sub

  Wait 100

  Exit Function

THandle:

  Print "IN Trap ", gi

Fend

Function sub

  For gi = 0 To 10

    Print gi

    Wait 0.5

  Next

Fend


---

# TriggeredForces Result
**Type:** result | **Section:** Operator

## Description
Returns force and torque for a force guide object when force-related end conditions are achieved.

## Notes
Returns force and torque for a force guide object when force-related end conditions are achieved.

Returns "0" for all values when force-related end conditions are not achieved or end conditions are invalid.

If the number of elements in a specified array variable is less than six, returns force and torque in each direction for the defined element numbers.  Also, if the number of elements in the array variable exceeds six, returns force and torque in each direction from element number 0 to 5, while making no change to element number 6 and above.

## Examples
```spel
Function TriggeredForcesTest
     Double dArray(6)
    Motor On
     FGRun Sequence1
     FGGet Sequence1.Contact01.TriggeredForces, dArray() ' Acquisition of TriggeredForces
    Print dArray(FG_FX)
Fend
```


---

# TriggeredPos Result
**Type:** result | **Section:** Operator

## Description
Returns position for a force guide object when force-related end conditions are achieved.

## Notes
Returns position for a force guide object when force-related end conditions are achieved.

Returns 0 for all values when force-related end conditions are not achieved or end conditions are invalid.

## Examples
```spel
Function EndPosTest
     Motor On
     FGRun Sequence1
     FGGet Sequence1.Contact01.TriggeredPos, P1 ' Acquisition of TriggeredPos

Fend
```


---

# UBound Function
**Type:** reference | **Section:** Operator

## Syntax
```
UBound (arrayName [, dimension])
```

## Parameters
arrayName	Name of the array variable; follows standard variable naming conventions.

dimension	Optional. Integer expression indicating which dimension's upper bound is returned. Use 1 for the first dimension, 2 for the second, and 3 for the third. If dimension is omitted, 1 is assumed.

## Description
UBound Function

UBound Function

See_Also Example

Returns the largest available subscript for the indicated dimension of an array.

## Examples
```spel
Integer i, a(10)

For i=0 to UBound(a)
		  a(i) = i
		Next
```

## See Also
Redim

UBound Function Example

Integer i, a(10)

For i=0 to UBound(a)

		  a(i) = i

		Next


---

# UByte Statement
**Type:** statement | **Section:** Operator

## Syntax
```
UByte varName [( subscripts )] [, varName [( subscripts )]...
```

## Parameters
varName	Variable name which the user wants to declare as UByte type.

subscripts	Optional.  Dimensions of an array variable; up to 3 dimensions may be declared.  The subscripts syntax is as follows

(ubound1, [ubound2], [ubound3])

ubound1, ubound2, ubound3 each specify the maximum upper bound for the associated dimension.

The elements in each dimension of an array are numbered from 0 and the available number of array elements is the upper bound value + 1.

When specifying the upper bound value, make sure the number of total elements is within the range shown below:

Local variable   2000

Global Preserve variable   4000

Global variable and module variable   100000

## Description
UByte is used to declare variables as UByte type.  Variables of UByte type can contain values from 0 to 255.  Local variables should be declared at the top of a function.  Global and module variables must be declared outside of functions.

## Examples
```spel
Function inttest UByte A(10) 'Single dimension array of UByte type UByte B(10, 10) 'Two dimension array of UByte type UByte C(5, 5, 5) 'Three dimension array of UByte type UByte test_ok test_ok = 15  Print "Inital value of test_ok = ", test_ok test_ok = (test_ok And 8) If test_ok <> 8 Then
    Print "test_ok high bit is ON" Else
    Print "test_ok high bit is OFF" EndIf
Fend
```

## See Also
Boolean

Byte

Data Types Overview

Double

Global

Int32

Integer

Long

Real

Short

String

UInt32

UShort

Variable Declarations

Variable Naming Conventions

UByte Statement Example

The following example shows a simple program which declares some variables as Integers using UByte.

Function inttest

  UByte A(10) 'Single dimension array of UByte type

  UByte B(10, 10) 'Two dimension array of UByte type

  UByte C(5, 5, 5) 'Three dimension array of UByte type

  UByte test_ok

  test_ok = 15
  Print "Inital value of test_ok = ", test_ok

  test_ok = (test_ok And 8)

  If test_ok <> 8 Then

    Print "test_ok high bit is ON"

  Else

    Print "test_ok high bit is OFF"

  EndIf

Fend


---

# UInt32 Statement
**Type:** statement | **Section:** Operator

## Syntax
```
UInt32 varName [( subscripts )] [, varName [( subscripts )]...
```

## Parameters
varName	Variable name which the user wants to declare.

subscripts	Optional.  Dimensions of an array variable; up to 3 dimensions may be declared.  The subscripts syntax is as follows

(ubound1, [ubound2], [ubound3])

ubound1, ubound2, ubound3 each specify the maximum upper bound for the associated dimension.

The elements in each dimension of an array are numbered from 0 and the available number of array elements is the upper bound value + 1.

When specifying the upper bound value, make sure the number of total elements is within the range shown below:

Local variable   2000

Global Preserve variable   4000

Global variable and module variable   100000

## Description
UInt32 is used to declare variables as integer type.  Variables of integer type can contain values from 0 to 4294967295.  Local variables should be declared at the top of a function.  Global and module variables must be declared outside of functions.

## Examples
```spel
Function inttest UInt32 A(10) 'Single dimension array of UInt32 type UInt32 B(10, 10) 'Two dimension array of UInt32 type UInt32 C(5, 5, 5) 'Three dimension array of UInt32 type UInt32 var1, arrayvar(10) Integer i Print "Please enter an Integer Number" Input var1 Print "The Integer variable var1 = ", var1 For i = 1 To 5
    Print "Please enter an Integer Number"
    Input arrayvar(i)
    Print "Value Entered was ", arrayvar(i) Next i
Fend
```

## See Also
Boolean

Byte

Data Types Overview

Double

Global

Int32

Integer

Long

Real

Short

String

UByte

UShort

Variable Declarations

Variable Naming Conventions

UInt32 Statement Example

The following example shows a simple program which declares some variables as Integers using UInt32.

Function inttest

  UInt32 A(10) 'Single dimension array of UInt32 type

  UInt32 B(10, 10) 'Two dimension array of UInt32 type

  UInt32 C(5, 5, 5) 'Three dimension array of UInt32 type

  UInt32 var1, arrayvar(10)

  Integer i

  Print "Please enter an Integer Number"

  Input var1

  Print "The Integer variable var1 = ", var1

  For i = 1 To 5

    Print "Please enter an Integer Number"

    Input arrayvar(i)

    Print "Value Entered was ", arrayvar(i)
 Next i

Fend


---

# UInt64 Statement
**Type:** statement | **Section:** Operator

## Syntax
```
UInt64 varName [( subscripts )] [, varName [( subscripts )]...
```

## Parameters
varName	Variable name which the user wants to declare.

subscripts	Optional.  Dimensions of an array variable; up to 3 dimensions may be declared.  The subscripts syntax is as follows

(ubound1, [ubound2], [ubound3])

ubound1, ubound2, ubound3 each specify the maximum upper bound for the associated dimension.

The elements in each dimension of an array are numbered from 0 and the available number of array elements is the upper bound value + 1.

When specifying the upper bound value, make sure the number of total elements is within the range shown below:

Local variable   2000

Global Preserve variable   4000

Global variable and module variable   100000

## Description
UInt64 is used to declare variables as integer type.  Variables of integer type can contain values from 0 to 18446744073709551615.  Local variables should be declared at the top of a function.  Global and module variables must be declared outside of functions.

## Examples
```spel
Function inttest UInt64 A(10) 'Single dimension array of UInt64 type UInt64 B(10, 10) 'Two dimension array of UInt64 type UInt64 C(5, 5, 5) 'Three dimension array of UInt64 type UInt64 var1, arrayvar(10) Integer i Print "Please enter an Integer Number" Input var1 Print "The Integer variable var1 = ", var1 For i = 1 To 5
    Print "Please enter an Integer Number"
    Input arrayvar(i)
    Print "Value Entered was ", arrayvar(i) Next i
Fend
```

## See Also
Boolean

Byte

Data Types Overview

Double

Global

Int32

Integer

Long

Real

Short

String

UByte

UShort

Variable Declarations

Variable Naming Conventions

UInt64 Statement Example

The following example shows a simple program which declares some variables as Integers using UInt64.

Function inttest

  UInt64 A(10) 'Single dimension array of UInt64 type

  UInt64 B(10, 10) 'Two dimension array of UInt64 type

  UInt64 C(5, 5, 5) 'Three dimension array of UInt64 type

  UInt64 var1, arrayvar(10)

  Integer i

  Print "Please enter an Integer Number"

  Input var1

  Print "The Integer variable var1 = ", var1

  For i = 1 To 5

    Print "Please enter an Integer Number"

    Input arrayvar(i)

    Print "Value Entered was ", arrayvar(i)
 Next i

Fend


---

# UShort Statement
**Type:** statement | **Section:** Operator

## Syntax
```
UShort varName [( subscripts )] [, varName [( subscripts )]...
```

## Parameters
varName	Variable name which the user wants to declare.

subscripts	Optional.  Dimensions of an array variable; up to 3 dimensions may be declared.  The subscripts syntax is as follows

(ubound1, [ubound2], [ubound3])

ubound1, ubound2, ubound3 each specify the maximum upper bound for the associated dimension.

The elements in each dimension of an array are numbered from 0 and the available number of array elements is the upper bound value + 1.

When specifying the upper bound value, make sure the number of total elements is within the range shown below:

Local variable   2000

Global Preserve variable   4000

Global variable and module variable   100000

## Description
UShort is used to declare variables as integer type.  Integer variables can contain values from 0 to 65535.  Local variables should be declared at the top of a function.  Global and module variables must be declared outside of functions.

## Examples
```spel
Function ushorttest UShort A(10) 'Single dimension array of UShort type UShort B(10, 10) 'Two dimension array of UShort type UShort C(5, 5, 5) 'Three dimension array of UShort type UShort var1, arrayvar(10) Integer i Print "Please enter an Integer Number" Input var1 Print "The Integer variable var1 = ", var1 For i = 1 To 5
    Print "Please enter an Integer Number"
    Input arrayvar(i)
    Print "Value Entered was ", arrayvar(i) Next i
Fend
```

## See Also
Boolean

Byte

Data Types Overview

Double

Global

Int32

Integer

Long

Real

Short

String

UByte

UInt32

Variable Declarations

Variable Naming Conventions

UShort Statement Example

The following example shows a simple program which declares some variables as Integers using UShort.

Function ushorttest

  UShort A(10) 'Single dimension array of UShort type

  UShort B(10, 10) 'Two dimension array of UShort type

  UShort C(5, 5, 5) 'Three dimension array of UShort type

  UShort var1, arrayvar(10)

  Integer i

  Print "Please enter an Integer Number"

  Input var1

  Print "The Integer variable var1 = ", var1

  For i = 1 To 5

    Print "Please enter an Integer Number"

    Input arrayvar(i)

    Print "Value Entered was ", arrayvar(i)
 Next i

Fend


---

# VRT page
**Type:** reference | **Section:** Operator

## Description
a comment for the selected VRT number. (Optional)

Apply	Sets
		 the current values.

Allow several seconds for processing.

Restore	Reverts
		 to the previous values.

Clear	Clears
		 all selected values.

Select
		 VRT number	Select
		 the number set for the VRT parameter to apply the VRT function
		 for this number to all subsequent robot actions.

However, this setting will take precedence
		 if a VRT command is executed during operations.

0: VRT OFF


---

# Val Function
**Type:** reference | **Section:** Operator

## Syntax
```
Val
			(string)
```

## Parameters
string	String expression which contains only numeric characters.

## Description
Val converts a character string of numbers into a numeric value.  The result may be an integer or floating point number.  If the string passed to the Val instruction contains a decimal point then the return value will be a floating point number.  Otherwise it will be an integer.

## Examples
```spel
Function ValDemo
		  String realstr$, intstr$
		  Real realsqr, realvar
		  Integer intsqr, intvar

realstr$ = "2.5"
		  realvar = Val(realstr$)
		  realsqr = realvar * realvar
		  Print "The value of ", realstr$, " squared is: ", realsqr

intstr$ = "25"
		  intvar = Val(intstr$)
		  intsqr = intvar * intvar
		  Print "The value of ", intstr$, " squared is: ", intsqr
		Fend
```

```spel
> Print Val("25.999")
		25.999

>
```

## See Also
Abs

Asc

Chr$

Int

Hex$

Left$

Len

Mid$

Mod

Right$

Sgn

Space$

Str$

Val Function Example

The example shown below shows a program which coverts several different strings to numbers and then prints them to the screen.

Function ValDemo

		  String realstr$, intstr$

		  Real realsqr, realvar

		  Integer intsqr, intvar

realstr$ = "2.5"

		  realvar = Val(realstr$)

		  realsqr = realvar * realvar

		  Print "The value of ", realstr$, " squared is: ", realsqr

intstr$ = "25"

		  intvar = Val(intstr$)

		  intsqr = intvar * intvar

		  Print "The value of ", intstr$, " squared is: ", intsqr

		Fend

Here's another example from Command window.

> Print Val("25.999")

		25.999

>


---

# Wait Statement
**Type:** reference | **Section:** Operator

## Syntax
```
(1) Wait time

(2) Wait inputcondition

(3) Wait inputcondition, time
```

## Parameters
time	Real expression between 0 and 2,147,483 which represents the amount of time to wait when using the Wait instruction to wait based on time. Time is specified in seconds. The smallest increment is 0.01 seconds.

inputCondition	The following syntax can be used to specify the inputcondition:

[Event] Comparative operator ( =, <>, >=, >, <, <= ) [Integer expression]

The following functions and variables can be used in the Event.

Functions :AtHome, Sw, In, InW, Oport, Out, OutW, MemSw, MemIn, MemInW, Ctr, GetRobotInsideBox, GetRobotInsidePlane, MCalComplete, Motor, LOF, ErrorOn, SaftyOn, EstopOn, TeachOn, Cnv_QueLen, WindowsStatus, LatchState, WorkQue_Len, PauseOn, AIO_In, AIO_InW, AIO_Out, AIO_OutW, Hand_On, Hand_Off

Variables:Byte, Int32, Integer, Long, Short, UByte, UShort global preserve variables, global variables, module variables

In addition, using the following operators you can specify multiple input conditions.

Operator : And, Or, Xor, Mask

## Description
(1) Wait with Time Interval:

When used as a timer, the Wait instruction causes the program to pause for the amount of time specified and then continues program execution.

(2) Wait for Input Conditions without Time Interval

When used as a conditional Wait interlock, the Wait instruction causes the program to wait until specified conditions are satisfied. If after TMOut time interval has elapsed and the Wait conditions have not yet been satisfied, an error occurs.  The user can check multiple conditions with a single Wait instruction by using the And, Mask, Or, or Xor instructions. (Please review the example section for Wait.)

(3) Wait with Input Condition and Time Interval:

Specifies Wait condition and time interval.  After either Wait condition is satisfied, or the time interval has elapsed, program control transfers to the next command.  Use Tw to verify if the Wait condition was satisfied or if the time interval elapsed.

## Notes
Specifying a Timeout for Use with Wait

When the Wait instruction is used without a time interval, a timeout can be specified which sets a time limit to wait for the specified condition.  This timeout is set through using the TMOut instruction.  Please refer to this instruction for more information. (The default setting for TMOut is 0 which means no timeout.)

Wait for variable with Wait

- Available variables are Integer type (Byte, Int32, Integer, Long, Short, UByte, UInt32, UShort)

-Array variables are not available

-Local variables are not available

-If variables value cannot satisfy the event condition for more than 0.01 seconds, the change in variables may not be retrieved.

-Up to 64 can wait for variables in one system (including ones used in the event condition expressions such as Till). If it is over 64, an error occurs during the project build.

-If you specify Byref to a waiting variable on any function call, an error occurs.

-When a variable is included in the right side member of the event condition expression, the value is calculated when setting the Trap condition. We recommend not using variables in an integer expression to avoid making unintended conditions.

## Examples
```spel
Function main Integer i MemOff 1 Xqt 2, task2 For i = 1 to 100
    Wait MemSw(1) = Off
    Go P(i)
    MemOn 1 Next i
Fend
```

```spel
Function task2 Integer i For i = 101 to 200
    Wait MemSw(1) = On
    Go P(i)
    MemOff 1 Next i
Fend

' Wait until input 0 turns on
Wait Sw(0) = On

' Wait 60.5 secs and then continue execution
Wait 60.5

' Wait until input 0 if off and input 1 is on
Wait Sw(0) = Off And Sw(1) = On

' Wait until memory bit 0 is on or memory bit 1 is on
Wait MemSw(1) = 1 Or MemSw(1) = 1
```

```spel
'Wait one second, then turn output bit 1 on
Wait 1; On 1
```

```spel
' Wait for the lower 3 bits of input port 0 to equal 1
```

```spel
Wait In(0) Mask 7 = 1
```

```spel
' Wait until the global Integer type variable giCounter is over 10
```

```spel
Wait giCounter > 10
```

```spel
' Wait ten seconds, until the global Long type variable glCheck is 30000
```

```spel
Wait glCheck = 30000, 10
```

## See Also
Ctr, ErrorOn, EstopOn, In, InsideBox, InsidePlane, InW, MemIn, MemOn, MemOff, MemOut, MemSW, Off, On, OpBCD, Oport, Out, OutW, SafetyOn, Sw, TMOut

Wait Statement Example

The example shown below shows 2 tasks each with the ability to initiate motion instructions.  However, a locking mechanism is used between the 2 tasks to ensure that each task gains control of the robot motion instructions only after the other task is finished using them.  This allows 2 tasks to each execute motion statements as required and in an orderly predictable fashion.  MemSw is used in combination with the Wait instruction to wait until the memory I/O #1 is the proper value before it is safe to move again.

Function main

  Integer i

  MemOff 1

  Xqt 2, task2

  For i = 1 to 100

    Wait MemSw(1) = Off

    Go P(i)

    MemOn 1

  Next i

Fend

Function task2

  Integer i

  For i = 101 to 200

    Wait MemSw(1) = On

    Go P(i)

    MemOff 1

  Next i

Fend

' Wait until input 0 turns on

Wait Sw(0) = On

' Wait 60.5 secs and then continue execution

Wait 60.5

' Wait until input 0 if off and input 1 is on

Wait Sw(0) = Off And Sw(1) = On

' Wait until memory bit 0 is on or memory bit 1 is on

Wait MemSw(1) = 1 Or MemSw(1) = 1

'Wait one second, then turn output bit 1 on

Wait 1; On 1

' Wait for the lower 3 bits of input port 0 to equal 1

Wait In(0) Mask 7 = 1

' Wait until the global Integer type variable giCounter is over 10

Wait giCounter > 10

' Wait ten seconds, until the global Long type variable glCheck is 30000

Wait glCheck = 30000, 10


---

# WaitNet Statement
**Type:** reference | **Section:** Operator

## Syntax
```
WaitNet #portNumber [, timeOut]
```

## Parameters
portNumber	Integer expression for TCP/IP port number to connect.
  Range is 201 - 216

timeOut	Optional.  Maximum time to wait for connection.

## Description
WaitNet Statement

WaitNet Statement

See_Also Example

Wait for TCP/IP port connection to be established.

## Examples
```spel
Function tcpip1
		  OpenNet #201 As Server

			  WaitNet #201
		  Print #201, "Data from host 1"
		Fend
```

```spel
Function tcpip2
		  String data$
		  OpenNet #201

			  WaitNet #201
		  Input #201, data$
		  Print "received '", data$, "' from host 1"
		Fend
```

## See Also
CloseNet

OpenNet

WaitNet Statement Example

For this example, two controllers have their TCP/IP settings configured as follows:

Controller #1:

Port: #201

Host Name: 192.168.0.2

TCP/IP Port: 1000

Function tcpip1

		  OpenNet #201 As Server

WaitNet #201

		  Print #201, "Data from host 1"

		Fend

Controller #2:

Port: #201

Host Name: 192.168.0.1

TCP/IP Port: 1000

Function tcpip2

		  String data$

		  OpenNet #201

WaitNet #201

		  Input #201, data$

		  Print "received '", data$, "' from host 1"

		Fend


---

# WaitPos Statement
**Type:** reference | **Section:** Operator

## Syntax
```
WaitPos
```

## Description
Normally, when path motion is active (CP On or CP parameter specified), the motion command starts the next statement as deceleration starts.

Use the WaitPos command right before the motion to complete the deceleration motion and go on to the next motion.

## Examples
```spel
Off 1

CP On

Move P1

Move P2

WaitPos ' wait for robot to decelerate

On 1

CP Off
```

## See Also
Wait

WaitSig

Cp

WaitPos Statement Example

Off 1

CP On

Move P1

Move P2

WaitPos ' wait for robot to decelerate

On 1

CP Off


---

# WaitSig Statement
**Type:** reference | **Section:** Operator

## Syntax
```
WaitSig signalNumber [, timeOut]
```

## Parameters
signalNumber	Integer expression representing signal number to receive.  Range is from 0 to 63.

timeOut	Optional.  Real expression representing the maximum time to wait.

## Description
Use WaitSig to wait for a signal from another task.  The signal will only be received after WaitSig has started. Previous signals are ignored.

## Examples
```spel
Function Main Xqt SubTask Wait 1 Signal 1
Fend

Function SubTask WaitSig 1 Print "signal received" .
Fend
```

## See Also
Wait

WaitPos

Signal

WaitSig Example

Function Main

  Xqt SubTask

  Wait 1

  Signal 1

Fend

Function SubTask

  WaitSig 1

  Print "signal received"

  .

Fend


---

# Weight Function
**Type:** function | **Section:** Operator

## Syntax
```
Weight(paramNumber)
```

## Parameters
paramNumber	Integer expression containing one of the values below:

1: Payload weight

2: Arm length

3: Load on the additional S axis

4: Load on the additional T axis

## Description
Weight Function

Weight Function

See_Also Example

Returns a Weight parameter.

## Examples
```spel
Print "The current Weight parameters are: ", Weight(1)
```

## See Also
Inertia, Weight Statement

For details of hand, refer to the Hand Function Manual.

Weight Function Example

Print "The current Weight parameters are: ", Weight(1)


---

# Weight Statement
**Type:** statement | **Section:** Operator

## Syntax
```
Weight [payloadWeight [, distance | S | T ]]

Weight
```

## Parameters
payloadWeight	Optional (It
		 is not possible to omit only payloadWeight). The weight of the
		 end effector to be carried in Kg unit.

distance	Optional.
		 The distance from the rotational center of the second arm to the
		 center of the gravity of the end effector in mm unit.  Valid
		 only for SCARA robots (including RS series).

S	Load weight
		 against the additional S axis in kg to 2 decimal places)

T	Load weight
		 against the additional T axis in kg to 2 decimal places)

## Description
Specifies parameters for calculating Point to Point motion maximum acceleration.  The Weight instruction specifies the weight of the end effector and the parts to be carried.

The Arm length (distance) specification is necessary only for SCARA robots (including RS series).  It is the distance from the second arm rotation joint centerline to the hand/workpiece combined center of gravity.

If the robot has the additional axis, the loads on the additional axis must be set with the S, T parameters.

If the equivalent value workpiece weight calculated from specified parameters exceeds the maximum allowable payload, an error occurs.

Robot parameter data is stored in compact flash in controller.  Therefore, writing to command flash occurs when executing this command.  Frequent writing to compact flash affect to lifetime of compact flash.  We recommend to use this command minimally.

You can also set by following "Weight, Inertia, and Eccentricity/offset Measurement Utility".

The following manual describes the details.

Epson RC+ User's Guide 6.18.12 Weight, Inertia, and Eccentricity / Offset Measurement Utility

Potential

## Examples
```spel
> weight
2.000, 200.000
>
```

```spel
> weight 3.0
```

```spel
> weight 30.0, S
```

## See Also
Accel, Inertia, Weight Function

For details of hand, refer to the Hand Function Manual.

Weight Statement


---

# Weight page, Robot Manager dialog
**Type:** reference | **Section:** Operator

## Description
Weight page, Robot Manager dialog

[Tools]-[Robot Manager]-[Weight] Panel

This page is for changing the Weight parameters for the robot.

For more details on Weight settings, refer to the following manual:

SPEL+ Language Reference - Weight Statement

You can also set by following "Weight, Inertia, and Eccentricity/offset Measurement Utility".

The following section describes the details.

Weight, Inertia, and Eccentricity/offset Measurement Utility

Item	Description

Weight	Type
		 in the new total weight of the payload on the robot.

kg/lbs	Select
		 which unit you would like to view. (kg/lbs)

Length	Change
		 it when you use SCARA robots with special specifications which
		 length of Arm #2 has been changed. The arm length is the distance
		 from the center of the second axis to the center of the third
		 axis.

Apply	Sets
		 the current values.

Restore	Reverts
		 to the previous values.

Defaults	Displays
		 factory default settings.


---

# Weight, Inertia, and Eccentricity / Offset Measurement Utility
**Type:** reference | **Section:** Operator

## Parameters
methods	Measurement
		 speed	J1	J2	J3	J4	J5	J6

WEIGHT/

		OFFSET	Static	Low speed	0 deg	0
		 deg	-3
		 to 3 deg	0
		 deg	-3
		 to 3 deg	0
		 deg

INERTIA	Iteration	High
		 speed	0
		 deg	0 deg	0 deg	0 deg	0 deg	270
		 to -360 deg

version
		 1.3 compatible models *1

Measurement
		 methods	Measurement
		 speed	C4, C8, C12,

		C4-B, C8-B, C12-B

		VT6

		*2, *3

WEIGHT/OFFSET	Static	Low speed	¡

INERTIA	Iteration	High speed	¡

A combination
		 of measurements			Staic &
		 iteration

* 1: Refer to readme in the project folder for the compatible models in the latest version.

* 2: N2 and N6 are not compatible.

* 3: The wall mounting type is not compatible.

Table 2: Measurement methods and compatible models for the SCARA robot (Static & iteration, or iteration only)

Measurement
		 posture (angle for each axis), motion area (motion range angle
		 for each axis)

Measurement
		 methods	Measurement
		 speed	J1	J2	J3	J4

WEIGHT	Static	Low speed	0 deg	0 deg	0 to -50mm	0 deg

WEIGHT	Iteration	High speed	0 deg	0 to 90 deg	0 mm	0, 180 deg

INERTIA	Iteration	High speed	0 deg	0 deg	0 mm	-180 to 180
		 deg

Eccentricity	Iteration	High speed	0 to 90 deg	-75 to 90
		 deg	0 mm	-360 to 360
		 deg

Eccentricity
		 (for RS3 and RS4)	Iteration	High
		 speed	0
		 to 90 deg	55
		 to 220 deg	0
		 mm	-360 to 360
		 deg

version
		 1.3 compatible models *1

Measurement
		 methods	Measurement
		 speed	GX4, GX8

		GX4-B, GX8-B

		GX10-B, GX20-B

LS3-B,
		 LS6-B, LS10-B, LS20-B *2	RS3, RS4	G3, G6, G10,
		 G20 *3

		T3, T6, T3-B, T6-B

		LS3, LS6, LS20

		LS3-B*V1, LS6-B*V1

WEIGHT	Static	Low speed	¡	-	-

WEIGHT	Iteration	High speed	-	¡	¡

INERTIA	Iteration	High speed	¡	¡	¡

Eccentricity	Iteration	High speed	¡	-	¡

Eccentricity
		 (for RS3 and RS4)	Iteration	High
		 speed	-	¡	-

A combination
		 of measurements			Staic
		 & iteration	Iteration
		 only

* 1: Refer to readme in the project folder for the compatible models in the latest version.

*2: Excludes LS3-B*V1/LS6-B*V1.

* 3: G1 is not compatible.

Preparation for measurement

When measuring, secure the necessary space for the operation and attach an end effector to the robot to measure. The motion range depends on the model and the corresponding measurement method. Refer to table 1 and 2. This measurement utility also operates in the simulator. Check the motion range on the simulator beforehand. You can also check the approximate measurement time on the simulator. For high-speed measurements, operates with speed 100, accel 100, 100. It cannot be measured with an end effector which strength cannot withstand high speed. In addition, to move a wide motion range, measure without connecting wiring or piping.

Measurement and measurement time

Run a program written in the SPEL+ language to measure.

Destination to save: C:\EpsonRC80\projects\Utilities (for default installation)

Project name: WeightInertiaMeasurement

Execute the main function first.

For the 6-axis robot: Measures in order of weight, offset, and inertia.

For the SCARA robot: Measures in order of weight, inertia, and offset.

The measurement time takes 4 to 13 minutes. A high-payload (20kg) SCARA robot takes the longest time.

Check for the start of the measurement and the operation at low speed

Before starting the measurement, the following message appears:

Start Measurement: [y: yes, n: no]:

?

To measure, enter "y" or "Y". If you enter any other characters, the measurement exits.

When you enter "y" or "Y", after checking the motion range of all measurements at low speed, measures. Make sure that there are no problems with the motion range. The measurement time takes 2 to 4 minutes.

Display of the setting parameters before starting the measurement

The three setting parameters before starting the measurement appear as follows. It changes when you start the measurement. To return the parameters after measuring, modify them manually.

An example for the SCARA robot:

Current Weight: 1 kg, Current Inertia: 0.016 kgm2, Current Eccentricity: 0 mm.

An example for the 6-axis robot:

Current Weight: 1 kg, Current Inertia: 0.03 kgm2, Current Offset: 0 mm.

Parameter settings by the measurement

After the measurement starts, the above three parameters are changed, and the parameter is confirmed in the order of measurements and set to the Controller. All three parameters are set and the measurement ends. If the measurement is quit in the middle, the setting of the parameter values is not ensured. It is not possible to resume the measurement from the middle. If you quit, start the measurement again from the beginning.

Measurement details and what appears in the Run window

An example of the measurement is shown below. "<<" is a supplementary explanation.

An example of the 6-axis robot measurement (C8, combination of measurement: Static & Iteration)

Weight,Inertia,Offset/Eccentricity Measurement Utility  ver. 1.0.0. << version display

2022/9/7  10:39:52

Model: C8-A701S, PerformMode  0

Max Weight: 8 kg, Max Inertia: 0.15 kgm2, Max Offset: 300 mm.

Current Weight: 1 kg, Current Inertia: 0.03 kgm2, Current Offset: 0 mm. <<current set value

ROBOT MOVEMENT AREA

WEIGHT,OFFSET Measurement Movement Area: J1, J2, J4, J6 [0 deg.]; J3, J5 [-3 to 3 deg.]

INERTIA Measurement Movement Area: J1, J2, J3, J4, J5 [0 deg.]; J6 [270 to -360 deg.]

Start Measurement: [y: yes, n: no]:

?y << check for the start of the measurement

WEIGHT,OFFSET Measurement Movement Area: J1, J2, J4, J6 [0 deg.]; J3, J5 [-3 to 3 deg.]

Area Movement Check [Low Power Mode] << low-speed operation for the weight and the offset measurement motion range

INERTIA Measurement Movement Area: J1, J2, J3, J4, J5 [0 deg.]; J6 [270 to -360 deg.]

Area Movement Check [Low Power Mode] << low-speed operation for the inertia measurement motion range

---------------------------------------------------------------

Start of WEIGHT,OFFSET Measurement for 6axis [Static Method]

---------------------------------------------------------------

Warm up Movement: J3, J5 (Repeats 10 times)[High Power Mode] << warm-up operation

Start Measurement J3, J5 (Repeats 6 times)

Measurement 1. << starts measurements for the weight and offset (six measurements)

Measurement 2.

Measurement 3.

Measurement 4.

Measurement 5.

Measurement 6.

---------------------------------------

WEIGHT 5.7 kg, OFFSET 35 mm  << the measurements and set values for the weight and the offset

---------------------------------------

WEIGHT,OFFSET Measurement and Settings Completed.

------------------------------------------------------------

Start of INERTIA Measurement for 6axis [Iteration Method]

------------------------------------------------------------

Current weight : 5.7 kg, Current offset : 35 mm

Warm up Movement: J6 (Repeats 5 times)[High Power Mode] << warm-up operation

Start INERTIA Measurement: J6

Measurement 1. << starts the measurement for the inertia (one to twelve measurements)

Measurement 2.

Measurement 3.

-----------------------

INERTIA : 0.13 kg*m2 << measured value for the inertia

-----------------------

INERTIA Measurement and Settings Completed.

-----------------------------------------------------------

WEIGHT : 5.7 kg, INERTIA : 0.13 kg*m2, OFFSET : 35 mm << final result and the set value

-----------------------------------------------------------

motor off

2022/9/7  10:43:19

------------- COMPLETE -----------------

An example of the SCARA robot measurement (GX8, combination of measurement: Static & Iteration)

Weight,Inertia,Offset/Eccentricity Measurement Program ver. 1.0.0. << version display

2022/9/7  10:52:40

Model: GX8-A553S, PerformMode  0

Max Weight: 8 kg, Max Inertia: 0.16 kgm2, Max Eccentricity: 150 mm.

Current Weight: 4 kg, Current Inertia: 0.01 kgm2, Current Eccentricity: 0 mm. <<current set value

ROBOT MOVEMENT AREA

WEIGHT Measurement Movement Area: J1, J2 [0 deg.]; J3 [0 to -50 mm.]; J4 [0 deg.]

INERTIA Measurement Movement Area: J1 [0 deg]; J2 [90 deg]; J3 [0mm]; J4 [-180 to 180 deg.]

ECCENTRICITY Measurement Movement Area: J1 [0 to 90 deg]; J2 [-75 to 90 deg.]; J3 [0mm]; J4 [-360 to 360 deg.]

Start Measurement: [y: yes, n: no]:

?y

WEIGHT Measurement Movement Area: J1, J2 [0 deg.]; J3 [0 to -50 mm.]; J4 [0 deg.]

Area Movement Check [Low Power Mode] << low-speed operation for the weight measurement motion range

INERTIA Measurement Movement Area: J1 [0 deg]; J2 [90 deg]; J3 [0mm]; J4 [-180 to 180 deg.]

Area Movement Check [Low Power Mode] << low-speed operation for the inertia measurement motion range

ECCENTRICITY Measurement Movement Area: J1 [0 to 90 deg]; J2 [-75 to 90 deg.]; J3 [0mm]; J4 [-360 to 360 deg.]

Area Movement Check [Low Power Mode] << moves the eccentricity measurement motion range at low speed

--------------------------------------------------------

Start of WEIGHT Measurement for SCARA [Static Method]

--------------------------------------------------------

Warm up Movement: (Repeats 10 times)[High Power Mode] << warm-up operation at high speed

Start WEIGHT: J3 (Repeats 5 times)

Measurement 1. << starts the measurement for WEIGHT (five measurements)

Measurement 2.

Measurement 3.

Measurement 4.

Measurement 5.

-----------------------

WEIGHT : 5.1 kg << measured value for the weight

-----------------------

WEIGHT Measurement and Settings Completed.

------------------------------------------------------------

Start of INERTIA Measurement for SCARA [Iteration method]

------------------------------------------------------------

Current Weight: 4.2 kg

Warm up Movement: (Repeats 5 times)[High Power Mode] << warm-up operation

Start Inertia Measurement: J4

Measurement 1. << starts the measurement for the inertia (one to twelve measurements)

Measurement 2.

Measurement 3.

Measurement 4.

Measurement 5.

Measurement 6.

-----------------------

INERTIA : 0.07 kg*m2 << measured value for the inertia

-----------------------

INERTIA Measurement and Settings Completed.

-----------------------------------------------------------------

Start of ECCENTRICITY Measurement for SCARA [Iteration Method]

-----------------------------------------------------------------

Current weight : 5.1 kg, Current inertia : 0.07kgm2

Warm up Movement: (4 movements x 1 set)[High Power Mode] << warm-up operation at high speed

Start ECCENTRICITY Measurement: J1-J4

Measurement 1. << starts the measurement for the eccentricity (one to thirteen measurements)

Measurement 2.

Measurement 3.

Measurement 4.

Measurement 5.

-----------------------

ECCENTRICITY : 90 mm << ends the measurement and sets the value

-----------------------

ECCENTRICITY Measurement and Settings Completed.

----------------------------------------------------------------

WEIGHT : 5.1 kg, INERTIA : 0.07 kg*m2, ECCENTRICITY : 90 mm

----------------------------------------------------------------

motor off

2022/9/7  10:57:54

------------- COMPLETE -----------------

An Iteration method example of the measurement for the SCARA robot WEIGHT (LS6-B, combination of measurement: Static & Iteration Iteration only)

The measurement for Inertia and eccentricity is omitted because it is the same operation as the GX8 example above.

-----------------------------------------------------------

Start of WEIGHT Measurement for SCARA [Iteration Method]

-----------------------------------------------------------

Warm up Movement: (Repeats 6 times)[High Power Mode] << warm-up operation at high speed

Start WEIGHT Measurement: J2

Measurement 1. << starts the measurement for WEIGHT (one to thirteen measurements)

Measurement 2.

Measurement 3.

Measurement 4.

Measurement 5.

Measurement 6.

-----------------------

WEIGHT : 1 kg << ends the measurement and sets the value

-----------------------

WEIGHT Measurement and Settings Completed.

Precautions

-       For the 6-axis robot, this function measures the tip weight of Arm 6. For the SCARA robot, it measures the weight attached to the shaft. For the weight of a workpiece, measure by attaching an equivalent object or set by adding the weight separately. The weight attached to the 6-axis arm 3 or 5 and the SCARA arm 2 should be converted to equivalent weight and added separately.

-       The weight set value and the inertia set value have the minimum value (about 10% to 20% of the maximum value). 0kg, 0kgm2, Values close to these are not set. Light end effectors less the minimum value are rounded up to the minimum value. When operating with the simulator, the minimum value is set.

-       It is recommended to use CollisionDetect with the default "ON". You can use the CollisionDetect command to check the current setting.

> CollisionDetect

ON,ON,ON,ON (always OFF in the simulator)

-       The settings for this measurement are as follows:

performmode: 0  (normal)

accel: 100

Use this setting with the upper limit of performmode "Normal" and accel "100". If you use performmode other than "Normal", change the mode of this measurement as well. When changing, modify the following Gperformmode variables manually and rebuild it before executing it.

"Function main

GPerformMode = 0 '0:normal, 1:boost, 2:low vibration

main2

Fend"

-       If you use other than "0" with a robot not compatible with the perform mode, the following message will appear, and exits.

PerfomMode 1 is not supported in this robot.

-- end --"

-       This measurement result can be used to set the same model uses the same end effector. It cannot be used for setting to different models (even if the arm length is different). Repeat the measurement with the compatible model.

-       If an error occurs in the middle of the program, force-quit the program, eliminate the cause (overload of the end effector, collision of the robot, etc.), and run it again.

-       The following warning message may be output at each measurement and after all measurements.

"Warning: XXXXX over specification, please check the endeffector."(XXXXX is Weight, Inertia, Offset, and Eccentricity)

The measured value is too large for the parameter. This measurement program ends after setting the maximum value, but check the design to make sure that there is no problem with the end effector specification.

-       For not compatible model, the following message appears and the measurement is quit.

N2-A450SR is not supported.

-- end --"

-       For the 6-axis wall mounting type, the following message appears and exits.

Wall mounted type manipulators are not supported.

C8-A701SW is not supported.

-- end --"

## Description
Weight, Inertia, and Eccentricity / Offset Measurement Utility

Weight, Inertia, and Eccentricity / Offset Measurement Utility

Functional overview

Epson RC+ 8.0 supports "Weight, Inertia, and Eccentricity/Offset Measurement Utility."

It is a function measures and sets the following three parameters with the customer's end effector attached to the robot.

Load weight: Specify with the weight command

Weight inertia: Specify with the inertia command

Eccentricity (offset of weight center of gravity from J6 flange surface for the 6-axis robot)

Measurement methods and compatible models

Two methods to measure:

Static (measured at low speed)

Measures and calculates the parameter value as accurately as possible (errors can occur).

Iteration (measured at high speed)

Sets the target parameter value to use the motor torque appropriately, not to measure the exact value. In particular, for large weight, large inertia, and eccentric end effectors, places importance on setting appropriate values that do not break the robot and are well balanced with speed.

The combination of Static and iteration measurements is determined by the robot model. Table 1 and 2 describe it.

Table 1: Measurement methods and compatible models for the 6-axis robot (Static & iteration)

Measurement
		 posture (angle for each axis), motion area (motion range angle
		 for each axis)

Measurement

## Examples
```spel
Start Measurement: [y: yes, n: no]:
```

```spel
?
```

```spel
Current Weight: 1 kg, Current Inertia: 0.016 kgm2, Current Eccentricity: 0 mm.
```

```spel
Current Weight: 1 kg, Current Inertia: 0.03 kgm2, Current Offset: 0 mm.
```

```spel
Weight,Inertia,Offset/Eccentricity Measurement Utility  ver. 1.0.0. << version display
2022/9/7  10:39:52
Model: C8-A701S, PerformMode  0
Max Weight: 8 kg, Max Inertia: 0.15 kgm2, Max Offset: 300 mm.
Current Weight: 1 kg, Current Inertia: 0.03 kgm2, Current Offset: 0 mm. <<current set value
ROBOT MOVEMENT AREA
WEIGHT,OFFSET Measurement Movement Area: J1, J2, J4, J6 [0 deg.]; J3, J5 [-3 to 3 deg.]
INERTIA Measurement Movement Area: J1, J2, J3, J4, J5 [0 deg.]; J6 [270 to -360 deg.]
Start Measurement: [y: yes, n: no]:
?y << check for the start of the measurement
WEIGHT,OFFSET Measurement Movement Area: J1, J2, J4, J6 [0 deg.]; J3, J5 [-3 to 3 deg.]
Area Movement Check [Low Power Mode] << low-speed operation for the weight and the offset measurement motion range
INERTIA Measurement Movement Area: J1, J2, J3, J4, J5 [0 deg.]; J6 [270 to -360 deg.]
Area Movement Check [Low Power Mode] << low-speed operation for the inertia measurement motion range
---------------------------------------------------------------
Start of WEIGHT,OFFSET Measurement for 6axis [Static Method]
---------------------------------------------------------------
Warm up Movement: J3, J5 (Repeats 10 times)[High Power Mode] << warm-up operation
Start Measurement J3, J5 (Repeats 6 times)
Measurement 1. << starts measurements for the weight and offset (six measurements)
Measurement 2.
Measurement 3.
Measurement 4.
Measurement 5.
Measurement 6.
---------------------------------------
WEIGHT 5.7 kg, OFFSET 35 mm  << the measurements and set values for the weight and the offset
---------------------------------------
WEIGHT,OFFSET Measurement and Settings Completed.
------------------------------------------------------------
Start of INERTIA Measurement for 6axis [Iteration Method]
------------------------------------------------------------
Current weight : 5.7 kg, Current offset : 35 mm
Warm up Movement: J6 (Repeats 5 times)[High Power Mode] << warm-up operation
Start INERTIA Measurement: J6
Measurement 1. << starts the measurement for the inertia (one to twelve measurements)
Measurement 2.
Measurement 3.
-----------------------
INERTIA : 0.13 kg*m2 << measured value for the inertia
-----------------------
INERTIA Measurement and Settings Completed.
-----------------------------------------------------------
WEIGHT : 5.7 kg, INERTIA : 0.13 kg*m2, OFFSET : 35 mm << final result and the set value
-----------------------------------------------------------
motor off
2022/9/7  10:43:19
------------- COMPLETE -----------------
```

```spel
Weight,Inertia,Offset/Eccentricity Measurement Program ver. 1.0.0. << version display
2022/9/7  10:52:40
Model: GX8-A553S, PerformMode  0
Max Weight: 8 kg, Max Inertia: 0.16 kgm2, Max Eccentricity: 150 mm.
Current Weight: 4 kg, Current Inertia: 0.01 kgm2, Current Eccentricity: 0 mm. <<current set value
ROBOT MOVEMENT AREA
WEIGHT Measurement Movement Area: J1, J2 [0 deg.]; J3 [0 to -50 mm.]; J4 [0 deg.]
INERTIA Measurement Movement Area: J1 [0 deg]; J2 [90 deg]; J3 [0mm]; J4 [-180 to 180 deg.]
ECCENTRICITY Measurement Movement Area: J1 [0 to 90 deg]; J2 [-75 to 90 deg.]; J3 [0mm]; J4 [-360 to 360 deg.]
Start Measurement: [y: yes, n: no]:
?y
WEIGHT Measurement Movement Area: J1, J2 [0 deg.]; J3 [0 to -50 mm.]; J4 [0 deg.]
Area Movement Check [Low Power Mode] << low-speed operation for the weight measurement motion range
INERTIA Measurement Movement Area: J1 [0 deg]; J2 [90 deg]; J3 [0mm]; J4 [-180 to 180 deg.]
Area Movement Check [Low Power Mode] << low-speed operation for the inertia measurement motion range
ECCENTRICITY Measurement Movement Area: J1 [0 to 90 deg]; J2 [-75 to 90 deg.]; J3 [0mm]; J4 [-360 to 360 deg.]
Area Movement Check [Low Power Mode] << moves the eccentricity measurement motion range at low speed
--------------------------------------------------------
Start of WEIGHT Measurement for SCARA [Static Method]
--------------------------------------------------------
Warm up Movement: (Repeats 10 times)[High Power Mode] << warm-up operation at high speed
Start WEIGHT: J3 (Repeats 5 times)
Measurement 1. << starts the measurement for WEIGHT (five measurements)
Measurement 2.
Measurement 3.
Measurement 4.
Measurement 5.
-----------------------
WEIGHT : 5.1 kg << measured value for the weight
-----------------------
WEIGHT Measurement and Settings Completed.
------------------------------------------------------------
Start of INERTIA Measurement for SCARA [Iteration method]
------------------------------------------------------------
Current Weight: 4.2 kg
Warm up Movement: (Repeats 5 times)[High Power Mode] << warm-up operation
Start Inertia Measurement: J4
Measurement 1. << starts the measurement for the inertia (one to twelve measurements)
Measurement 2.
Measurement 3.
Measurement 4.
Measurement 5.
Measurement 6.
-----------------------
INERTIA : 0.07 kg*m2 << measured value for the inertia
-----------------------
INERTIA Measurement and Settings Completed.
-----------------------------------------------------------------
Start of ECCENTRICITY Measurement for SCARA [Iteration Method]
-----------------------------------------------------------------
Current weight : 5.1 kg, Current inertia : 0.07kgm2
Warm up Movement: (4 movements x 1 set)[High Power Mode] << warm-up operation at high speed
Start ECCENTRICITY Measurement: J1-J4
Measurement 1. << starts the measurement for the eccentricity (one to thirteen measurements)
Measurement 2.
Measurement 3.
Measurement 4.
Measurement 5.
-----------------------
ECCENTRICITY : 90 mm << ends the measurement and sets the value
-----------------------
ECCENTRICITY Measurement and Settings Completed.
----------------------------------------------------------------
WEIGHT : 5.1 kg, INERTIA : 0.07 kg*m2, ECCENTRICITY : 90 mm
----------------------------------------------------------------
motor off
2022/9/7  10:57:54
------------- COMPLETE -----------------
```

```spel
-----------------------------------------------------------
Start of WEIGHT Measurement for SCARA [Iteration Method]
-----------------------------------------------------------
Warm up Movement: (Repeats 6 times)[High Power Mode] << warm-up operation at high speed
Start WEIGHT Measurement: J2
Measurement 1. << starts the measurement for WEIGHT (one to thirteen measurements)
Measurement 2.
Measurement 3.
Measurement 4.
Measurement 5.
Measurement 6.
-----------------------
WEIGHT : 1 kg << ends the measurement and sets the value
-----------------------
WEIGHT Measurement and Settings Completed.
```

```spel
> CollisionDetect
```

```spel
ON,ON,ON,ON (always OFF in the simulator)
```

```spel
"Function main
```

```spel
GPerformMode = 0 '0:normal, 1:boost, 2:low vibration
```

```spel
main2
```

```spel
Fend"
```

```spel
PerfomMode 1 is not supported in this robot.
-- end --"
```

```spel
"Warning: XXXXX over specification, please check the endeffector."(XXXXX is Weight, Inertia, Offset, and Eccentricity)
```

```spel
Wall mounted type manipulators are not supported.
```

```spel
C8-A701SW is not supported.
```

```spel
-- end --"
```


---

# Welcome to Epson RC+ 8.0
**Type:** reference | **Section:** Operator

## Description
Welcome to Epson RC+ 8.0

Epson RC+ 8.0

Operator

Version 8.0.0

The Operator Window

Robot Manager

I/O Monitor Window

I/O Label Editor

System History


---

# Where Statement
**Type:** statement | **Section:** Operator

## Syntax
```
Where [LocalNumber]
```

## Parameters
LocalNumber	Optional.  Specifies the local coordinate system number.  Local 0 is default.

## Description
Where Statement

Where Statement

## Examples
```spel
>where
```

```spel
WORLD:  X: 350.000 mm  Y:    0.000 mm  Z:    0.000 mm  U:    0.000 deg V: 0.000 deg W: 0.000 deg
```

```spel
JOINT:  1:
    0.000 deg 2:    0.000 deg 3:    0.000 mm  4:    0.000 deg
```

```spel
PULSE:  1:
        0 pls 2:        0 pls 3:        0 pls 4:        0 pls
```

```spel
> local 1, 100,100,0,0
```

```spel
> where 1
```

```spel
WORLD1: X:  250.000 mm  Y: -100.000 mm  Z:    0.000 mm  U:    0.000 deg V: 0.000 deg W: 0.000 deg
```

```spel
JOINT:  1:
    0.000 deg 2:    0.000 deg 3:    0.000 mm  4:    0.000 deg
```

```spel
PULSE:  1:
        0 pls 2:        0 pls 3:        0 pls 4:        0 pls
```

## See Also
Displays current robot position data.

Joint

Plist

Pulse

Where Statement Example

The display type can be different depending on the robot type and existence of additional axes.
The following example is for Scara robot without the additional axis.

>where

WORLD:  X:
  350.000 mm  Y:    0.000 mm  Z:    0.000 mm  U:    0.000 deg V: 0.000 deg W: 0.000 deg

JOINT:  1:
    0.000 deg 2:    0.000 deg 3:    0.000 mm  4:    0.000 deg

PULSE:  1:
        0 pls 2:        0 pls 3:        0 pls 4:        0 pls

> local 1, 100,100,0,0

> where 1

WORLD1: X:  250.000 mm  Y: -100.000 mm  Z:    0.000 mm  U:    0.000 deg V: 0.000 deg W: 0.000 deg

JOINT:  1:
    0.000 deg 2:    0.000 deg 3:    0.000 mm  4:    0.000 deg

PULSE:  1:
        0 pls 2:        0 pls 3:        0 pls 4:        0 pls


---

# Working with variables
**Type:** reference | **Section:** Operator

## Description
Working with variables

Working with variables

Variable scopes

SPEL+ has variables with different scopes:

Local

Module

Global

Local variables

Local variables are available to enabled statements in the same function. Functions using local variable names cannot refer to the same local variables in other functions. This is why they are called locals, because they are local to the function they are being used in.

To declare local variables in a function, use one of the variable declaration instructions at the beginning of the function after the Function statement:

Boolean, Byte, UByte, Integer, Short, UShort, Long, Int32, UInt32, Int64, UInt64, Real, Double, String

For example, the following function declares several local variables:

Function test

Integer intVar1, intVar2

Real realVar

String dataStr$

Integer array(10)

Fend

Module variables

Module variables are available to all functions in the same program file.

To declare module variables in a program, use one of the variable declaration instructions at the beginning of the program before any Function statements:

Boolean, Byte, UByte, Integer, Short, UShort, Long, Int32, UInt32, Int64, UInt64, Real, Double, String

TIP :  In order to indicate that a variable is module level, precede the name with "m_", as shown in the example below. With this, you can improve the program readability.

For example, the following function declares several module level variables:

' Module level vars, used by all functions in this file

Integer m_IntVar1, m_IntVar2

Real m_RealVar

String m_DataStr$

Integer m_Array(10)

Function main

    m_IntVar1 = 25

    Call test

Fend

Function test

    Print m_IntVar1

Fend

Global variables

Global variables can be shared between all functions in a project. The Global instruction is used to declare a global variable.

To declare global variables in a program, use the Global instruction with the desired variable type (Boolean, Byte, UByte, Integer, Short, UShort, Long, Int32, UInt32, Int64, UInt64, Real, Double, String) at the beginning of the program before any Function statements:

Boolean, Byte, UByte, Integer, Short, UShort, Long, Int32, UInt32, Int64, UInt64, Real, Double, String

For details, see Data Types.

NOTE:  To indicate that variables are global, precede the name with "g_" as shown in the example below. With this, you can improve the program readability.

Program: MAIN.PRG

Global Integer g_TotalCycles

Function main

    Call LoadPart

    ...

    ...

Fend

Program: LOADPART.PRG

Function LoadPart

    Jump pick

    On gripper

    Wait .1

    Jump place

    Off gripper

    Wait .1

    g_TotalCycles = g_TotalCycles + 1

Fend

Global Preserve variables

You can preserve global variable values by using the optional Preserve parameter when you declare global variables.

Preserved variables are stored in the controller's SRAM.

If the data type of a preserved variable or the number of dimensions is changed, the variable values will be cleared.

NOTE:  Be careful about the backup battery power, because you will lose the data of global preserve variables stored in SRAM if the battery is weak.

Arrays

You can declare local, module, and global variables with up to three dimensions as arrays for all data types.

To declare an array, use this syntax:

dataType name ( ubound1 [ , ubound2 [ , ubound3] ] )

SPEL+ arrays are zero based. The first element is referenced with a value of zero.

The total available number of array elements for local variables is 200 for strings and 2000 for all other types.

The total available number of array elements for global preserve variables is 400 for strings and 4000 for all other types.

The total available number of array elements for global and module variables is 10,000 for strings and 100,000 for all other types.

To calculate the total elements used in an array, use the following formula.

(If a dimension is not used, substitute 0 for the ubound values.)

total elements = (ubound1 + 1) * (ubound2 + 1) * (ubound3 + 1)

Array declaration examples:

' Global string array

Global String gData$(10)

Function main

' Arrays local to this function

Integer intArray(10)

Real coords(20, 10)

Use Redim to change the bounds of an array at run time.

Integer a(10)

Redim a(20)

To preserve values when using Redim, add the Preserve optional argument.

Integer a(10)

Redim Preserve a(20)

Use UBound to get the maximum element number.

Integer i, a(10)

For i = 1 to UBound(a)

a(i) = i

Next i

Initial values

All variables are initialized when first used except for Global Preserve variables. Strings are set to empty, and all other variables are set to zero.

Clearing arrays

Execute Redim (without Preserve) to clear all of the elements of array variables.

## Examples
```spel
' Module level vars, used by all functions in this file
Integer m_IntVar1, m_IntVar2
Real m_RealVar
String m_DataStr$
Integer m_Array(10)
Function main
    m_IntVar1 = 25
    Call test
Fend
```

```spel
Function test
    Print m_IntVar1
Fend
```

```spel
Global Integer g_TotalCycles
```

```spel
Function main
    Call LoadPart
    ...
    ...
Fend
```

```spel
Function LoadPart
    Jump pick
    On gripper
    Wait .1
    Jump place
    Off gripper
    Wait .1
    g_TotalCycles = g_TotalCycles + 1
Fend
```

```spel
' Global string array
```

```spel
Global String gData$(10)
Function main
' Arrays local to this function
Integer intArray(10)
Real coords(20, 10)
```

```spel
Integer a(10)
Redim a(20)
```

```spel
Integer a(10)
Redim Preserve a(20)
```

```spel
Integer i, a(10)
For i = 1 to UBound(a)
a(i) = i
Next i
```


---

# Wrist Function
**Type:** function | **Section:** Operator

## Syntax
```
Wrist [(point)]
```

## Parameters
point	Optional.
		  P number
		 or P(expr)
		 or point label or point expression.  If point is omitted,
		 then the wrist orientation of the current robot position is returned.

## Description
Wrist Function

Wrist Function

See_Also

## Examples
```spel
Print Wrist(pick)
Print Wrist(P1)
Print Wrist
Print Wrist(P1 + P2)
```

## See Also
Elbow, Hand, J4Flag, J6Flag, Wrist Statement

Wrist Function Example

Print Wrist(pick)

Print Wrist(P1)

Print Wrist

Print Wrist(P1 + P2)


---

# Wrist Keyword
**Type:** reference | **Section:** Operator

## Description
Wrist Keyword

Wrist Keyword

The Wrist keyword is used in these contexts:

Wrist Statement

Wrist Function


---

# Wrist Statement
**Type:** statement | **Section:** Operator

## Syntax
```
(1) Wrist
			point, [Flip | NoFlip ]

(2) Wrist
```

## Parameters
point	P
						number or P(expr) or point label.

Flip | NoFlip	Representing wrist orientation.

## Description
Wrist Statement

Wrist Statement

## Examples
```spel
Wrist P0, Flip

			Wrist P(mypoint), NoFlip

P1 = 320.000, 400.000, 350.000, 140.000, 0.000, 150.000
```

## See Also
Elbow, Hand, J4Flag, J6Flag, Wrist Function

Wrist Statement Example

Wrist P0, Flip

Wrist P(mypoint), NoFlip

P1 = 320.000, 400.000, 350.000, 140.000, 0.000, 150.000


---

# Write Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Write #portNumber, string
```

## Parameters
portNumber	ID number that specifies the file or communications port

File number can be specified in ROpen, WOpen, AOpen statements.

Communication port number can be specified in OpenCom (RS-232C) or OpenNet (TCP/IP) statements.

string	String expression that will be written to the file.

## Description
Write is different from Print in that it does not add an end of line terminator.

Note: File write buffering

File writing is buffered. The buffered data can be written with Flush statement. Also, when closing a file with Close statement, the buffered data can be written.

## Examples
```spel
OpenCom #1
For i=1 to 10 Write #1, data$(i)
Next i
CloseCom #1
```

## See Also
Print

Read

WriteBin

Write Statement Example

OpenCom #1

For i=1 to 10

  Write #1, data$(i)

Next i

CloseCom #1


---

# WriteBin Statement
**Type:** reference | **Section:** Operator

## Syntax
```
WriteBin #portNumber, data

WriteBin #portNumber, array(), count
```

## Parameters
portNumber	ID number that specifies the file or communications port

File number can be specified in BOpen statements.

Communication port number can be specified in OpenCom (RS-232C) or OpenNet (TCP/IP) statements.

data	Integer expression containing the data to be written.

array()	Name of a byte, integer, or long array variable that contains the data bytes to be written.  Specify a one dimension array variable.

count	Specifies the number of bytes to be written and must be less than or equal to the number of array elements.

## Description
WriteBin Statement

WriteBin Statement

Writes binary data to a file or communications port.

## Examples
```spel
OpenCom #1
		For i = 0 To 100

			  WriteBin #1, i
		Next i
		WriteBin #1, data(), 100
		CloseCom #1
```

## See Also
ReadBin, Write

WriteBin Statement Example

OpenCom #1

		For i = 0 To 100

WriteBin #1, i

		Next i

		WriteBin #1, data(), 100

		CloseCom #1


---

# XY Function
**Type:** reference | **Section:** Operator

## Syntax
```
XY( x, y, z, u, [v, w])
```

## Parameters
x	Real expression representing the X coordinate.

y	Real expression representing the Y coordinate.

z	Real expression representing the Z coordinate.

u	Real expression representing the U coordinate.

v	Optional for 6-Axis robots (including
		 N series).  Real expression representing the V coordinate.

w	Optional for 6-Axis robots (including
		 N series).  Real expression representing the W coordinate.

## Description
When you don't use the additional ST axis, there are nothing in particular to be care of.

You can move the manipulator to the specified coordinate with XY function like below:

   Go XY(60,30,-50,45)

When you use the additional ST axis, you need to be careful.

XY function returns the only robot point data, not including the additional axis.

If you use XY function lick this: Go XY(60,30,-50,45), the manipulator will move to the specified coordinate but the additional axis will not move.  If you want to move the additional axis as well, specify like this: Go XY(60,30,-50,45) : ST( 10,20).

For the details of additional axis, refer to Epson RC+ Users Guide: 21. Additional Axis.

## Examples
```spel
P10 = XY(60, 30, -50, 45) + P20
```

## See Also
JA

Point Expression

ST Function

XY Function Example

P10 = XY(60, 30, -50, 45) + P20


---

# XYLim Function
**Type:** function | **Section:** Operator

## Syntax
```
XYLim(limit)
```

## Parameters
limit	Integer expression that specifies which limit to return.

1: Lower limit.

2: Upper limit.

## Description
XYLim Function

XYLim Function

See_Also Example

Returns point data for either upper or lower limit of XYLim region.

## Examples
```spel
P1 = XYLim(1)
P2 = XYLim(2)
```

## See Also
XYLim Statement

XYLim Function Example

P1 = XYLim(1)

P2 = XYLim(2)


---

# XYLim Keyword
**Type:** reference | **Section:** Operator

## Description
XYLim Keyword

XYLim Keyword

The XYLim keyword is used in these contexts:

XYLim Statement

XYLim Function


---

# XYLim Statement
**Type:** statement | **Section:** Operator

## Syntax
```
XYLim minX, maxX, minY, maxY, [minZ], [maxZ]

XYLim
```

## Parameters
minX	The minimum
		 X coordinate position to which the manipulator may travel. (The
		 manipulator may not move to a position with the X Coordinate less
		 than minX.)

maxX	The maximum
		 X coordinate position to which the manipulator may travel. (The
		 manipulator may not move to a position with the X Coordinate greater
		 than maxX.)

minY	The minimum
		 Y coordinate position to which the manipulator may travel. (The
		 manipulator may not move to a position with the Y Coordinate less
		 than minY.)

maxY	The maximum
		 Y coordinate position to which the manipulator may travel. (The
		 manipulator may not move to a position with the Y Coordinate greater
		 than maxY.)

minZ	Optional.
		  The minimum Z coordinate position to which the manipulator
		 may travel. (The manipulator may not move to a position with the
		 Z Coordinate less than minZ.)

maxZ	Optional.
		  The maximum Z coordinate position to which the manipulator
		 may travel. (The manipulator may not move to a position with the
		 Z Coordinate greater than maxZ.)

Result

Displays current XYLim values when used without parameters.

## Description
The motion range established with XYLim values applies to monitor method configured in XYLimMode command. For details of monitor method, refer to XYLimMode statement.

Robot parameter data is stored in compact flash in controller.  Therefore, writing to command flash occurs when executing this command.  Frequent writing to compact flash affect to lifetime of compact flash.  We recommend to use this command minimally.

## Notes
Turning Off Motion Range Limit Checking

There are many applications which don't require Motion Range limit checking and for that reason there is a simple method to turn this limit checking off. To turn motion range limit checking off, define the Motion Range Limit values for minX, maxX, minY, and maxY to be 0. For example XYLim 0, 0, 0, 0.

Default Motion Range Limit Values

The default values for the XYLim instruction are "0, 0, 0, 0". (Motion Range Limit Checking is turned off.)

Tip

Point & Click Setup for XYLim

Epson RC+ has a point and click dialog box for defining the motion range limits. The simplest method to set the XYLim values is by using the XYZ Limits page on the Robot Manager.

## Examples
```spel
> xylim -200, 300, 0, 500

> xyLim
-200.000, 300.000, 0.000, 500.000
```

## See Also
XYZ Limits page: Robot Manager

Range

XYLimMode

XYLim Statement


---

# XYLimMode Statement
**Type:** statement | **Section:** Operator

## Syntax
```
(1) XYLimMode
  monitor method

(2) XYLimMode
```

## Parameters
monitor
		 method	Integer expression
		 represents monitor method of using XYLim.

Constant	Value	Description

XYLIM_STANDARD	0	Applies XYLim to endpoint of motion
		 command. (There is no effect on Pulse.)

XYLIM_STRICT	1	Applies XYLim to monitor method of
		 XYLIM_STANDARD, trajectory, and pulse motion.

Result

Displays monitor method of XYLim that currently configured when used without parameters.

## Description
XYLimMode sets monitor method of XYLim for spcified robot.

When XYLIM_STANDARD is specified, the motion range set in XYLim is effective only for endpoint of motion command. From start point of motion to trajectory of endpoint is not applicable. Therefore, during operation, the arm may pass outside of the area that set in XYLim. In this mode, XYLim is not applied to pulse motion.

When XYLIM_STRICT is specified, the motion range set in XYLim is applied to endpoint of motion command and start point of motion to trajectory of endpoint. Therefore, during operation, if the arm tried to move out of the range set in the XYLim, an error will occur. In this mode, XYLim is applied to pulse motion. However, moving from outside the XYLim range to within the range, such as "the start point is outside the XYLim range and the endpoint is within the XYLim range", it is possible to move without an outside XYLim range error.

To prevent robot interferes other devices, using with XYLIM_STRICT is recommended.

It is possible to change settings of default value of monitoring method when Controller start up, in the Controller preferences of Epson RC+. The value confihured in XYLimMode command is enabled until Controller restart. When restarted Controller, the monitoring method of XYLim will be reset to the method specified in the Controller preferences.

Caution:
  For XYLIM_STANDARD, the arm may pass outside of the area that set in XYLim. Therefore, note that the robot does not interfere other devices. For example, setting extra space to XYLim and actual obstacle, operating near XYLim area, check trajectory at low speed.

Potential Errors:

When executed PTP near XYLim area.

When executing PTP motion such as Go motion, start point and endpoint moves like the arrow of image on the left. Therefore, in XYLIM_STRICT, target coordinate is in the range but trajectory is out of range so an error will occur. In this case, avoid it so that the motion trajectory does not exceed XYLim by adding midPoint between start point and target coordinate like following image on the right.

When using past project:

If a project used with Controller FW Ver 7.5.2.0 or earlier than 7.5.52.0 is applied to a Controller that XYLim monitoring method is XYLIM_STRICT, the trajectory may become an out-of-range error. In this case, change the program to not exceed XYLim by adding midpoint.

## Examples
```spel
Function XYLimMode_sample Motor On XYLimMode XYLIM_STANDARD Go P1 'Applying XYLim only for endpoint. XYLimMode XYLIM_STRICT Go P2 'Applying XYLim to endpoint and trajectory.
Fend
```

```spel
> XYLimMode
1
```

## See Also
Sets or displays monitor method of XYLim.

XYLim

XYLimMode CommandExample

This example uses XYLimMode. Moving current point to P1 with XYLIM_STANDARD and moving P1 to P2 with XYLIM_STRICT.

Function XYLimMode_sample
 Motor On
 XYLimMode XYLIM_STANDARD
 Go P1 'Applying XYLim only for endpoint.
 XYLimMode XYLIM_STRICT
 Go P2 'Applying XYLim to endpoint and trajectory.

Fend

This is an example using XYLimMode in command window. Displays current monitor method of XYLim.

> XYLimMode

1


---

# XYZ Limits page: Robot Manager Window
**Type:** reference | **Section:** Operator

## Description
XYZ Limits page: Robot Manager Window

[Tools]-[Robot Manager]-[XYZ Limits] Page

This page allows you to configure limits for X, Y and Z motion in the robot envelope.

For more details on XYZ limits, refer to the following manual:

SPEL+ Language Reference - XYLim Statement

NOTE:  When using Safety Function (the Controller with Safety Board), the Safety Limited Position (SLP) of the Safety Function can be used.

Set them using the Safety Function Manager. For more details, refer to the following manual:

Robot Controller Safety Function Manual 4.3.4 Setting Safety Limited Position (SLP)

Item	Description

Read
		 Current	Click
		 this button to read the value from the current robot position.

		The button text shows the axis and minimum or maximum depending
		 on which text field has the current focus.

Apply	Sets
		 the current values.

Restore	Reverts
		 to the previous values.

Defaults	Reverts
		 back to the default settings.


---

# Xor Operator
**Type:** reference | **Section:** Operator

## Syntax
```
result = expr1  Xor  expr2
```

## Parameters
expr1, expr2	A numeric value, or a variable name.

r
						esult	An integer.

## Description
The Xor operator performs the bitwise Xor operation on the values of the operands. Each bit of the result is the Xored value of the corresponding bits of the two operands.

If bit in expr1 is	And bit in expr2 is	The result is

0	0	0

0	1	1

1	0	1

1	1	0

## Examples
```spel
>print 2 Xor 6

4

>
```

## See Also
And

LShift

Not

Or

RShift

Xor Example

>print 2 Xor 6

4

>


---

# Xqt Statement
**Type:** reference | **Section:** Operator

## Syntax
```
Xqt [taskNumber,] funcName [( argList ), [,Normal | NoPause | NoEmgAbort ]]
```

## Parameters
taskNumber	Optional. The task number for the task
		 to be executed. The range of the task number is 1 to 32.

For background tasks, specifies integer
		 value from 65 ~ 80.

funcName	The name of
		 the function to be executed.

argList	Optional.
		 List of arguments that are passed to the function procedure when
		 it is called.  Multiple arguments are separated by commas.

taskType	Optional.
		 Usually omitted.

For background
		 tasks, specifying a task type means nothing.

Normal	Executes a
		 normal task.

NoPause	Executes a
		 task that does not pause at Pause statement or Pause input signal
		 occurance or Safety Door Open.

NoEmgAbort	Executes a
		 task that continues processing at Emergency Stop or error occurence.

## Description
Xqt starts the specified function and returns immediately.

Normally, the taskNumber parameter is not required.
  When taskNumber is omitted, SPEL automatically assigns a task number to the function, so you don't have to keep track of which task numbers are in use.

## Notes
Task Type

Speciify NoPause or NoEmgAbort as a task type to execute a task that monitors the whole controller. However, be sure to use these special tasks based on the understanding of the task motion using SPEL+ or restriction of special tasks.

For details of special tasks, refer to the section Special Tasks in the Epson RC+ User's Guide.

Background task

When executing Xqt in a background task, the generated task is also the background task. To execute the main function from a background task, use the StartMain statement. The details of the background task is explained in the Epson RC+ Users Guide manual: 6.20 Special Task.

Unavailable Commands in NoEmgAbort Task and background task

The following commands cannot be executed in NoEmgAbort task and background task.

A	Accel		Cnv_Trigger		Plane		VDefArm

AccelR		Cnv_UpStream		PlaneClr		VDefGetMotionRange

AccelS		CollisionDetect		Power		VDefLocal

AIO_TrackingStart		CP		PTPBoost		VDefSetMotionRange

AIO_TrackingEnd		CP_Offset		Pulse		VDefTool

Arc		Curve	Q	QP		VDeleteCalibration

Arc3		CVMove		QPDecelR		VDeleteObject

Arch	E	ECP		QPDecelS		VDeleteSeuence

Arm		ECPClr	R	Range		VEditWindow

ArmCalib		ECPSet		Reset
		 *1		VGet

ArmCalibCLR	F	Find		Restart
		 *2		VGoCenter

ArmCalibSET		Fine	S	Sense		VLoad

ArmClr		FineDist		SetLatch		VLoadModel

ArmSet	G	Go		SFree		VRun

AutoLJM	H	Hand_On		SF_LimitSpeedS		VSave

AutoOrientationFlag		Hand_Off		SF_LimitSpeedSEnable		VSaveImage

AvoidSingularity		Home		SF_RealSpeedS		VSaveModel

B	Base		HomeClr		SingularityAngle		VSet

BGo		HomeSet		SingularityDist		VShowModel

BMove		Hordr		SingularitySpeed		VStasShow

Box	I	Inertia		SLock		VStatsReset

BoxClr	J	JTran		SoftCP		VStatsResetAll

Brake		Jump		Speed		VStatsSave

C	Calib		Jump3		SpeedFactor		VSD

Cnv_AbortTrack		Jump3CP		SpeedR		VStatsShow

Cnv_Accel		JRange		SpeedS		VTeach

Cnv_AccelLim	L	LatchEnable		SyncRobots		VTrain

Cnv_Adjust		LimitTorque	T	TC	W	WaitPos

Cnv_AdjustClear		LimZ		TGo		Weight

Cnv_AdjustGet		LimZMargin		Till		WorkQue_Add

Cnv_AdjustSet		Local		TLSet		WorkQue_Reject

Cnv_DownStream		LocalClr		TLClr		WorkQue_Remove

Cnv_Fine	M	MCal		TMove		WorkQue_Sort

Cnv_Mode		MCordr		Tool		WorkQue_UserData

Cnv_OffsetAngle		Motor		Trap	X	Xqt  *3

Cnv_PosErrOffset		Move	V	VCal		XYLim

Cnv_QueAdd	O	OLAccel		VcalPoints

Cnv_QueMove	P	Pass		VCls

Cnv_QueReject		PerformMode		VCreateCalibration

Cnv_QueRemove		Pg_LSpeed		VCreateObject

Cnv_QueUserData		Pg_Scan		VCreateSequence

*1 Reset Error can be executed

*2 Executable from the Trap Error processing task

*3 Executable from the background tasks

DO NOT use XQT command repeatedly in Loop statements.

Do not use XQT command repeatedly in Loop statements such as Do...Loop.

The controller may freeze up. If you use Loop statements repeatedly, make sure to add Wait commad (Wait 0.1).

## Examples
```spel
Function main Xqt flash    'Start flash function as task 2 Xqt Cycle(5) 'Start Cycle function as task 3 Do
    Wait 3 'Execute task 2 for 3 seconds
    Halt flash 'Suspend the task

    Wait 3
    Resume flash 'Resume the task Loop
Fend
```

```spel
Function Cycle(count As Integer) Integer i For i = 1 To count
    Jump pick
    On vac
    Wait .2
    Jump place
    Off vac
    Wait .2 Next i
Fend
```

```spel
Function flash Do
    On 1
    Wait 0.2
    Off 1
    Wait 0.2 Loop
Fend
```

## See Also
Simplest Application

Multitasking

Function/Fend

Halt

Resume

Quit

StartMain

Trap

Xqt Statement Example

Function main

  Xqt flash    'Start flash function as task 2

  Xqt Cycle(5) 'Start Cycle function as task 3

  Do

    Wait 3 'Execute task 2 for 3 seconds

    Halt flash 'Suspend the task

    Wait 3

    Resume flash 'Resume the task

  Loop

Fend

Function Cycle(count As Integer)

  Integer i

  For i = 1 To count

    Jump pick

    On vac

    Wait .2

    Jump place

    Off vac

    Wait .2

  Next i

Fend

Function flash

  Do

    On 1

    Wait 0.2

    Off 1

    Wait 0.2

  Loop

Fend


---

# [Jogging] Group
**Type:** reference | **Section:** Operator

## Description
[Jogging] Group

[Jogging] Group

This group contains controls for setting jog mode, speed, and jog buttons.

Symbol	Item

a	Jog Mode

b	Speed

c	Jog Buttons

Jog Mode

This dropdown list contains the following choices jog mode.

World    Jogs the robot along the X, Y, Z axes in the current local, tool, arm, and ECP.

For robots with 4 DOF (Cartesian coordinate or SCARA), you can also jog U (roll).

For robots with 6 DOF (vertical 6-axis (including N series)), you can jog U (Z axis rotation of the base coordinate system), V (Y axis rotation of the base coordinate system), and W (X axis rotation of the base coordinate system). When the [Jog & Teach] panel is displayed, Jog & Teach is set to "World".

Tool      Jogs the robot in the coordinate system defined by the current tool.

Local     Jogs the robot in the coordinate system defined by the current local.

Joint      Jogs each joint of the robot. A separate set of jog buttons will appear when using joint mode when using non-Cartesian robots.

ECP      Jogs the robot along the axes of the coordinate system defined by the current external control point. Coordinates are World coordinates.

Speed

The speed for jogging and motion commands can be changed by selecting Low or High. When starting RC+, the speed is set to "Low speed" when the [Robot Manager] window is displayed. Jogging is always in low power mode. The speeds and accelerations associated with the jog speed settings are shown below.

SCARA robot RS series

Speed	Jog Method	Speed	Accel	Decel

Low	Continuous
		 World/Tool/ECP XYZ	10 mm/sec	100 mm/sec2	200 mm/sec2

Continuous World/Tool/ECP UVW	2 deg/sec	20 deg/sec2	40 deg/sec2

Continuous Joint	*	10 deg/sec2	20 deg/sec2

Step	1/5 of default PTP speed	Default PTP acceleration	Default PTP deceleration

High	Continuous World/Tool/ECP XYZ	50 mm/sec	100 mm/sec2	200 mm/sec2

Continuous World/Tool/ECP UVW	10 deg/sec	20 deg/sec2	40 deg/sec2

Continuous Joint	*	10 deg/sec2	20 deg/sec2

Step	Default PTP
		 speed	Default PTP
		 acceleration	Default PTP deceleration

* Speed of Continuous Joint depends on the robot model

Vertical 6-axis robot, N series

Speed	Jog
		 Method	Speed	Accel	Decel

Low	Continuous
		 World/Tool/ECP XYZ	10 mm/sec	200 mm/sec2	400 mm/sec2

Continuous World/Tool/ECP UVW	2 deg/sec	20 deg/sec2	40 deg/sec2

Continuous Joint	*	20 deg/sec2	40 deg/sec2

Step	1/5 of default PTP speed	Default PTP acceleration	Default PTP deceleration

High	Continuous World/Tool/ECP XYZ	*	200 mm/sec2	400 mm/sec2

Continuous World/Tool/ECP UVW	15 deg/sec	20 deg/sec2	40 deg/sec2

Continuous Joint	*	20 deg/sec2	40 deg/sec2

Step	Default PTP
		 speed	Default PTP
		 acceleration	Default PTP deceleration

* Speed of Continuous Joint and High speed Continuous XYZ depends on the robot model.

Jog Buttons

Use the jog buttons to jog the robot throughout the work envelope.

They can be controlled only by the mouse.

The robot jogs one step at a time as you click the button in either "Long", "Medium", or "Short" mode of the Jog Distance. The robot jogs continuously by holding the button down. To jog continuously without stepping, set the Jog Distance to Continuous. For details, refer to How to jog robot.

You can change the orientation of the jog buttons to align your PC monitor with the robot from the Epson RC+ 8.0 menu-[Setup]-[Preferences]-[Jog & Teach].

The jog buttons are displayed differently depending on the Jog mode.

For World, Local, Tool, and ECP jogging, the X, Y, Z, U, V, W buttons appear (V and W are only for 6-axis robots (including N series)).

For Joint jogging, the joint buttons labeled J1 - J6 appear.

The X, Y, and Z buttons jog the robot in the Cartesian axis.

The U buttons rotate the Tool coordinate system of the Z axis. (roll)

For 6-axis robots (including N series), the V buttons rotate the Tool coordinate system of the Y axis. (pitch)

The W buttons rotate the Tool coordinate system of the X axis. (yaw)

Local

In the [Local] box, select the local coordinate system for jogging or teaching.

Only Locals that have been defined are shown in the list. When you teach a point, the Local point attribute defaults to the current local number.

Tool

In the [Tool] box, select the tool for jogging or teaching.

Only Tools that have been defined are shown in the list.

Arm

In the [Arm] box, select the arm for jogging or teaching.

Only Arms that have been defined are shown in the list.

NOTE:  Arms are not used with 6-axis robots (including the N series). Arms cannot be change from the [Arm] box with a PG axis.

ECP

In the [ECP] box, select the ECP to perform jog operation.

Only ECPs that have been defined are shown in the list. ECPs are only allowed if the External Control Point option has been activated.

[Current Position] Group

This group displays the current position of the robot. There are three ways to display position.

World: Displays the current position and tool orientation in the selected local coordinate system

Joint: Displays the current joint values

Pulse: Displays the current encoder pulse count for each joint

[Current Arm Orientation] Group

This group displays the current arm orientation.

6-axis robot : Hand orientation, Elbow orientation, wrist orientation,

J1Flag value, J4Flag value, J6Flag value

N               : Hand orientation, Elbow orientation, wrist orientation,

J4Flag value, J6Flag value

RS series    : Hand orientation, J1Flag value, J2Flag value

Others        : Hand orientation

[Jog Distance] Group

There are radio buttons for selecting Continuous, Long, Medium, and Short jog distances.

When "Continuous" is selected, the robot operates in continuous jog mode and the [Jog Distance] box is grayed out and cannot be selected.

If anything other than "Continuous" is selected, the distance specified in the [Jog Distance] box is considered as one step (step mode).

To change a jog distance, first select the distance to be changed, then type in the new value.

Distance	Set
		 Value *	Default
		 Value

Short	0
		 to 10	0.1

Medium	0 to 30	1

Long	More
		 than 0 to 180	10

* If you enter a too large value, an error message appears when you attempt to jog.

When the jog mode is changed, the jog distance units change appropriately between millimeters (mm) and degrees (deg).

NOTE:  When the jog distance is longer than the default, jog distance is reset to default status by rebooting Epson RC+.

[Teach Points] Tab

Select the [Teach] tab.

This tab shows the current point file name and point number.

Use the [Teach] button to register the current robot position.

Use the [Edit] button to select and view the current point in the [Points] tab.

Click the [Save] button to save teach point data.

See How to teach points for more information.

[Execute Motion] Group

Select the [Execute Motion] tab.

This executes motion commands. You can execute commands such as Go, Move, Jump, Arc, Home, and Align (6-axis robots only).

Click the [Execute] button from this group to execute the motion.

When [USE LJM (Least Joint Motion)] checkbox is checked, posture of the manipulator is automatically adjusted to reduce the motion distance.

The default setting is unchecked.

In the Epson RC+ 8.0 menu, clear the [Setup]-[Preferences]-[Jog & Teach]-[Enable motion commands] checkbox to disable motion command execution.

[Free Joints] Group

You can free one or more joints using the checkboxes. PG axis not available for 6-axis robots (including the N series).

Click the [Free All] button to free all joints from the servo control.

Click the [Lock All] button to lock all joints under the servo control.

[Hands] group

When hands are set, the [Hands] tab is displayed.

Item	Description

Hand:	Select the
		 hand to operate from pull-down menu.

		In the pull-down menu, the registered hands are displayed for the
		 robot selected in [Robot:] on the upper left of the [Robot Manager]
		 window.

Display	Meaning

The
				 return value of Hand_On function is True

The
				 return value of Hand_On function is False

The
				 return value of Hand_On function is False

Display	Meaning

The return value of Hand_Off
				 function is True

The return value of Hand_Off
				 function is False

The return value of Hand_Off
				 function is False

For details of hand settings, refer to "Hand Function Manual".


---

# [Tools]-[Robot Manager]-[Boxes] Page
**Type:** reference | **Section:** Operator

## Description
[Tools]-[Robot Manager]-[Boxes] Page

[Tools]-[Robot Manager]-[Boxes] Page

This page allows you to define Box (approach check area) settings for a robot. When the page is selected, the current values are displayed. When a Box is undefined, then all fields for that Box will be blank. When you enter a value in any of the fields for an undefined Box setting, then the remaining fields will be set to zero. The Box will be defined when you press the [Apply] button.

For more details on Box Page settings, refer to the following manual:

SPEL+ Language Reference - Box Statement

Navigating the grid

Press the [Tab] key to move to the next cell. Press the [Shift] + [Tab] key to move to the previous cell. Press the arrow [↑] or [↓] key to move to the cell above or below.

Item	Description

Min X	Type
		 in the minimum X limit value in millimeters.

Max X	Type
		 in the maximum X limit value in millimeters.

Min Y	Type
		 in the minimum Y limit value in millimeters.

Max Y	Type
		 in the maximum Y limit value in millimeters.

Min Z	Type
		 in the minimum Z limit value in millimeters.

Max Z	Type
		 in the maximum Z limit value in millimeters.

Polarity	Sets
		 the polarity to output I/O at approach check.

Local	Selects
		 the local coordinate system.

Apply	Sets
		 the current values.

Restore	Reverts
		 to the previous values.

Clear	Clears
		 all values.

Setting both values to zero disables the limits.

Using the Box Wizard

(1)      Select [Robot Manager]-[Boxes] tab to show the [Boxes] page.

(2)      Click the [Box Wizard] button. The following dialog appears.

(3)      Select the Box number and local coordinate system to define and click the [Next] button.

(4)      Click the [Teach] button to show the [Teach first corner of box] page.

(5)      Jog the robot to the first corner to teach the position of it. Click the [Teach] button. The following dialog appears.

(6)      Teach the second to forth corners by following the steps (4) and (5).

(7)      Select the polarity to output the I/O

(8)      The new box definition is displayed as shown below.

Click [Finish] to apply the new definition.


---

# [Tools]-[Robot Manager]-[Jog and Teach] Page
**Type:** reference | **Section:** Operator

## Description
[Tools]-[Robot Manager]-[Jog and Teach] Page

[Tools]-[Robot Manager]-[Jog and Teach] Page

The [Jog & Teach] page is primarily used for jogging the robot to a desired position and teaching a point using the current coordinates and orientation.

You can jog the robot in World, Tool, Local, Joint, or ECP modes. You can also execute motion commands.

The [Robot Manager]-[Jog & Teach] page contains several controls, described below.


---

# labels
**Type:** reference | **Section:** Operator

## Description
labels

Labels

A program line is an alphanumeric name followed by a colon (":") that marks a location in a program for a GoTo or GoSub statement. The name may be up to 32 characters long and can include alphanumeric characters and the underscore ("_") character if it is not the first character. You cannot use any SPEL+ keywords as labels.

For example:

Function Main

  Do

    Jump P1

    Jump P2

    If Sw(1) Then GoTo MainAbort

  Loop

MainAbort: ' This is a program label.

  Print "Program aborted"

Fend

## Examples
```spel
Function Main Do
    Jump P1
    Jump P2
    If Sw(1) Then GoTo MainAbort Loop

MainAbort: ' This is a program label. Print "Program aborted"
Fend
```


---

# setup plane cmd
**Type:** reference | **Section:** Operator

## Description
setup plane cmd

[Tools]-[Robot Manager]-[Planes] Page

This page allows you to define Plane (approach check plane) settings for a robot. When the page is selected, the current values are displayed. When a Plane is undefined, then all fields for that Plane will be blank. When you enter a value in any of the fields for an undefined Plane setting, then the remaining fields will be set to zero. The Plane will be defined when you press the [Apply] button.

For more details on Planes settings, refer to the following manual:

SPEL+ Language Reference - Plane Statement

Navigating the grid

Press the [Tab] key to move to the next cell. Press the [Shift] + [Tab] key to move to the previous cell. Press the arrow [↑] or [↓] key to move to the cell above or below.

Item	Description

X	Sets
		 the X origin of the coordinate for approach check plane.

Y	Sets
		 the Y origin of the coordinate for approach check plane.

Z	Sets
		 the Z origin of the coordinate for approach check plane.

U	Sets
		 the U origin of the coordinate for approach check plane.

V	Sets
		 the V origin of the coordinate for approach check plane.

W	Sets
		 the W origin of the coordinate for approach check plane.

Apply	Sets
		 the current values.

Restore	Reverts
		 to the previous values.

Clear	Clears
		 all values.

Wizard

(1)      Select [Robot Manager]-[Planes] tab to show the [Planes] page.

(2)      Click the [Plane Wizard] button. The following dialog appears.

(3)      Select the plane number to define and the number of points to teach, and then click the [Next] button.

NOTE:  You can select either "1" or "3" for the number of points to teach. If you select "1", the robot posture at teaching will be reflected. If you select "3", the robot posture will not be reflected.

For more details, refer to the following manual:

SPEL+ Language Reference - Plane Statement

(4)      Click the [Teach] button to show the [Teach plane origin point] page.

If the number of point to teach is "1":

(5)      Jog the robot to the reference point to teach the position of it.

Click the [Teach] button. The following dialog appears.

(6)      The new plane definition is displayed as shown below. Click [Finish] to apply the new definition.

If the number of points to teach is "3":

Jog
	 the robot to the reference point to teach the position of it (Point
	 #1).

	Click the [Teach] button. The following dialog appears.

Teach
	 the X axis specified point (Point #2) and the Y axis specified point
	 (Point #3) in the same way as the step 1).

(7)    The new plane definition is displayed as shown below.

Click [Finish] to apply the new definition.


---

